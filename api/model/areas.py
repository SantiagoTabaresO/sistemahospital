import functools
import db
import pymysql

def get_areas():
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql="SELECT * FROM areas"
        cursor.execute(sql)
        ret = cursor.fetchall()
        print(ret)
        return ret
    finally:
        con.close()

def get_area(area_id):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM areas WHERE idareas = {}".format(area_id)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def get_area_by_name(area_name):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM areas WHERE nombre = '{}'".format(area_name)
        print(sql)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def create_area(name):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="INSERT INTO areas(nombre) VALUES('{}')".format(name)
        print(sql)
        cursor.execute(sql)
        con.commit()
        id_org = cursor.lastrowid
        return {"message":"OK", "id": id_org}
    finally:
        con.close()

def update_area(name, area_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="UPDATE areas set nombre='{0}' WHERE idareas = {1}".format(name, area_id)
        print(sql)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()

def delete_area(area_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="DELETE FROM areas WHERE idareas = {}".format(area_id)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()
