# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['SantanderScriptTest::test_data_frame_gets_filtered_by_time_interval filterByDateInterval_credit'] = [
]

snapshots['SantanderScriptTest::test_data_frame_gets_filtered_by_time_interval filterByDateInterval_debit'] = [
    {
        'CONCEPTO': 'tacos',
        'DEPOSITO': '',
        'FECHA': '15/Ene/2000',
        'HORA': '12:00:982342535423',
        'REFERENCIA': '001112299',
        'RETIRO': '300.00',
        'SALDO': '109.99',
        'SUCURSAL': '1111',
        'dateExecuted': '2000-01-15'
    }
]

snapshots['SantanderScriptTest::test_xls_file_gets_parsed_correctly santander_script()_credit'] = [
    {
        'dateExecuted': '2022-01-01',
        'description': 'PAYPAL RAPI',
        'inflow': 0.0,
        'outflow': 100.0
    }
]

snapshots['SantanderScriptTest::test_xls_file_gets_parsed_correctly santander_script()_debit'] = [
    {
        'dateExecuted': '2000-01-01',
        'description': 'internet',
        'inflow': 0.0,
        'outflow': 200.0,
        'timeExecuted': '12:00:00'
    },
    {
        'dateExecuted': '2000-01-15',
        'description': 'tacos',
        'inflow': 0.0,
        'outflow': 300.0,
        'timeExecuted': '12:00:59'
    }
]
