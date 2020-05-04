'''
Created on Apr 28, 2020

@author: apfox
'''

import sqlite3
from sqlite3 import Error 

def createConnection(db_file):
    """Create Connection to SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return conn

def createTable(conn , tableCreation):
    
    try:
        c = conn.cursor()
        c.execute(tableCreation)
    except Error as e:
        print(e)

def main():
    
    database = r"C:\sqlite\db\reservation.db"
    
    createCustomerTable = """CREATE TABLE IF NOT EXISTS customer (
                                customerId integer PRIMARY KEY,
                                firstName character(30),
                                lastName character(30) NOT NULL,
                                email character(20) NOT NULL,
                                phone character(12) NOT NULL,
                                address character(30) NOT NULL,
                                salesDate date NOT NULL); """
    
    createSalesTable = """CREATE TABLE IF NOT EXISTS sales (
                                saleID integer PRIMARY KEY,
                                custumoerId integer NOT NULL,
                                resivervationDate date NOT NULL,
                                extraServices character(30) NOT NULL,
                                costExtraServices money NOT NULL,
                                totalCost money NOT NULL);"""
    
    conn = createConnection(database)
    
    if conn is not None:
        createTable(conn , createCustomerTable)
        
        createTable(conn , createSalesTable)

if __name__ == '__main__':
    main()