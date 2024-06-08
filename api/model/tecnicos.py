import functools
import db
import pymysql

def get_tecnicos():
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql="SELECT * FROM tecnico"
        cursor.execute(sql)
        ret = cursor.fetchall()
        print(ret)
        return ret
    finally:
        con.close()

def get_tecnico(tecnico_id):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM tecnico WHERE idtecnico = {}".format(tecnico_id)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def get_tecnico_by_name(tecnico_nombre):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM tecnico WHERE nombre = '{}'".format(tecnico_nombre)
        print(sql)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def create_tecnico(nombre, empresa):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="INSERT INTO tecnico(nombre, empresa) VALUES('{}','{}')".format(nombre, empresa)
        print(sql)
        cursor.execute(sql)
        con.commit()
        id_org = cursor.lastrowid
        return {"message":"OK", "id": id_org}
    finally:
        con.close()

def update_tecnico(nombre, empresa, tecnico_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="UPDATE tecnico set nombre='{0}', empresa='{1}' WHERE idtecnico = {2}".format(nombre, empresa, tecnico_id)
        print(sql)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()

def delete_tecnico(tecnico_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="DELETE FROM tecnico WHERE idtecnico = {}".format(tecnico_id)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()
