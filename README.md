# NutriMBG — Aplikasi Rekomendasi Gizi Berbasis Certainty Factor

Aplikasi web sederhana berbasis Flask yang memberikan rekomendasi program diet/gizi menggunakan metode **Sistem Pakar (Expert System)** dengan algoritma **Certainty Factor (CF)**. Pengguna mengisi form kondisi fisik/kesehatan, lalu sistem melakukan forward chaining terhadap basis pengetahuan (rule base) dan menghitung tingkat keyakinan dari setiap kemungkinan rekomendasi diet.

## Fitur

- Form input kondisi fisik dengan skala keyakinan (Tidak Tahu, Mungkin Iya, Yakin, Sangat Yakin)
- Perhitungan Certainty Factor (CF) dari kombinasi gejala/kondisi yang dipilih
- Kombinasi CF otomatis jika lebih dari satu rule mengarah ke kesimpulan yang sama
- Output rekomendasi diet diurutkan berdasarkan persentase keyakinan tertinggi
- Tampilan responsif menggunakan Tailwind CSS

## Struktur Proyek

```
.
├── app.py                  # Entry point Flask, menangani routing & request form
├── inference_engine.py     # Logika mesin inferensi (perhitungan Certainty Factor)
├── knowledge_base.py       # Basis pengetahuan: kondisi, rule, dan rencana diet
├── requirements.txt        # Daftar dependensi Python
├── templates/
│   └── index.html          # Tampilan form input & hasil rekomendasi
└── README.md
```

> **Catatan:** Flask secara default mencari file HTML di dalam folder `templates/`. Pastikan `index.html` berada di dalam folder tersebut agar `render_template('index.html', ...)` dapat menemukannya.

## Basis Pengetahuan

### Kondisi (Gejala Input)

| Kode | Deskripsi |
|------|-----------|
| K01  | Mengalami Obesitas (BMI > 25) |
| K02  | Mengalami Underweight (BMI < 18.5) |
| K03  | Memiliki Riwayat Penyakit Maag / Asam Lambung |
| K04  | Memiliki Riwayat Diabetes (Gula Darah Tinggi) |
| K05  | Aktivitas Fisik Sangat Rendah (Sedentary) |
| K06  | Aktivitas Fisik Tinggi (Sering Olahraga) |

### Rekomendasi Diet

| Kode | Nama Diet |
|------|-----------|
| D01  | Diet Defisit Kalori & Rendah Karbohidrat |
| D02  | Diet Surplus Kalori & Tinggi Protein (Bulking) |
| D03  | Diet Ramah Lambung (Porsi Kecil Sering) |
| D04  | Diet Rendah Glikemik (Khusus Diabetes) |

### Rule Base

| ID | Kondisi (AND) | Kesimpulan | MB Pakar |
|----|----------------|------------|----------|
| R1 | K01 & K05 | D01 | 0.8 |
| R2 | K02 & K06 | D02 | 0.9 |
| R3 | K03 | D03 | 0.85 |
| R4 | K04 | D04 | 0.9 |

## Cara Kerja Algoritma

1. Setiap kondisi yang dipilih pengguna memiliki nilai keyakinan (CF user): `0`, `0.4`, `0.7`, atau `1.0`.
2. Untuk setiap rule, sistem mengecek apakah **semua** kondisi pada rule tersebut terpenuhi (bernilai > 0).
3. Jika terpenuhi, dihitung `CF_rule = min(CF_user semua kondisi) × MB_pakar`.
4. Jika satu kesimpulan diperoleh dari lebih dari satu rule, CF digabung dengan rumus kombinasi CF:
   `CF_kombinasi = CF_lama + CF_baru × (1 − CF_lama)`
5. Hasil akhir ditampilkan sebagai persentase keyakinan (`CF × 100%`), diurutkan dari yang tertinggi.

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
- **Metode:** Sistem Pakar — Forward Chaining + Certainty Factor

## Pengembangan Lebih Lanjut

Beberapa ide pengembangan yang bisa ditambahkan:
- Menyimpan riwayat hasil konsultasi pengguna ke database
- Menambah jumlah kondisi dan rule pada basis pengetahuan
- Menambahkan autentikasi pengguna
- Validasi input di sisi backend (saat ini nilai form diasumsikan valid)

## Lisensi

Proyek ini dibuat untuk keperluan pembelajaran/akademik. Silakan gunakan dan modifikasi sesuai kebutuhan.