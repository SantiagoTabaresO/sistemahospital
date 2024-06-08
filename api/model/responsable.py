import functools
import db
import pymysql

def get_responsables():
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql="SELECT * FROM responsable"
        cursor.execute(sql)
        ret = cursor.fetchall()
        print(ret)
        return ret
    finally:
        con.close()

def get_responsable(responsable_id):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM responsable WHERE idresponsable = {}".format(responsable_id)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def get_responsable_by_name(responsable_name):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM responsable WHERE nombre = '{}'".format(responsable_name)
        print(sql)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def create_responsable(nombre, descripcion):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="INSERT INTO responsable(nombre, descripcion) VALUES('{}','{}')".format(nombre, descripcion)
        print(sql)
        cursor.execute(sql)
        con.commit()
        id_org = cursor.lastrowid
        return {"message":"OK", "id": id_org}
    finally:
        con.close()

def update_responsable(nombre, descripcion, responsable_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="UPDATE responsable set nombre='{0}', descripcion='{1}' WHERE idresponsable = {2}".format(nombre, descripcion, responsable_id)
        print(sql)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()

def delete_responsable(responsable_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="DELETE FROM responsable WHERE idresponsable = {}".format(responsable_id)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()
