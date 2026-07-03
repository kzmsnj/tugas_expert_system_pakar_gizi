from flask import Flask, render_template, request
from knowledge_base import KONDISI
from inference_engine import hitung_certainty_factor
from distance_classifier import klasifikasi_minimum_distance

app = Flask(__name__)


def gabungkan_hasil(hasil_cf, hasil_distance):
    """
    Menggabungkan hasil perhitungan Certainty Factor (skor gejala klinis) 
    dan Minimum Distance Classifier (skor kecocokan fisik) menjadi satu rekomendasi akhir.
    Masing-masing metode memiliki bobot seimbang 50%.
    """
    gabungan = {}

    for item in hasil_cf or []:
        gabungan[item['kode']] = {
            'kode': item['kode'],
            'nama': item['nama'],
            'deskripsi': item['deskripsi'],
            'menu': item['menu'],
            'gaya_hidup': item['gaya_hidup'],  
            'skor_gejala': item['keyakinan'],
            'skor_fisik': None
        }

    if hasil_distance:
        jarak_semua = [d['jarak'] for d in hasil_distance]
        jarak_min, jarak_max = min(jarak_semua), max(jarak_semua)

        for item in hasil_distance:
            if jarak_max == jarak_min:
                skor_fisik = 100.0
            else:
                skor_fisik = round((1 - (item['jarak'] - jarak_min) / (jarak_max - jarak_min)) * 100, 1)

            if item['kode'] in gabungan:
                gabungan[item['kode']]['skor_fisik'] = skor_fisik
            else:
                gabungan[item['kode']] = {
                    'kode': item['kode'],
                    'nama': item['nama'],
                    'deskripsi': item['deskripsi'],
                    'menu': item['menu'],
                    'gaya_hidup': item['gaya_hidup'],
                    'skor_gejala': 0.0,
                    'skor_fisik': skor_fisik
                }

    hasil_akhir = []
    for item in gabungan.values():
        sg, sf = item['skor_gejala'], item['skor_fisik']

        if sg is not None and sf is not None:
            item['skor_gabungan'] = round(sg * 0.5 + sf * 0.5, 1)
        else:
            item['skor_gabungan'] = sg if sg is not None else sf

        hasil_akhir.append(item)

    hasil_terurut = sorted(hasil_akhir, key=lambda x: x['skor_gabungan'], reverse=True)
    return hasil_terurut[:1]


@app.route('/', methods=['GET', 'POST'])
def index():
    rekomendasi = None
    input_kosong = False


    kondisi_manual = {k: KONDISI[k] for k in ['K03', 'K04'] if k in KONDISI}

    if request.method == 'POST':
        user_responses = {}
        total_skor = 0

        for kode in kondisi_manual.keys():
            val = float(request.form.get(kode, 0))
            total_skor += val
            if val > 0:
                user_responses[kode] = val

        bmi_inp = request.form.get('bmi_value')
        manis_inp = request.form.get('manis_value')      
        aktivitas_inp = request.form.get('aktivitas_value')

        hasil_distance = None

        if bmi_inp and manis_inp and aktivitas_inp:
            try:
                bmi_val = float(bmi_inp)
                manis_val = float(manis_inp)
                akt_val = float(aktivitas_inp)

                if bmi_val >= 25.0:
                    user_responses['K01'] = 1.0  
                    total_skor += 1
                elif bmi_val < 18.5:
                    user_responses['K02'] = 1.0  
                    total_skor += 1
                else:
                    user_responses['K07'] = 1.0  
                    total_skor += 1

                if akt_val <= 2:
                    user_responses['K05'] = 1.0  
                    total_skor += 1
                elif akt_val >= 4:
                    user_responses['K06'] = 1.0  
                    total_skor += 1

                user_numerik = {
                    'bmi': bmi_val,
                    'konsumsi_manis': manis_val,
                    'aktivitas': akt_val
                }
                hasil_distance = klasifikasi_minimum_distance(user_numerik)

            except ValueError:
                hasil_distance = None

        hasil_cf = hitung_certainty_factor(user_responses) if total_skor > 0 else []

        if total_skor == 0 and not hasil_distance:
            input_kosong = True
        else:
            rekomendasi = gabungkan_hasil(hasil_cf, hasil_distance)

    return render_template(
        'index.html',
        kondisi=kondisi_manual,
        rekomendasi=rekomendasi,
        input_kosong=input_kosong
    )


if __name__ == '__main__':
    app.run(debug=True)