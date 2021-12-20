from database.db import conn
from database.db import mysql
conn = mysql.connect()

def get_data():
    query = "select pa.id_pasien, pa.nama, pa.umur, pa.alamat, pe.penyakit, pa.tanggal from pasien pa inner join penyakit pe on pe.kode_penyakit = pa.kode_penyakit"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return result

def store(data):
    query = "insert into pasien values('"+ data[0] +"', '"+ data[1] +"', '"+ data[2] +"', '"+ data[3] +"', '"+ data[4] +"', '"+ data[5] +"')"
    cursor = conn.cursor()
    result = cursor.execute(query)
    conn.commit()

    return result

def show(id):
    query = "select pa.id_pasien, pa.nama, pa.umur, pa.alamat, pe.penyakit, pe.deskripsi, pa.tanggal, pe.kode_penyakit from pasien pa inner join penyakit pe on pe.kode_penyakit = pa.kode_penyakit where id_pasien='"+ id +"'"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return result

def update(id, data):
    query = "update pasien set kode_penyakit='"+ data[0] +"', nama='"+ data[1] +"', alamat='"+ data[2] +"', umur='"+ data[3] +"', tanggal='"+ data[4] +"' where id_pasien='"+ id +"'"
    cursor = conn.cursor()
    result = cursor.execute(query)
    conn.commit()

    return result

def delete(id):
    query = "delete from pasien where id_pasien='"+ id +"'"
    cursor = conn.cursor()
    result = cursor.execute(query)
    conn.commit()

    return result

def store_detail(data):
    query = "insert into detail values('"+ data[0] +"', '"+ data[1] +"')"
    cursor = conn.cursor()
    result = cursor.execute(query)
    conn.commit()

    return result

def get_detail(id):
    query = "select ga.kode_gejala, ga.gejala from pasien p inner join detail d on d.id_pasien = p.id_pasien inner join gejala ga on ga.kode_gejala = d.kode_gejala where p.id_pasien='"+ id +"'"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return result