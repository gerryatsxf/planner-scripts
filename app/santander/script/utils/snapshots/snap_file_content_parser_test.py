# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['UserModelCase::test_get_file_content_returns_right_snapshot FileContentParser.getFileContent()_credit'] = '<html>    <head>        <title>            Movimientos Tarjeta Cr�dito        </title>    </head>    <body>        <table border="0">            <tr>                <td>                    <br>                    <table border="2">                        <tr>                            <td colspan="2" align="left">No. de Cuenta: &nbsp;<b>5555444422223333</b></td>                            <tr>                                <td colspan="2" align="left">Producto: &nbsp;<b>UNI SANTANDER K</b></td>                                <tr>                                    <td colspan="4" align="left">                                        <b>TASA DE INTER�S ANUALIZADA QUE SE COBRA SOBRE EL SALDO PROMEDIO INSOLUTO DEL PERIODO ANTERIOR:</b> &nbsp;71.11 &nbsp; %</td>                                        <tr>                                            <td colspan="2" align="left">Detalle del 01-01-2000 al 31-01-2000</td>                                            <td colspan="2" align="right">Total de movimientos:<b>1</b></td>                                        </tr>                                        <tr>                                            <td colspan="4">&nbsp;</td>                                        </tr>                                        <tr>                                            <td align="center">                                                <b>FECHA</b>                                            </td>                                            <td align="center">                                                <b>CONSECUTIVO</b>                                            </td>                                            <td align="center">                                                <b>CONCEPTO</b>                                            </td>                                            <td align="center">                                                <b>IMPORTE</b>                                            </td>                                            <tr>                                                <td align="center">01/Ene/2022</td>                                                <td align="center">0000001</td>                                                <td align="left">PAYPAL RAPI</td>                                                <td align="center">100.00</td>                                            </tr>                    </table>                </td>            </tr>        </table>        <br>    </body></html>'

snapshots['UserModelCase::test_get_file_content_returns_right_snapshot FileContentParser.getFileContent()_debit'] = '<html>    <head>        <title>            Movimientos Cuentas Chequeras        </title>    </head>    <body>        <table border="0">            <tr>                <td>                    <br>                    <table border="2">                        <tr>                            <td colspan="5" align="left">Detalle del 01-01-2000 al 31-01-2001 de la cuenta 022211155555</td>                            <td colspan="3" align="right">N&uacute;mero de registros:<b>1</b></td>                        </tr>                        <tr>                            <td colspan="8">&nbsp;</td>                        </tr>                        <tr>                            <td align="center">                                <b>FECHA</b>                            </td>                            <td align="center">                                <b>HORA</b>                            </td>                            <td align="center">                                <b>SUCURSAL</b>                            </td>                            <td align="center">                                <b>CONCEPTO</b>                            </td>                            <td align="center">                                <b>RETIRO</b>                            </td>                            <td align="center">                                <b>DEPOSITO</b>                            </td>                            <td align="center">                                <b>SALDO</b>                            </td>                            <td align="center">                                <b>REFERENCIA</b>                            </td>                        </tr>                        <tr>                            <td align="center">01/Ene/2000</td>                            <td align="center">12:00:00</td>                            <td align="left">1111</td>                            <td align="center">internet                      </td>                            <td align="center">200.00</td>                            <td align="center"></td>                            <td align="center">99.99</td>                            <td align="center">003332299      </td>                        </tr>                                </table>                </td>            </tr>        </table>        <br>    </body></html>'

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
