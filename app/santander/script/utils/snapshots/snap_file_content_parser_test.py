# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['UserModelCase::test_header_cleaning_returns_right_snapshot FileContentParser.cleanHeaders_credit'] = [
    [
        'FECHA',
        'CONSECUTIVO',
        'CONCEPTO',
        'IMPORTE'
    ],
    [
        '01/Ene/2022',
        '0000001',
        'PAYPAL RAPI',
        '100.00'
    ]
]

snapshots['UserModelCase::test_header_cleaning_returns_right_snapshot FileContentParser.cleanHeaders_debit'] = [
    [
        'FECHA',
        'HORA',
        'SUCURSAL',
        'CONCEPTO',
        'RETIRO',
        'DEPOSITO',
        'SALDO',
        'REFERENCIA'
    ],
    [
        '01/Ene/2000',
        '12:00:00',
        '1111',
        'internet',
        '200.00',
        '',
        '99.99',
        '003332299'
    ]
]

snapshots['UserModelCase::test_that_df_has_correct_columns FileContentParser.getDf().columns_credit'] = GenericRepr("Index(['FECHA', 'CONSECUTIVO', 'CONCEPTO', 'IMPORTE'], dtype='object')")

snapshots['UserModelCase::test_that_df_has_correct_columns FileContentParser.getDf().columns_debit'] = GenericRepr("Index(['FECHA', 'HORA', 'SUCURSAL', 'CONCEPTO', 'RETIRO', 'DEPOSITO', 'SALDO',\n       'REFERENCIA'],\n      dtype='object')")
