import re
from typing import get_args
from flask import Flask, render_template, request, redirect, url_for
import json, os, string, random, time
from models import PenyakitModel
from models import GejalaModel
from models import PengobatanModel
from models import BasisModel
from models import SolusiModel
from models import PasienModel

date_now = time.strftime('%Y-%m-%d')

app = Flask(__name__)

# Home
@app.route('/')
def home():
    return render_template('index.html')

# Gejala
@app.route('/gejala')
def gejala():
    result = GejalaModel.get_data()

    return render_template('/gejala/index.html', data=result)

@app.route('/gejala/store', methods=['POST'])
def gejala_store():
    msg = ""
    if request.method == 'POST': 
        data = [
            request.form['kode_gejala'],
            request.form['nama_gejala']
        ]
        result = GejalaModel.store(data)
        # cursor.execute(query)
        if result:
            msg = redirect(url_for('gejala'))
        else:
            msg = redirect(url_for('gejala'))

    return msg
    # return 

@app.route('/gejala/show/<id>')
def gejala_show(id):
    result = GejalaModel.show(id)

    return render_template('/gejala/edit.html', data=result)

@app.route('/gejala/update/<id>', methods=['POST'])
def gejala_update(id):
    if request.method == 'POST':
        data = [
            request.form['kode_gejala'],
            request.form['nama_gejala']
        ]
        result = GejalaModel.update(id, data)
        if result:
            msg = redirect(url_for('gejala'))
        else:
            msg = redirect(url_for('gejala'))

    return msg

@app.route('/gejala/delete/<id>')
def gejala_delete(id):
    result = GejalaModel.delete(id)
    if result:
        msg = redirect(url_for('gejala'))
    else:
        redirect(url_for('gejala'))

    return msg

# Penyakit
@app.route('/penyakit')
def penyakit():
    result = PenyakitModel.get_data()

    return render_template('/penyakit/index.html', data=result)

# Pengobatan
@app.route('/pengobatan')
def pengobatan():
    result = PengobatanModel.get_data()
    return render_template('/pengobatan/index.html', data=result)

@app.route('/pengobatan/store', methods=['POST'])
def pengobatan_store():
    msg = ""
    if request.method == 'POST': 
        data = [
            request.form['kode_pengobatan'],
            request.form['nama_pengobatan']
        ]
        result = PengobatanModel.store(data)
        # cursor.execute(query)
        if result:
            msg = redirect(url_for('pengobatan'))
        else:
            msg = redirect(url_for('pengobatan'))

    return msg
    # return 

@app.route('/pengobatan/show/<id>')
def pengobatan_show(id):
    result = PengobatanModel.show(id)

    return render_template('/pengobatan/edit.html', data=result)

@app.route('/pengobatan/update/<id>', methods=['POST'])
def pengobatan_update(id):
    if request.method == 'POST':
        data = [
            request.form['kode_pengobatan'],
            request.form['nama_pengobatan']
        ]
        result = PengobatanModel.update(id, data)
        if result:
            msg = redirect(url_for('pengobatan'))
        else:
            msg = redirect(url_for('pengobatan'))

    return msg

@app.route('/pengobatan/delete/<id>')
def pengobatan_delete(id):
    result = PengobatanModel.delete(id)
    if result:
        msg = redirect(url_for('pengobatan'))
    else:
        redirect(url_for('pengobatan'))

    return msg

# Basis Pengetahuan
@app.route('/basis')
def basis():
    result = BasisModel.get_data()
    penyakit = PenyakitModel.get_data()
    gejala = GejalaModel.get_data()
    return render_template('/basis/index.html', data=result, penyakit=penyakit, gejala=gejala)

@app.route('/basis/store', methods=['POST'])
def basis_store():
    msg = ""
    if request.method == 'POST': 
        data = [
            request.form['kode_penyakit'],
            request.form['kode_gejala']
        ]
        result = BasisModel.store(data)
        # cursor.execute(query)
        if result:
            msg = redirect(url_for('basis'))
        else:
            msg = redirect(url_for('basis'))

    return msg
    # return 

@app.route('/basis/show/<id>')
def basis_show(id):
    result = BasisModel.show(id)
    penyakit = PenyakitModel.get_data()
    gejala = GejalaModel.get_data()
    return render_template('/basis/edit.html', data=result, penyakit=penyakit, gejala=gejala)

@app.route('/basis/update/<id>', methods=['POST'])
def basis_update(id):
    if request.method == 'POST':
        data = [
            request.form['kode_penyakit'],
            request.form['kode_gejala']
        ]
        result = BasisModel.update(id, data)
        if result:
            msg = redirect(url_for('basis'))
        else:
            msg = redirect(url_for('basis'))

    return msg

@app.route('/basis/delete/<id>')
def basis_delete(id):
    result = BasisModel.delete(id)
    if result:
        msg = redirect(url_for('basis'))
    else:
        redirect(url_for('basis'))

    return msg

# Solusi
@app.route('/solusi')
def solusi():
    result = SolusiModel.get_data()
    penyakit = PenyakitModel.get_data()
    pengobatan = PengobatanModel.get_data()
    return render_template('/solusi/index.html', data=result, penyakit=penyakit, pengobatan=pengobatan)

@app.route('/solusi/store', methods=['POST'])
def solusi_store():
    msg = ""
    if request.method == 'POST': 
        data = [
            request.form['kode_penyakit'],
            request.form['kode_pengobatan']
        ]
        result = SolusiModel.store(data)
        # cursor.execute(query)
        if result:
            msg = redirect(url_for('solusi'))
        else:
            msg = redirect(url_for('solusi'))

    return msg
    # return 

@app.route('/solusi/show/<id>')
def solusi_show(id):
    result = SolusiModel.show(id)
    penyakit = PenyakitModel.get_data()
    pengobatan = PengobatanModel.get_data()
    return render_template('/solusi/edit.html', data=result, penyakit=penyakit, pengobatan=pengobatan)

@app.route('/solusi/update/<id>', methods=['POST'])
def solusi_update(id):
    if request.method == 'POST':
        data = [
            request.form['kode_penyakit'],
            request.form['kode_pengobatan']
        ]
        result = SolusiModel.update(id, data)
        if result:
            msg = redirect(url_for('solusi'))
        else:
            msg = redirect(url_for('solusi'))

    return msg

@app.route('/solusi/delete/<id>')
def solusi_delete(id):
    result = SolusiModel.delete(id)
    if result:
        msg = redirect(url_for('solusi'))
    else:
        redirect(url_for('solusi'))

    return msg

@app.route('/konsultasi')
def konsultasi():
    data = GejalaModel.get_data()
    errors = False
    return render_template('/konsultasi/index.html', data=data, errors=errors)

def akurasi(g):
    errors = False
    id_pasien = random_string()

    # RULES
    p1 = ["G001", "G002", "G003", "G012", "G019"]
    p2 = ["G001", "G002", "G003", "G004", "G005", "G006", "G007", "G008", "G009", "G010", "G011", "G012", "G013"]
    p3 = ["G001", "G002", "G003", "G004", "G006", "G007", "G008", "G009", "G010", "G011", "G012", "G013"]
    p4 = ["G001", "G002", "G003", "G004", "G006", "G014", "G015", "G016", "G017"]

    # Rule akan di looping dan di cek datanya sesuai rule
    # dan akan di cek akurasi oleh sistem akurasi terbesarlah yang akan output penyakitnya
    cp1, cp2, cp3, cp4= 0, 0, 0, 0
    temp=[] # Akurasi akan disimpan di array
    for x in g:
        if x in p1:
            cp1+=1
        if x in p2:
            cp2+=1
        if x in p3:
            cp3+=1
        if x in p4:
            cp4+=1

    # menghitung akurasi jumlah pilihan / jumlah isi rule * 100%
    accP1=((cp1/len(p1))*100/100)*100
    accP2=((cp2/len(p2))*100/100)*100
    accP3=((cp3/len(p3))*100/100)*100
    accP4=((cp4/len(p4))*100/100)*100
    
    temp.append(accP1)
    temp.append(accP2)
    temp.append(accP3)
    temp.append(accP4)

    i = [x for x in temp if x <= 100]
    acc=max(i) # akurasi tertinggi
    
    # akurasi yang kurang dari 45 akan termasuk P005 yang artinya penyakit tidak ditemukan
    if acc >= 45:
        if temp.index(acc)==0:
            msg="P001"
        elif temp.index(acc)==1:
            msg="P002"
        elif temp.index(acc)==2:
            msg="P003"
        elif temp.index(acc)==3:
            msg="P004"
    else:
        msg = 'P005'
    
    result= {}
    result["akurasi"] = acc
    result["penyakit"] = msg

    # return result

    # Menyimpan ke database
    if len(g) > 2:
        pasien = [
                id_pasien,
                result['penyakit'],
                request.form['nama'],
                str(request.form['umur']),
                request.form['alamat'],
                str(result['akurasi']),
                date_now
            ]

        PasienModel.store(pasien)
        for row in range(len(g)):
            gejala_terpilih = [
                id_pasien,
                g[row]
            ]
            PasienModel.store_detail(gejala_terpilih)
        # end for
        
        detail = PasienModel.get_detail(id_pasien)
        result = PenyakitModel.show(msg)
        
        return render_template('/konsultasi/hasil.html', data=result, bio=pasien, gejala=detail, acc=acc)
    else:            
        errors = True
        data = GejalaModel.get_data()
        return render_template('/konsultasi/index.html', data=data, errors=errors)
    # return render_template('/hasil.html')

@app.route('/konsultasi/hasil', methods=['POST'])
def testing_hasil():
    if request.method == 'POST':
        gejala = request.form.getlist('kode_gejala')
        # count = len(gejala)
        result = akurasi(gejala)
        # aks = result[0]
        # penyakit = result[1]

    return result

@app.route('/testing', methods=['POST'])
def konsultasi_hasil():
    msg = ''
    errors = False
    id_pasien = random_string()
    if request.method == 'POST':
        gejala = request.form.getlist('kode_gejala')
        count = len(gejala)
            
        # while count is True:
        if count > 1:
            if count < 5 and count < 10 and count < 14 and count < 7:             
                msg = 'P005'
            else:
                if count <= 5:
                    if gejala[0] == 'G001' and gejala[1] == 'G002' and gejala[2] == 'G003' and gejala[3] == 'G012' and gejala[4] == 'G019':                        
                        msg = 'P001'
                    else:
                        msg = 'P005'
                elif count == 13:
                    if gejala[0] == 'G001' and gejala[1] == 'G002' and gejala[2] == 'G003' and gejala[3] == 'G004' and gejala[4] == 'G005' and gejala[5] == 'G006' and gejala[6] == 'G007' and gejala[7] == 'G008' and gejala[8] == 'G009' and gejala[9] == 'G010' and gejala[10] == 'G011' and gejala[11] == 'G012' and gejala[12] == 'G013':
                        msg = 'P002'
                    else:
                        msg = 'P005'
                elif count == 12:
                    if gejala[0] == 'G001' and gejala[1] == 'G002' and gejala[2] == 'G003' and gejala[3] == 'G004' and gejala[4] == 'G006' and gejala[5] == 'G007' and gejala[6] == 'G008' and gejala[7] == 'G009' and gejala[8] == 'G010' and gejala[9] == 'G0011' and gejala[10] == 'G012' and gejala[11] == 'G013':
                        msg = 'P003'
                    else:
                        msg = 'P005'
                elif count == 11:
                    if gejala[0] == 'G001' and gejala[1] == 'G002' and gejala[2] == 'G003' and gejala[3] == 'G004' and gejala[4] == 'G006' and gejala[5] == 'G007' and gejala[6] == 'G014' and gejala[7] == 'G015' and gejala[8] == 'G016' and gejala[9] == 'G017' and gejala[10] == 'G018':
                        msg = 'P004'
                    else:
                        msg = 'P005'
                else:
                    msg = 'P005'
                #  end if
            # end if

            pasien = [
                id_pasien,
                msg,
                request.form['nama'],
                str(request.form['umur']),
                request.form['alamat'],
                date_now
            ]

            PasienModel.store(pasien)
            for row in range(count):
                gejala_terpilih = [
                    id_pasien,
                    gejala[row]
                ]
                PasienModel.store_detail(gejala_terpilih)
            # end for
            
            detail = PasienModel.get_detail(id_pasien)
            result = PenyakitModel.show(msg)
            
            return render_template('/konsultasi/hasil.html', data=result, bio=pasien, gejala=detail)
        else:            
            errors = True
            limit_asc = GejalaModel.get_limit_asc()
            limit_desc = GejalaModel.get_limit_desc()
            return render_template('/konsultasi/index.html', asc=limit_asc, desc=limit_desc, errors=errors)
        # return msg
        # endif
    # end if

@app.route('/tests', methods=['POST'])
def tests():
    msg = ''
    if request.method == 'POST':
        gejala = request.form.getlist('kode_gejala')
        count = len(gejala)
        if gejala[0] == 'G001' and gejala[1] == 'G002' and gejala[2] == 'G003' and gejala[3] == 'G012' and gejala[4] == 'G019':
            msg = 'P001'
        elif gejala[0] == 'G001' and gejala[1] == 'G002' and gejala[2] == 'G003' and gejala[3] == 'G004' and gejala[4] == 'G005' and gejala[5] == 'G006' and gejala[6] == 'G007' and gejala[7] == 'G008' and gejala[8] == 'G009' and gejala[9] == 'G010' and gejala[10] == 'G011' and gejala[11] == 'G012' and gejala[12] == 'G013':
            msg = 'P002'
        elif gejala[0] == 'G001' and gejala[1] == 'G002' and gejala[2] == 'G003' and gejala[3] == 'G004' and gejala[4] == 'G006' and gejala[5] == 'G007' and gejala[6] == 'G008' and gejala[7] == 'G009' and gejala[8] == 'G010' and gejala[9] == 'G0011' and gejala[10] == 'G012' and gejala[11] == 'G013':
            msg = 'P003'
        elif gejala[0] == 'G001' and gejala[1] == 'G002' and gejala[2] == 'G003' and gejala[3] == 'G004' and gejala[4] == 'G006' and gejala[5] == 'G007' and gejala[6] == 'G014' and gejala[7] == 'G015' and gejala[8] == 'G016' and gejala[9] == 'G017' and gejala[10] == 'G018':
            msg = 'P004'
        else:
            msg = 'P005'
        #  end if
    # end if
    return render_template('test2.html', gejala=gejala, count=count)

def random_string(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@app.route('/laporan')
def laporan():
    result = PasienModel.get_data()

    return render_template('/laporan/index.html', data=result)

@app.route('/laporan/detail/<id>')
def detail_laporan(id):
    result = PasienModel.show(id)
    detail = PasienModel.get_detail(id)
    # penyakit = PasienModel.get_penyakit(id)
    
    return render_template('/laporan/laporan_user.html', data=result, gejala=detail)


@app.route('/laporan/cekobat/<id>')
def cek_pengobatan(id):
    obat = SolusiModel.get_solusi(id)

    return render_template('/laporan/solusi.html', data=obat)

@app.route('/rules')
def rules():
    result = BasisModel.get_rules()
    penyakit = PenyakitModel.get_data()

    return render_template('/rules/index.html', data=result, penyakit=penyakit)

@app.route('/test')
def test():
    select = PenyakitModel.get_data()
    return render_template('/app.html', penyakit=select)
    # return render_template('/app.html', penyakit=select_option('penyakit'))

if __name__ == "__main__":
    app.run(debug=True)