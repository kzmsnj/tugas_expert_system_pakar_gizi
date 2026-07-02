import math
from knowledge_base import DIET_PLANS

# 1. Definisi acuan nilai ideal (Centroid) tiap kelas diet
CENTROIDS = {
    'D01': {'bmi': 28.0, 'gula': 90.0, 'aktivitas': 1.0},
    'D02': {'bmi': 17.0, 'gula': 90.0, 'aktivitas': 5.0},
    'D03': {'bmi': 22.0, 'gula': 90.0, 'aktivitas': 3.0},
    'D04': {'bmi': 23.0, 'gula': 180.0, 'aktivitas': 3.0}
}

def hitung_jarak(user, centroid):
    """
    Menghitung Jarak Euclidean antara vektor user dan vektor centroid.
    """
    selisih_bmi = user['bmi'] - centroid['bmi']
    selisih_gula = user['gula'] - centroid['gula']
    selisih_aktivitas = user['aktivitas'] - centroid['aktivitas']
    
    # Rumus Jarak Euclidean: akar( Δx^2 + Δy^2 + Δz^2 )
    return math.sqrt((selisih_bmi ** 2) + (selisih_gula ** 2) + (selisih_aktivitas ** 2))

def klasifikasi_minimum_distance(user_numerik):
    """
    Melakukan klasifikasi dengan mencari jarak terkecil ke centroid.
    """
    hasil_jarak = []
    
    # Hitung jarak untuk setiap centroid kelas diet
    for kode, centroid in CENTROIDS.items():
        jarak = hitung_jarak(user_numerik, centroid)
        
        hasil_jarak.append({
            'kode': kode,
            'nama': DIET_PLANS[kode]['nama'],
            'deskripsi': DIET_PLANS[kode]['deskripsi'],
            'menu': DIET_PLANS[kode]['menu'],
            'jarak': round(jarak, 2)
        })
        
    # Urutkan hasil dari jarak terkecil ke terbesar
    return sorted(hasil_jarak, key=lambda x: x['jarak'])