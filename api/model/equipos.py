import functools
import db
import pymysql

def get_equipos():
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql="SELECT * FROM equipos"
        cursor.execute(sql)
        ret = cursor.fetchall()
        print(ret)
        return ret
    finally:
        con.close()

def get_equipo(equipo_id):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM equipos WHERE idEquipos = {}".format(equipo_id)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def get_equipo_by_name(equipo_name):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM equipos WHERE nombre = '{}'".format(equipo_name)
        print(sql)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def create_equipo(name, description, facturacion, invima, riesgo, historial, proveedores, marcas, areas, responsables):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="INSERT INTO equipos(nombre, descripcion, facturacion, invima, riesgo, historial, proveedores, marcas, areas, responsables) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name, description, facturacion, invima, riesgo, historial, proveedores, marcas, areas, responsables)
        print(sql)
        cursor.execute(sql)
        con.commit()
        id_org = cursor.lastrowid
        return {"message":"OK", "id": id_org}
    finally:
        con.close()

def update_equipo(name, description, facturacion, invima, riesgo, historial, proveedores, marcas, areas, responsables, equipo_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="UPDATE equipos set nombre='{0}', descripcion='{1}', facturacion='{2}', invima='{3}', riesgo='{4}', historial='{5}', proveedores='{6}', marcas='{7}', areas='{8}', responsables='{9}', WHERE idEquipos = {10}".format(name, description, facturacion, invima, riesgo, historial, proveedores, marcas, areas, responsables, equipo_id)
        print(sql)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()

def delete_equipo(equipo_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="DELETE FROM equipos WHERE idEquipos = {}".format(equipo_id)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()
