import pandas as pd
class DataReconciliator(object):

    def __init__(self, incoming, stored):
        
        new = pd.DataFrame(incoming)
        new['id'] = None
        new['source'] = 'incoming'
        self.incomingItems = new.to_dict('records')

        old = pd.DataFrame(stored)
        old['source'] = 'stored'
        self.storedItems = old.to_dict('records')

    def reconciliate(self):

        # Classify by repeated and non repeated items
        searchResult = self.findNonRepeatedItems()
        nonRepeated = searchResult['nonRepeated']
        allIncoming = searchResult['allIncoming']

        result = {
            'create':[],
            'update':[],
            'delete':[]
        }

        if len(nonRepeated) > 0 and not allIncoming:
            
            # We only care about non repeated since repeated items are just full matches between incoming items and stored items
            nonRepeated = pd.DataFrame(nonRepeated)
            
            # Rows to be updated are the duplicated non repeated ones; duplicated since there was a change in serialIndex due to list order changes
            reduced = nonRepeated.loc[(nonRepeated['serialKey'].duplicated(keep=False))].sort_values(['source','serialKey','serialIndex'])
            reduced['auxIndex'] = reduced['serialIndex'] + '___' + reduced['serialKey']
            reduced = reduced.loc[~(reduced['auxIndex'].duplicated(keep=False))]

            incoming = reduced.loc[reduced['source'] == 'incoming'].to_dict('records')
            stored = reduced.loc[reduced['source'] == 'stored'].to_dict('records')

            toUpdate = []

            while True:
                if len(incoming) == 0 or len(stored) == 0:
                    break 
                stored[0]['serialIndex___OLD'] = stored[0]['serialIndex']
                stored[0]['serialIndex'] = incoming[0]['serialIndex']
                toUpdate.append(stored[0])
                del incoming[0]
                del stored[0]

            foundDeleteItems = stored
            foundCreateItems = incoming

            result['update'] = toUpdate

            # Get rid of duplicated rows that have been handled already
            nonRepeated  = nonRepeated.loc[~nonRepeated['serialKey'].duplicated(keep=False)]

            # Unique rows with source from 'incoming' are new transactions to be created since they weren't found in the stored transactions
            toCreate = nonRepeated.loc[nonRepeated.source == 'incoming'].drop(columns='source')
            result['create'] = toCreate.to_dict('records')
            result['create'] = result['create'] + foundCreateItems

            # Unique rows with source from 'stored' are transactions to be bricked since they are no longer in the incoming records
            toDelete = nonRepeated.loc[nonRepeated.source == 'stored'].drop(columns='source')
            result['delete'] = toDelete.to_dict('records')
            result['delete'] = result['delete'] + foundDeleteItems

        elif len(nonRepeated) > 0 and allIncoming:
            result['create'] = nonRepeated

        return result

    def findNonRepeatedItems(self):

        if len(self.incomingItems) == 0:
            raise ValueError("AN EMPTY LIST OF INCOMING ITEMS WAS FETCHED")

        repeated = []
        nonRepeated = []
        allItemsAreIncoming = False

        if len(self.storedItems) > 0:

            items = self.incomingItems + self.storedItems
            items = sorted(items, key=lambda d: d['serialKey'], reverse=False)
            idx = 0

            while idx < len(items):

                localIdx = idx + 1
                itsRepeated = False

                # do not run while loop if we cannot assert that items[idx+1] (which is equivalent to items[localIdx]) exists
                if localIdx <= len(items)-1:
                    while items[idx]['serialKey'] == items[localIdx]['serialKey'] and items[idx]['serialIndex'] == items[localIdx]['serialIndex']:
                        localIdx = localIdx + 1
                        itsRepeated = True
                        if localIdx > len(items)-1:
                            break

                    if itsRepeated:
                        repeated.append(items[idx])
                        idx = localIdx
                        itsRepeated = False
                    else:
                        nonRepeated.append(items[idx])
                        idx = idx + 1
                # else, if we get to the point where localIdx equals list length, that means we are done with loop but still have one non-repeated item to be considering, the last item in the list
                elif localIdx == len(items):
                    nonRepeated.append(items[idx])
                    break
                # else, if localIdx it's just plain bigger than items list length, that means we are done
                elif localIdx > len(items):
                    break 
                
        else:
            nonRepeated = self.incomingItems
            allItemsAreIncoming = True

        return {
            'repeated': repeated,
            'nonRepeated': nonRepeated,
            'allIncoming': allItemsAreIncoming
        }
