from database.db import conn
from database.db import mysql

conn = mysql.connect()

def get_data():
    query = "select * from gejala"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return result

def get_limit_asc():
    query = "select * from gejala where kode_gejala >= 'G001' and kode_gejala < 'G010'"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return result

def get_limit_desc():
    query = "select * from gejala where kode_gejala >= 'G010' and kode_gejala < 'G019'"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return result

def store(data):
    query = "insert into gejala values('"+ data[0] +"', '"+ data[1] +"')"
    cursor = conn.cursor()
    result = cursor.execute(query)
    conn.commit()

    return result

def show(id):
    query = "select * from gejala where kode_gejala='"+ id +"'"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return result

def update(id, data):
    query = "update gejala set gejala='"+ data[1] +"' where kode_gejala='"+ id +"'"
    cursor = conn.cursor()
    result = cursor.execute(query)
    conn.commit()

    return result

def delete(id):
    query = "delete from gejala where kode_gejala='"+ id +"'"
    cursor = conn.cursor()
    result = cursor.execute(query)
    conn.commit()

    return result