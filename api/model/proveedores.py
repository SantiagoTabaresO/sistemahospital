import functools
import db
import pymysql

def get_proveedores():
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql="SELECT * FROM proveedores"
        cursor.execute(sql)
        ret = cursor.fetchall()
        print(ret)
        return ret
    finally:
        con.close()

def get_proveedor(proveedor_id):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM proveedores WHERE idproveedores = {}".format(proveedor_id)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def get_proveedor_by_name(proveedor_name):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM proveedores WHERE nombre = '{}'".format(proveedor_name)
        print(sql)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def create_proveedor(nombre, pais):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="INSERT INTO proveedores(nombre, paisl) VALUES('{}','{}')".format(nombre, pais)
        print(sql)
        cursor.execute(sql)
        con.commit()
        id_org = cursor.lastrowid
        return {"message":"OK", "id": id_org}
    finally:
        con.close()

def update_proveedor(nombre, pais, proveedor_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="UPDATE proveedores set nombre='{0}', paisl='{1}' WHERE idproveedores = {2}".format(nombre, pais, proveedor_id)
        print(sql)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()

def delete_proveedor(proveedor_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="DELETE FROM proveedores WHERE idproveedores = {}".format(proveedor_id)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()
