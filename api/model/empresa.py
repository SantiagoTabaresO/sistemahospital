import functools
import db
import pymysql

def get_empresas():
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql="SELECT * FROM empresa"
        cursor.execute(sql)
        ret = cursor.fetchall()
        print(ret)
        return ret
    finally:
        con.close()

def get_empresa(empresa_id):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM empresa WHERE idempresa = {}".format(empresa_id)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def get_empresa_by_name(empresa_name):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM empresa WHERE nombre = '{}'".format(empresa_name)
        print(sql)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def create_empresa(name):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="INSERT INTO empresa(nombre) VALUES('{}')".format(name)
        print(sql)
        cursor.execute(sql)
        con.commit()
        id_org = cursor.lastrowid
        return {"message":"OK", "id": id_org}
    finally:
        con.close()

def update_empresa(name, company_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="UPDATE empresa set nombre='{0}', ' WHERE idempresa = {1}".format(name, company_id)
        print(sql)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()

def delete_empresa(empresa_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="DELETE FROM empresa WHERE idempresa = {}".format(empresa_id)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()
