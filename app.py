from flask import Flask, render_template, request
from knowledge_base import KONDISI
from inference_engine import hitung_certainty_factor
from distance_classifier import klasifikasi_minimum_distance

app = Flask(__name__)


def gabungkan_hasil(hasil_cf, hasil_distance):
    """Menggabungkan hasil Certainty Factor & Minimum Distance jadi satu daftar rekomendasi,
    supaya user cukup lihat satu hasil akhir per diet (bukan dua panel terpisah)."""
    gabungan = {}

    for item in hasil_cf or []:
        gabungan[item['kode']] = {
            'kode': item['kode'],
            'nama': item['nama'],
            'deskripsi': item['deskripsi'],
            'menu': item['menu'],
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

    return sorted(hasil_akhir, key=lambda x: x['skor_gabungan'], reverse=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    rekomendasi = None
    input_kosong = False

    if request.method == 'POST':
        # data dari langkah "ceritakan kondisi kesehatanmu"
        user_responses = {}
        total_skor = 0

        for kode in KONDISI.keys():
            val = float(request.form.get(kode, 0))
            total_skor += val
            if val > 0:
                user_responses[kode] = val

        hasil_cf = hitung_certainty_factor(user_responses) if total_skor > 0 else []

        # data dari kalkulator BMI + data tambahan
        bmi_inp = request.form.get('bmi_value')
        gula_inp = request.form.get('gula_value')
        aktivitas_inp = request.form.get('aktivitas_value')

        hasil_distance = None
        if bmi_inp and gula_inp and aktivitas_inp:
            try:
                user_numerik = {
                    'bmi': float(bmi_inp),
                    'gula': float(gula_inp),
                    'aktivitas': float(aktivitas_inp)
                }
                hasil_distance = klasifikasi_minimum_distance(user_numerik)
            except ValueError:
                hasil_distance = None

        if total_skor == 0 and not hasil_distance:
            input_kosong = True
        else:
            rekomendasi = gabungkan_hasil(hasil_cf, hasil_distance)

    return render_template(
        'index.html',
        kondisi=KONDISI,
        rekomendasi=rekomendasi,
        input_kosong=input_kosong
    )


if __name__ == '__main__':
    app.run(debug=True)