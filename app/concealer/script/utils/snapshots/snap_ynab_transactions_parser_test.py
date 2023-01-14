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
        'inflow': 0.0,
        'outflow': 300.0,
        'serialIndex': 'aaa',
        'serialKey': 'PAYPAL RAPI___0___300000'
    },
    {
        'dateExecuted': '2022-01-02',
        'description': 'PIZZA HOT',
        'id': '2',
        'inflow': 0.0,
        'outflow': 100.1,
        'serialIndex': 'aba',
        'serialKey': 'PIZZA HOT___0___100100'
    },
    {
        'dateExecuted': '2022-01-15',
        'description': 'DISH SOAP',
        'id': '3',
        'inflow': 0.0,
        'outflow': 30.01,
        'serialIndex': 'aoa',
        'serialKey': 'DISH SOAP___0___30010'
    },
    {
        'dateExecuted': '2022-02-01',
        'description': 'RENT',
        'id': '4',
        'inflow': 0.0,
        'outflow': 10000.0,
        'serialIndex': 'baa',
        'serialKey': 'RENT___0___10000000'
    },
    {
        'dateExecuted': '2022-02-01',
        'description': 'NETFLIS',
        'id': '5',
        'inflow': 0.0,
        'outflow': 110.0,
        'serialIndex': 'bab',
        'serialKey': 'NETFLIS___0___110000'
    },
    {
        'dateExecuted': '2022-02-01',
        'description': 'INTERNET',
        'id': '6',
        'inflow': 0.0,
        'outflow': 300.0,
        'serialIndex': 'bac',
        'serialKey': 'INTERNET___0___300000'
    },
    {
        'dateExecuted': '2022-02-01',
        'description': 'HBO',
        'id': '7',
        'inflow': 0.0,
        'outflow': 80.0,
        'serialIndex': 'bad',
        'serialKey': 'HBO___0___80000'
    },
    {
        'dateExecuted': '2022-02-15',
        'description': 'BURGER QUEEN',
        'id': '8',
        'inflow': 0.0,
        'outflow': 150.0,
        'serialIndex': 'boa',
        'serialKey': 'BURGER QUEEN___0___150000'
    },
    {
        'dateExecuted': '2022-02-15',
        'description': 'JHONNY AIRPLANES',
        'id': '9',
        'inflow': 0.0,
        'outflow': 200.0,
        'serialIndex': 'bob',
        'serialKey': 'JHONNY AIRPLANES___0___200000'
    },
    {
        'dateExecuted': '2022-02-16',
        'description': 'PAYPAL AMAZONG',
        'id': '10',
        'inflow': 0.0,
        'outflow': 650.0,
        'serialIndex': 'bpa',
        'serialKey': 'PAYPAL AMAZONG___0___650000'
    },
    {
        'dateExecuted': '2022-05-17',
        'description': 'MOVIES',
        'id': '11',
        'inflow': 0.0,
        'outflow': 300.0,
        'serialIndex': 'eqa',
        'serialKey': 'MOVIES___0___300000'
    },
    {
        'dateExecuted': '2022-05-17',
        'description': 'ICE CREAM',
        'id': '12',
        'inflow': 0.0,
        'outflow': 90.0,
        'serialIndex': 'eqb',
        'serialKey': 'ICE CREAM___0___90000'
    },
    {
        'dateExecuted': '2022-05-18',
        'description': 'BOOKS',
        'id': '13',
        'inflow': 0.0,
        'outflow': 400.0,
        'serialIndex': 'era',
        'serialKey': 'BOOKS___0___400000'
    },
    {
        'dateExecuted': '2022-05-19',
        'description': 'CLOTHES',
        'id': '14',
        'inflow': 0.0,
        'outflow': 3500.0,
        'serialIndex': 'esa',
        'serialKey': 'CLOTHES___0___3500000'
    },
    {
        'dateExecuted': '2022-05-29',
        'description': 'AIRPLANE TICKETS',
        'id': '15',
        'inflow': 0.0,
        'outflow': 7000.0,
        'serialIndex': 'eCa',
        'serialKey': 'AIRPLANE TICKETS___0___7000000'
    }
]
