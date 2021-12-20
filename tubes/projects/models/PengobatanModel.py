from database.db import conn
from database.db import mysql

conn = mysql.connect()

def get_data():
    query = "select * from pengobatan"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return result

def store(data):
    query = "insert into pengobatan values('"+ data[0] +"', '"+ data[1] +"')"
    cursor = conn.cursor()
    result = cursor.execute(query)
    conn.commit()

    return result

def show(id):
    query = "select * from pengobatan where kode_pengobatan='"+ id +"'"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return result

def update(id, data):
    query = "update pengobatan set pengobatan='"+ data[1] +"' where kode_pengobatan='"+ id +"'"
    cursor = conn.cursor()
    result = cursor.execute(query)
    conn.commit()

    return result

def delete(id):
    query = "delete from pengobatan where kode_pengobatan='"+ id +"'"
    cursor = conn.cursor()
    result = cursor.execute(query)
    conn.commit()

    return result