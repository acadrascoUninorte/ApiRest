import sqlite3
from sqlite3 import Error
from conexion import sql_connection


# DML  CREATE, READ, UPDATE Y DELETE

def sql_insert_producto(id, nombre, precio, existencia):
    try:

        con = sql_connection()
        # sql="insert into Producto(id, nombre, precio, existencia) values("+str(id)+", '"+nombre+"', "+str(precio)+", "+str(existencia)+")"
        strSql = "insert into Producto(id, nombre, precio, existencia) values(?,?,?,?)"
        cursor = con.cursor()
        cursor.execute(strSql, (id, nombre, precio, existencia))
        con.commit()
        con.close()
    except Error:
        print(Error)


def sql_select_productos():
    try:
        sql = "SELECT * FROM Producto"
        con = sql_connection()
        cursor = con.cursor()
        cursor.execute(sql)
        productos = cursor.fetchall()
        return productos
    except Error:
        print(Error)


def sql_select_producto(id):
    try:
        sql = "SELECT * FROM Producto where id = "+str(id)+""
        con = sql_connection()
        cursor = con.cursor()
        cursor.execute(sql)
        producto = cursor.fetchone()
        return producto
    except Error:
        print(Error)


def sql_edit_producto(id, nombre):
   try:
     sql = "UPDATE Producto SET nombre = '" + \
         str(nombre)+"' where id = "+str(id)+""
     con = sql_connection()
     cursor = con.cursor()
     cursor.execute(sql)
     con.commit()
     con.close()
   except Error:
        print(Error)


def sql_delete_producto(id):
    try:
        sql="DELETE FROM Producto where id = "+str(id)+""
        con = sql_connection()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()
    except Error:
        print(Error)


