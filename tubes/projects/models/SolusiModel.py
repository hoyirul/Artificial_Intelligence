from database.db import conn
from database.db import mysql

conn = mysql.connect()

def get_data():
    query = "select s.id, py.penyakit, pb.pengobatan from solusi s inner join penyakit py on s.kode_penyakit = py.kode_penyakit inner join pengobatan pb on s.kode_pengobatan = pb.kode_pengobatan"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return result

def store(data):
    query = "insert into solusi values(null,'"+ data[0] +"', '"+ data[1] +"')"
    cursor = conn.cursor()
    result = cursor.execute(query)
    conn.commit()

    return result

def show(id):
    query = "select s.id, py.penyakit, pb.pengobatan from solusi s inner join penyakit py on s.kode_penyakit = py.kode_penyakit inner join pengobatan pb on s.kode_pengobatan = pb.kode_pengobatan where id='"+ id +"'"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return result

def get_solusi(id):
    query = "select s.id, py.penyakit, pb.pengobatan from solusi s inner join penyakit py on s.kode_penyakit = py.kode_penyakit inner join pengobatan pb on s.kode_pengobatan = pb.kode_pengobatan where py.kode_penyakit='"+ id +"'"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return result

def update(id, data):
    query = "update solusi set kode_penyakit='"+ data[0] +"', kode_pengobatan='"+ data[1] +"' where id='"+ id +"'"
    cursor = conn.cursor()
    result = cursor.execute(query)
    conn.commit()

    return result

def delete(id):
    query = "delete from solusi where id='"+ id +"'"
    cursor = conn.cursor()
    result = cursor.execute(query)
    conn.commit()

    return result