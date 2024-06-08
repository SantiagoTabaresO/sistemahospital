import functools
import db
import pymysql

def get_marcas():
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql="SELECT * FROM marcas"
        cursor.execute(sql)
        ret = cursor.fetchall()
        print(ret)
        return ret
    finally:
        con.close()

def get_marca(marca_id):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM marcas WHERE idmarcas = {}".format(marca_id)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def get_marca_by_name(marca_name):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM marcas WHERE nombre = '{}'".format(marca_name)
        print(sql)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def create_marca(nombre, pais):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="INSERT INTO marcas(nombre, pais) VALUES('{}','{}')".format(nombre, pais)
        print(sql)
        cursor.execute(sql)
        con.commit()
        id_org = cursor.lastrowid
        return {"message":"OK", "id": id_org}
    finally:
        con.close()

def update_marca(nombre, pais, marcas_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="UPDATE marcas set nombre='{0}', pais='{1}' WHERE idmarcas = {2}".format(nombre, pais, marcas_id)
        print(sql)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()

def delete_marca(marcas_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="DELETE FROM marcas WHERE idmarcas = {}".format(marcas_id)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()
