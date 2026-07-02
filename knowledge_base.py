# Data Gejala / Kondisi Input
KONDISI = {
    'K01': 'Mengalami Obesitas (BMI > 25)',
    'K02': 'Mengalami Underweight (BMI < 18.5)',
    'K03': 'Memiliki Riwayat Penyakit Maag / Asam Lambung',
    'K04': 'Memiliki Riwayat Diabetes (Gula Darah Tinggi)',
    'K05': 'Aktivitas Fisik Sangat Rendah (Sedentary / Jarang Gerak)',
    'K06': 'Aktivitas Fisik Tinggi (Sering Olahraga / Pekerja Berat)'
}

# Data Kesimpulan / Rekomendasi
DIET_PLANS = {
    'D01': {
        'nama': 'Diet Defisit Kalori & Rendah Karbohidrat',
        'deskripsi': 'Fokus pada penurunan berat badan dengan membatasi porsi karbohidrat dan mengurangi kalori harian secara aman.',
        'menu': 'Sarapan: Telur rebus & alpukat. Makan Siang: Dada ayam panggang & sayur bayam. Makan Malam: Ikan bakar & tumis buncis.'
    },
    'D02': {
        'nama': 'Diet Surplus Kalori & Tinggi Protein (Bulking)',
        'deskripsi': 'Fokus pada peningkatan berat badan dan massa otot dengan menambah asupan kalori sehat dan protein.',
        'menu': 'Sarapan: Oatmeal dengan pisang & susu. Makan Siang: Daging sapi, nasi merah, & tempe. Makan Malam: Dada ayam & telur.'
    },
    'D03': {
        'nama': 'Diet Ramah Lambung (Porsi Kecil Sering)',
        'deskripsi': 'Fokus pada menjaga asam lambung tetap stabil dengan menghindari makanan pemicu (pedas, asam) dan makan dengan porsi kecil namun sering.',
        'menu': 'Sarapan: Bubur ayam/oatmeal pisang. Makan Siang: Nasi lembek, sup ayam bening, tahu tim. Makan Malam: Kentang tumbuk (mash potato) & ikan kukus.'
    },
    'D04': {
        'nama': 'Diet Rendah Glikemik (Khusus Diabetes)',
        'deskripsi': 'Fokus pada menjaga kadar gula darah dengan mengonsumsi karbohidrat kompleks yang lambat diserap tubuh.',
        'menu': 'Sarapan: Roti gandum utuh & putih telur. Makan Siang: Nasi merah, pepes ikan, & tahu. Makan Malam: Brokoli kukus & ayam panggang.'
    }
}

# Rule Base & Nilai MB (Measure of Belief) Pakar
RULES = [
    {
        'id': 'R1',
        'kondisi': ['K01', 'K05'],
        'kesimpulan': 'D01',
        'mb': 0.8
    },
    {
        'id': 'R2',
        'kondisi': ['K02', 'K06'],
        'kesimpulan': 'D02',
        'mb': 0.9
    },
    {
        'id': 'R3',
        'kondisi': ['K03'],
        'kesimpulan': 'D03',
        'mb': 0.85
    },
    {
        'id': 'R4',
        'kondisi': ['K04'],
        'kesimpulan': 'D04',
        'mb': 0.9
    }
]