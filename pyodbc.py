#!/usr/bin/env python
# coding: utf-8


import pyodbc

driver="SQL Server"
server = 'DESKTOP-HD9OHSA\MSSQLEXPRESS'
database = 'Database_name'

connection = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};trusted_connection=yes')

cursor = connection.cursor()

cursor.execute('SELECT * FROM table_name')
cursor.fetchall()

