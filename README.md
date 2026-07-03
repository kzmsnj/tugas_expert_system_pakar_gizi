# NutriMBG — Aplikasi Rekomendasi Gizi (Certainty Factor & Minimum Distance Classifier)

Aplikasi web berbasis Flask yang memberikan rekomendasi program diet/gizi menggunakan **dua pendekatan sekaligus**:

1. **Sistem Pakar (Expert System) — Certainty Factor (CF)**: pendekatan *rule-based* menggunakan forward chaining terhadap basis pengetahuan (rule) dan menghitung tingkat keyakinan dari gejala/kondisi kualitatif yang dipilih pengguna.
2. **Minimum Distance Classifier (Pattern Recognition)**: pendekatan klasifikasi berbasis Jarak Euclidean, mengklasifikasikan data numerik pengguna (BMI, kadar gula darah, tingkat aktivitas) terhadap titik acuan (centroid) tiap kelas diet, lalu memilih kelas dengan jarak terkecil.

Kedua hasil ditampilkan berdampingan sehingga bisa dibandingkan secara langsung.

## Fitur

- **Form 1 — Input Kualitatif (Certainty Factor):** skala keyakinan (Tidak Tahu, Mungkin Iya, Yakin, Sangat Yakin) untuk tiap kondisi fisik/kesehatan.
- **Form 2 — Input Numerik (Minimum Distance):** input BMI, kadar gula darah, dan tingkat aktivitas fisik (skala 1–5).
- Perhitungan Certainty Factor dengan kombinasi CF otomatis jika lebih dari satu rule mengarah ke kesimpulan yang sama.
- Perhitungan Jarak Euclidean ke centroid tiap kelas diet, diurutkan dari jarak terkecil.
- Validasi input (form kosong maupun input numerik tidak valid ditangani dengan aman).
- Tampilan responsif menggunakan Tailwind CSS.

## Struktur Proyek

```
.
├── app.py                  # Entry point Flask, menangani routing & kedua alur perhitungan
├── inference_engine.py     # Mesin inferensi Certainty Factor
├── distance_classifier.py  # Mesin klasifikasi Minimum Distance (Jarak Euclidean)
├── knowledge_base.py       # Basis pengetahuan: kondisi, rule, dan rencana diet
├── requirements.txt        # Daftar dependensi Python
├── templates/
│   └── index.html          # Tampilan form input & kedua hasil rekomendasi
└── README.md
```

> **Catatan:** Flask secara default mencari file HTML di dalam folder `templates/`. Pastikan `index.html` berada di dalam folder tersebut.

## Basis Pengetahuan

### Kondisi Kualitatif (Input Form 1 — Certainty Factor)

| Kode | Deskripsi |
|------|-----------|
| K01  | Mengalami Obesitas (BMI > 25) |
| K02  | Mengalami Underweight (BMI < 18.5) |
| K03  | Memiliki Riwayat Penyakit Maag / Asam Lambung |
| K04  | Memiliki Riwayat Diabetes (Gula Darah Tinggi) |
| K05  | Aktivitas Fisik Sangat Rendah (Sedentary) |
| K06  | Aktivitas Fisik Tinggi (Sering Olahraga) |

### Rule Base (Certainty Factor)

| ID | Kondisi (AND) | Kesimpulan | MB Pakar |
|----|----------------|------------|----------|
| R1 | K01 & K05 | D01 | 0.8 |
| R2 | K02 & K06 | D02 | 0.9 |
| R3 | K03 | D03 | 0.85 |
| R4 | K04 | D04 | 0.9 |

### Centroid Kelas Diet (Input Form 2 — Minimum Distance)

| Kode | BMI | Gula Darah (mg/dL) | Aktivitas (1–5) |
|------|-----|---------------------|-------------------|
| D01  | 28.0 | 90.0 | 1.0 |
| D02  | 17.0 | 90.0 | 5.0 |
| D03  | 22.0 | 90.0 | 3.0 |
| D04  | 23.0 | 180.0 | 3.0 |

### Rekomendasi Diet

| Kode | Nama Diet |
|------|-----------|
| D01  | Diet Defisit Kalori & Rendah Karbohidrat |
| D02  | Diet Surplus Kalori & Tinggi Protein (Bulking) |
| D03  | Diet Ramah Lambung (Porsi Kecil Sering) |
| D04  | Diet Rendah Glikemik (Khusus Diabetes) |

## Cara Kerja Algoritma

### 1. Certainty Factor (`inference_engine.py`)

1. Setiap kondisi yang dipilih pengguna punya nilai keyakinan (CF user): `0`, `0.4`, `0.7`, atau `1.0`.
2. Untuk setiap rule, dicek apakah **semua** kondisi pada rule tersebut terpenuhi (bernilai > 0).
3. Jika terpenuhi, dihitung `CF_rule = min(CF_user semua kondisi) × MB_pakar`.
4. Jika satu kesimpulan diperoleh dari lebih dari satu rule, CF digabung dengan rumus kombinasi:
   `CF_kombinasi = CF_lama + CF_baru × (1 − CF_lama)`
5. Hasil ditampilkan sebagai persentase keyakinan (`CF × 100%`), diurutkan dari yang tertinggi.

### 2. Minimum Distance Classifier (`distance_classifier.py`)

1. Nilai numerik pengguna (BMI, gula darah, aktivitas) dibentuk sebagai vektor.
2. Dihitung Jarak Euclidean dari vektor pengguna ke centroid tiap kelas diet:
   `jarak = √((Δbmi)² + (Δgula)² + (Δaktivitas)²)`
3. Kelas diet dengan jarak terkecil menjadi rekomendasi utama.
4. Semua kelas ditampilkan, diurutkan dari jarak terkecil ke terbesar.

## Instalasi & Menjalankan Aplikasi

1. Clone repository ini dan masuk ke direktori proyek.
2. (Opsional tapi disarankan) buat virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```
3. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```
4. Jalankan aplikasi:
   ```bash
   python app.py
   ```
5. Buka browser dan akses `http://127.0.0.1:5000`.

## Teknologi yang Digunakan

- **Backend:** Python, Flask
- **Frontend:** HTML (Jinja2 Templates), Tailwind CSS (CDN)
- **Metode:** Sistem Pakar (Forward Chaining + Certainty Factor) & Pattern Recognition (Minimum Distance Classifier)

## Pengembangan Lebih Lanjut

- Menyimpan riwayat hasil konsultasi pengguna ke database
- Menambah jumlah kondisi, rule, dan centroid pada basis pengetahuan
- Menambahkan autentikasi pengguna
- Validasi input tambahan di sisi backend (mis. rentang nilai BMI/gula darah yang wajar)

## Lisensi

Proyek ini dibuat untuk keperluan pembelajaran/akademik. Silakan gunakan dan modifikasi sesuai kebutuhan.