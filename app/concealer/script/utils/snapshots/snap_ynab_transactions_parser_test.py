# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['YnabTransactionsParserTest::test_naive_parsing_compliance YnabTransactionsParser.getTransactions'] = [
    {
        'dateExecuted': '2022-01-01',
        'description': 'PAYPAL RAPI',
        'id': '1',
        'inflow': 300.0,
        'outflow': 0.0,
        'serialIndex': 'aaa',
        'serialKey': 'PAYPAL RAPI___300000___0',
        'transfer_account_id': 'im an id'
    },
    {
        'dateExecuted': '2022-01-02',
        'description': 'PIZZA HOT',
        'id': '2',
        'inflow': 0.0,
        'outflow': 100.10000000000001,
        'serialIndex': 'aba',
        'serialKey': 'PIZZA HOT___0___100100',
        'transfer_account_id': 0
    },
    {
        'dateExecuted': '2022-01-15',
        'description': 'DISH SOAP',
        'id': '3',
        'inflow': 30.01,
        'outflow': 0.0,
        'serialIndex': 'aoa',
        'serialKey': 'DISH SOAP___30010___0',
        'transfer_account_id': 0
    },
    {
        'dateExecuted': '2022-02-01',
        'description': 'RENT',
        'id': '4',
        'inflow': 10000.0,
        'outflow': 0.0,
        'serialIndex': 'baa',
        'serialKey': 'RENT___10000000___0',
        'transfer_account_id': 0
    },
    {
        'dateExecuted': '2022-02-01',
        'description': 'NETFLIS',
        'id': '5',
        'inflow': 110.0,
        'outflow': 0.0,
        'serialIndex': 'bab',
        'serialKey': 'NETFLIS___110000___0',
        'transfer_account_id': 0
    },
    {
        'dateExecuted': '2022-02-01',
        'description': 'INTERNET',
        'id': '6',
        'inflow': 300.0,
        'outflow': 0.0,
        'serialIndex': 'bac',
        'serialKey': 'INTERNET___300000___0',
        'transfer_account_id': 0
    },
    {
        'dateExecuted': '2022-02-01',
        'description': 'HBO',
        'id': '7',
        'inflow': 80.0,
        'outflow': 0.0,
        'serialIndex': 'bad',
        'serialKey': 'HBO___80000___0',
        'transfer_account_id': 0
    },
    {
        'dateExecuted': '2022-02-15',
        'description': 'BURGER QUEEN',
        'id': '8',
        'inflow': 150.0,
        'outflow': 0.0,
        'serialIndex': 'boa',
        'serialKey': 'BURGER QUEEN___150000___0',
        'transfer_account_id': 0
    },
    {
        'dateExecuted': '2022-02-15',
        'description': 'JHONNY AIRPLANES',
        'id': '9',
        'inflow': 200.0,
        'outflow': 0.0,
        'serialIndex': 'bob',
        'serialKey': 'JHONNY AIRPLANES___200000___0',
        'transfer_account_id': 0
    },
    {
        'dateExecuted': '2022-02-16',
        'description': 'PAYPAL AMAZONG',
        'id': '10',
        'inflow': 650.0,
        'outflow': 0.0,
        'serialIndex': 'bpa',
        'serialKey': 'PAYPAL AMAZONG___650000___0',
        'transfer_account_id': 0
    },
    {
        'dateExecuted': '2022-05-17',
        'description': 'MOVIES',
        'id': '11',
        'inflow': 300.0,
        'outflow': 0.0,
        'serialIndex': 'eqa',
        'serialKey': 'MOVIES___300000___0',
        'transfer_account_id': 0
    },
    {
        'dateExecuted': '2022-05-17',
        'description': 'ICE CREAM',
        'id': '12',
        'inflow': 90.0,
        'outflow': 0.0,
        'serialIndex': 'eqb',
        'serialKey': 'ICE CREAM___90000___0',
        'transfer_account_id': 0
    },
    {
        'dateExecuted': '2022-05-18',
        'description': 'BOOKS',
        'id': '13',
        'inflow': 400.0,
        'outflow': 0.0,
        'serialIndex': 'era',
        'serialKey': 'BOOKS___400000___0',
        'transfer_account_id': 0
    },
    {
        'dateExecuted': '2022-05-19',
        'description': 'CLOTHES',
        'id': '14',
        'inflow': 3500.0,
        'outflow': 0.0,
        'serialIndex': 'esa',
        'serialKey': 'CLOTHES___3500000___0',
        'transfer_account_id': 0
    },
    {
        'dateExecuted': '2022-05-29',
        'description': 'AIRPLANE TICKETS',
        'id': '15',
        'inflow': 7000.0,
        'outflow': 0.0,
        'serialIndex': 'eCa',
        'serialKey': 'AIRPLANE TICKETS___7000000___0',
        'transfer_account_id': 0
    }
]
