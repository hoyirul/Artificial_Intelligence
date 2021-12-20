from database.db import conn
from database.db import mysql

conn = mysql.connect()

def get_data():
    query = "select * from penyakit"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return result

def store(data):
    query = "insert into penyakit values('"+ data[0] +"', '"+ data[1] +"', '"+ data[2] +"')"
    cursor = conn.cursor()
    result = cursor.execute(query)
    conn.commit()

    return result

def show(id):
    query = "select * from penyakit where kode_penyakit='"+ id +"'"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return result

def update(id, data):
    query = "update penyakit set penyakit='"+ data[1] +"' deskripsi='"+ data[2] +"' where kode_penyakit='"+ id +"'"
    cursor = conn.cursor()
    result = cursor.execute(query)
    conn.commit()

    return result

def delete(id):
    query = "delete from penyakit where kode_penyakit='"+ id +"'"
    cursor = conn.cursor()
    result = cursor.execute(query)
    conn.commit()

    return result