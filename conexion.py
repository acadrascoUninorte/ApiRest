import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('C:\\Users\\Administrador\\Documents\\SQLiteStudio\\Ejercicio4.db')
        print(con)
        return con
    except Error:
        print(Error)


#Crear la base de datos Ejercicio4.db
#sql_connection()