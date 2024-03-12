#!/usr/bin/env python
# coding: utf-8

# ## Connection


import pyodbc

driver="SQL Server"
server = 'DESKTOP-HD9OHSA\MSSQLEXPRESS'

connection = pyodbc.connect( f'DRIVER={{SQL Server}};SERVER={server};trusted_connection=yes')

cursor = connection.cursor()


# ## Available Database Names

# In[3]:


cursor.execute('SELECT name FROM sys.databases')
cursor.fetchall()


# ## Table Names
# Tables available in that data base

# In[4]:


cursor.execute("USE master")
cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_type='BASE TABLE'")
cursor.fetchall()


# In[ ]:




