import pandas as pd

class DataReconciliator(object):

    def __init__(self, incoming, stored):
        
        new = pd.DataFrame(incoming)
        new['id'] = '0'
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
            reduced = nonRepeated.loc[(nonRepeated['serialKey'].duplicated(keep=False))] # if serialKey is duplicated, row only changed serial position
            reduced = reduced.sort_values(['serialKey','serialIndex'])
            cols = ['dateExecuted','description','inflow','outflow']
            toUpdate = reduced.groupby(cols)['serialIndex'].apply(lambda x: '-'.join(x)).reset_index()
            toUpdate['newSerialIndex'] = toUpdate['serialIndex'].str[-3:]
            toUpdate['serialIndex']  = toUpdate['serialIndex'].str[:3]
            toUpdate['id'] = pd.merge(reduced,toUpdate,left_on='serialIndex', right_on='serialIndex', how='inner')['id']
            toUpdate['serialIndex'] = toUpdate['newSerialIndex']
            toUpdate = toUpdate.drop(columns='newSerialIndex')
            result['update'] = toUpdate.to_dict('records')

            # Get rid of duplicated rows that have been handled already
            nonRepeated  = nonRepeated.loc[~nonRepeated['serialKey'].duplicated(keep=False)]

            # Unique rows with source from 'incoming' are new transactions to be created since they weren't found in the stored transactions
            toCreate = nonRepeated.loc[nonRepeated.source == 'incoming'].drop(columns='source')
            result['create'] = toCreate.to_dict('records')

            # Unique rows with source from 'stored' are transactions to be bricked since they are no longer in the incoming records
            toDelete = nonRepeated.loc[nonRepeated.source == 'stored'].drop(columns='source')
            result['delete'] = toDelete.to_dict('records')

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
                if localIdx > len(items)-1:
                    break
                itsRepeated = False

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

        else:
            nonRepeated = self.incomingItems
            allItemsAreIncoming = True

        return {
            'repeated': repeated,
            'nonRepeated': nonRepeated,
            'allIncoming': allItemsAreIncoming
        }
