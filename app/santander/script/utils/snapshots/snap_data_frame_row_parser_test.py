# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['DataFrameRowParserTest::test_correct_columns_are_dropped DataFrameRowParser.dropColumns_credit'] = GenericRepr("Index(['FECHA', 'CONCEPTO', 'IMPORTE'], dtype='object')")

snapshots['DataFrameRowParserTest::test_correct_columns_are_dropped DataFrameRowParser.dropColumns_debit'] = GenericRepr("Index(['FECHA', 'HORA', 'CONCEPTO', 'RETIRO', 'DEPOSITO'], dtype='object')")

snapshots['DataFrameRowParserTest::test_parsed_data_frame_columns_are_right DataFrameRowParser.parseDataFrame().columns_credit'] = GenericRepr("Index(['FECHA', 'description', 'inflow', 'outflow'], dtype='object')")

snapshots['DataFrameRowParserTest::test_parsed_data_frame_columns_are_right DataFrameRowParser.parseDataFrame().columns_debit'] = GenericRepr("Index(['FECHA', 'HORA', 'description', 'inflow', 'outflow'], dtype='object')")