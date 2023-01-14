# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['DataReconciliatorTest::test_naive_reconciliation_compliance DataReconciliator.reconciliate'] = {
    'create': [
        {
            'dateExecuted': '2022-01-02',
            'description': 'BIG CAESARS',
            'id': '0',
            'inflow': 0,
            'outflow': 90.1,
            'serialIndex': 'aba',
            'serialKey': 'BIG CAESARS___0___90100'
        },
        {
            'dateExecuted': '2022-05-29',
            'description': 'BUS TICKETS',
            'id': '0',
            'inflow': 0,
            'outflow': 1400.0,
            'serialIndex': 'eCb',
            'serialKey': 'BUS TICKETS___0___1400000'
        },
        {
            'dateExecuted': '2022-05-19',
            'description': 'CLOTHES',
            'id': '0',
            'inflow': 0,
            'outflow': 3500.0,
            'serialIndex': 'esa',
            'serialKey': 'CLOTHES___0___3500000'
        },
        {
            'dateExecuted': '2022-05-17',
            'description': 'MUSIC FESTIVAL',
            'id': '0',
            'inflow': 0,
            'outflow': 900.0,
            'serialIndex': 'eqc',
            'serialKey': 'MUSIC FESTIVAL___0___900000'
        },
        {
            'dateExecuted': '2022-01-01',
            'description': 'PAYPAL PETCO',
            'id': '0',
            'inflow': 0,
            'outflow': 400.0,
            'serialIndex': 'aaa',
            'serialKey': 'PAYPAL PETCO___0___400000'
        }
    ],
    'delete': [
        {
            'dateExecuted': '2022-05-19',
            'description': 'CAR FIX',
            'id': '14',
            'inflow': 0,
            'outflow': 8700.0,
            'serialIndex': 'esa',
            'serialKey': 'CAR FIX___0___8700000'
        },
        {
            'dateExecuted': '2022-05-17',
            'description': 'ICE CREAM',
            'id': '12',
            'inflow': 0,
            'outflow': 90.0,
            'serialIndex': 'eqb',
            'serialKey': 'ICE CREAM___0___90000'
        }
    ],
    'update': [
        {
            'dateExecuted': '2022-01-01',
            'description': 'PAYPAL RAPI',
            'id': '1',
            'inflow': 0,
            'outflow': 300.0,
            'serialIndex': 'aab',
            'serialKey': 'PAYPAL RAPI___0___300000'
        },
        {
            'dateExecuted': '2022-01-02',
            'description': 'PIZZA HOT',
            'id': '2',
            'inflow': 0,
            'outflow': 100.1,
            'serialIndex': 'abb',
            'serialKey': 'PIZZA HOT___0___100100'
        }
    ]
}
