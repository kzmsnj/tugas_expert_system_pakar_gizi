import math
from knowledge_base import REKOMENDASI_GIZI

CENTROIDS = {
    'D01': {'bmi': 28.0, 'konsumsi_manis': 8.0, 'aktivitas': 1.0},
    'D02': {'bmi': 17.0, 'konsumsi_manis': 4.0, 'aktivitas': 5.0},
    'D03': {'bmi': 22.0, 'konsumsi_manis': 3.0, 'aktivitas': 3.0},
    'D04': {'bmi': 23.0, 'konsumsi_manis': 12.0, 'aktivitas': 3.0},
    'D05': {'bmi': 21.5, 'konsumsi_manis': 5.0, 'aktivitas': 1.5}, 
    'D06': {'bmi': 22.0, 'konsumsi_manis': 4.0, 'aktivitas': 4.5}  
}

def hitung_jarak(user, centroid):
    selisih_bmi = user['bmi'] - centroid['bmi']
    selisih_manis = user['konsumsi_manis'] - centroid['konsumsi_manis']
    selisih_aktivitas = user['aktivitas'] - centroid['aktivitas']

    return math.sqrt((selisih_bmi ** 2) + (selisih_manis ** 2) + (selisih_aktivitas ** 2))

def klasifikasi_minimum_distance(user_numerik):
    hasil_jarak = []
    for kode, centroid in CENTROIDS.items():
        jarak = hitung_jarak(user_numerik, centroid)
        hasil_jarak.append({
            'kode': kode,
            'nama': REKOMENDASI_GIZI[kode]['nama'],
            'deskripsi': REKOMENDASI_GIZI[kode]['deskripsi'],
            'menu': REKOMENDASI_GIZI[kode]['menu'],
            'gaya_hidup': REKOMENDASI_GIZI[kode]['gaya_hidup'],
            'jarak': round(jarak, 2)
        })
    return sorted(hasil_jarak, key=lambda x: x['jarak'])