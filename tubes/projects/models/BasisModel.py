from database.db import conn
from database.db import mysql

conn = mysql.connect()

def get_data():
    query = "select bp.id, py.penyakit, gj.gejala from basis_pengetahuan bp inner join penyakit py on bp.kode_penyakit = py.kode_penyakit inner join gejala gj on bp.kode_gejala = gj.kode_gejala"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return result

def get_rules():
    query = "select * from basis_pengetahuan bp inner join penyakit py on bp.kode_penyakit = py.kode_penyakit inner join gejala gj on bp.kode_gejala = gj.kode_gejala"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return result

def store(data):
    query = "insert into basis_pengetahuan values(null, '"+ data[0] +"', '"+ data[1] +"')"
    cursor = conn.cursor()
    result = cursor.execute(query)
    conn.commit()

    return result

def get_where_penyakit(id):
    query = "select kode_gejala from basis_pengetahuan where kode_penyakit='"+ id +"'"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return result

def show(id):
    query = "select * from basis_pengetahuan where id='"+ id +"'"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return result

def update(id, data):
    query = "update basis_pengetahuan set kode_penyakit='"+ data[0] +"', kode_gejala='"+ data[1] +"' where id='"+ id +"'"
    cursor = conn.cursor()
    result = cursor.execute(query)
    conn.commit()

    return result

def delete(id):
    query = "delete from basis_pengetahuan where id='"+ id +"'"
    cursor = conn.cursor()
    result = cursor.execute(query)
    conn.commit()

    return result