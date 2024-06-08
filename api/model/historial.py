import functools
import db
import pymysql

def get_historiales():
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql="SELECT * FROM historial"
        cursor.execute(sql)
        ret = cursor.fetchall()
        print(ret)
        return ret
    finally:
        con.close()

def get_historial(historial_id):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM historial WHERE idhistorial = {}".format(historial_id)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def create_historial(fecha, descripcion, revision, mantenimiento, control, tecnico):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="INSERT INTO historial(fecha, descripcion, revision, mantenimiento, control, tecnico) VALUES('{}','{}','{}','{}','{}','{}')".format(fecha, descripcion,revision,mantenimiento,control,tecnico)
        print(sql)
        cursor.execute(sql)
        con.commit()
        id_org = cursor.lastrowid
        return {"message":"OK", "id": id_org}
    finally:
        con.close()

def update_historial(fecha, descripcion, revision, mantenimiento, control, tecnico, historial_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="UPDATE historial set fecha='{0}', descripcion='{1}', revision='{2}', mantenimiento='{3}', control='{4}', tecnico='{5}' ,  WHERE idhistorial = {6}".format(fecha,descripcion,revision,mantenimiento,control,tecnico, historial_id)
        print(sql)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()

def delete_historial(historial_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="DELETE FROM historial WHERE idhistorial = {}".format(historial_id)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()
