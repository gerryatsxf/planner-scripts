import pandas as pd


def print_debug(item):
    if item['dateExecuted'] == '2023-07-23':
        print(item)

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

        self.filter_items()

        # Classify by repeated and non-repeated items
        search_result = self.find_non_repeated_items()

        non_repeated = search_result['nonRepeated']
        all_incoming = search_result['allIncoming']

        result = {
            'create': [],
            'update': [],
            'delete': []
        }

        if len(non_repeated) > 0 and not all_incoming:

            # We only care about non-repeated since repeated items are just full matches between incoming items and
            # stored items
            non_repeated = pd.DataFrame(non_repeated)

            # Rows to be updated are the duplicated non-repeated ones; duplicated since there was a change in
            # serialIndex due to list order changes
            reduced = non_repeated.loc[(non_repeated['serialKey'].duplicated(keep=False))].sort_values(
                ['source', 'serialKey', 'serialIndex'])
            reduced['auxIndex'] = reduced['serialIndex'] + '___' + reduced['serialKey']
            reduced = reduced.loc[~(reduced['auxIndex'].duplicated(keep=False))]
            incoming = reduced.loc[reduced['source'] == 'incoming'].to_dict('records')
            stored = reduced.loc[reduced['source'] == 'stored'].to_dict('records')

            to_update = []

            #print(incoming)

            while True:
                if len(incoming) == 0 or len(stored) == 0:
                    break
                stored[0]['serialIndex___OLD'] = stored[0]['serialIndex']
                stored[0]['serialIndex'] = incoming[0]['serialIndex']
                to_update.append(stored[0])
                del incoming[0]
                del stored[0]

            found_delete_items = stored
            found_create_items = incoming

            result['update'] = to_update

            # Get rid of duplicated rows that have been handled already
            non_repeated = non_repeated.loc[~non_repeated['serialKey'].duplicated(keep=False)]

            # Unique rows with source from 'incoming' are new transactions to be created since they weren't found in
            # the stored transactions
            to_create = non_repeated.loc[non_repeated.source == 'incoming'].drop(columns='source')
            result['create'] = to_create.to_dict('records')
            result['create'] = result['create'] + found_create_items

            # Unique rows with source from 'stored' are transactions to be bricked since they are no longer in the
            # incoming records
            to_delete = non_repeated.loc[non_repeated.source == 'stored'].drop(columns='source')
            result['delete'] = to_delete.to_dict('records')
            result['delete'] = result['delete'] + found_delete_items

        elif len(non_repeated) > 0 and all_incoming:
            result['create'] = non_repeated

        return result
    
    # TODO: write tests
    def get_reconciliation_interval(self):
        max_date = '1900-01-01'
        min_date = '2100-12-31'
        for el in self.incomingItems:
            if el['dateExecuted'] < min_date:
                min_date = el['dateExecuted']
            if el['dateExecuted'] > max_date:
                max_date = el['dateExecuted']
        return {
            'max_date': max_date,
            'min_date': min_date
        }

    # TODO: write tests
    def filter_items(self):
        interval = self.get_reconciliation_interval()
        
        filtered = []
        for s in self.incomingItems:
            if s['dateExecuted'] >= interval['min_date'] and s['dateExecuted'] <= interval['max_date']:
                filtered.append(s)
        self.incomingItems = filtered

        filtered = []
        for s in self.storedItems:
            if s['dateExecuted'] >= interval['min_date'] and s['dateExecuted'] <= interval['max_date']:
                filtered.append(s)
        self.storedItems = filtered

    def find_non_repeated_items(self):

        if len(self.incomingItems) == 0:
            raise ValueError("AN EMPTY LIST OF INCOMING ITEMS WAS FETCHED")

        repeated = []
        non_repeated = []
        all_items_are_incoming = False

        if len(self.storedItems) > 0:

            items = self.incomingItems + self.storedItems
            items = sorted(items, key=lambda d: d['serialKey'], reverse=False)
            idx = 0

            while idx < len(items):

                local_idx = idx + 1
                its_repeated = False

                # do not run while loop if we cannot assert that items[idx+1] (which is equivalent to items[
                # localIdx]) exists
                if local_idx <= len(items) - 1:
                    while items[idx]['serialKey'] == items[local_idx]['serialKey'] and items[idx]['serialIndex'] == \
                            items[local_idx]['serialIndex']:
                        local_idx = local_idx + 1
                        its_repeated = True
                        if local_idx > len(items) - 1:
                            break

                    if its_repeated:
                        repeated.append(items[idx])
                        idx = local_idx
                    else:
                        non_repeated.append(items[idx])
                        idx = idx + 1
                # else, if we get to the point where localIdx equals list length, that means we are done with loop
                # but still have one non-repeated item to be considering, the last item in the list
                elif local_idx == len(items):
                    non_repeated.append(items[idx])
                    break
                # else, if localIdx it's just plain bigger than items list length, that means we are done
                elif local_idx > len(items):
                    break

        else:
            non_repeated = self.incomingItems
            all_items_are_incoming = True

        return {
            'repeated': repeated,
            'nonRepeated': non_repeated,
            'allIncoming': all_items_are_incoming
        }
