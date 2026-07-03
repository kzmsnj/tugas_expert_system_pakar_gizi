KONDISI = {
    'K01': 'Mengalami Obesitas (BMI >= 25)',
    'K02': 'Mengalami Underweight (BMI < 18.5)',
    'K07': 'Memiliki Berat Badan Normal (18.5 <= BMI < 25)', 
    'K03': 'Memiliki Riwayat Penyakit Maag / Asam Lambung',
    'K04': 'Memiliki Riwayat Diabetes (Gula Darah Tinggi)',
    'K05': 'Aktivitas Fisik Sangat Rendah (Sedentary / Jarang Gerak)',
    'K06': 'Aktivitas Fisik Tinggi (Sering Olahraga / Pekerja Berat)'
}

REKOMENDASI_GIZI = {
    'D01': {
        'nama': 'Manajemen Berat Badan & Defisit Kalori Bertahap',
        'deskripsi': 'Fokus pada optimalisasi metabolisme dengan mengurangi asupan kalori berlebih tanpa mengorbankan mikronutrisi harian. Cocok untuk menormalkan BMI dan menekan risiko penyakit metabolik.',
        'menu': 'Sarapan: Telur rebus & buah potong. Makan Siang: Nasi secukupnya, dada ayam panggang & sayur bayam rebus. Makan Malam: Ikan bakar & tumis buncis.',
        'gaya_hidup': 'Tingkatkan langkah harian perlahan hingga 7.000-10.000 langkah/hari (NEAT). Biasakan minum 1 gelas air putih sebelum makan untuk membantu kontrol porsi.'
    },
    'D02': {
        'nama': 'Peningkatan Massa Tubuh & Gizi Padat (Nutrient Dense)',
        'deskripsi': 'Fokus pada pemenuhan energi dan makronutrien untuk mendukung aktivitas tinggi dan mencapai berat badan ideal secara sehat, mencegah malnutrisi dan kelelahan kronis.',
        'menu': 'Sarapan: Oatmeal dengan selai kacang & pisang. Makan Siang: Daging sapi/ayam porsi ekstra, nasi, & tempe. Makan Malam: Telur, alpukat, & karbohidrat kompleks.',
        'gaya_hidup': 'Lakukan latihan beban ringan (resistance training) 2-3x seminggu agar surplus kalori diubah menjadi massa otot, bukan lemak. Pastikan tidur minimal 7-8 jam/hari.'
    },
    'D03': {
        'nama': 'Protokol Gastrointestinal (Ramah Lambung)',
        'deskripsi': 'Penyesuaian ritme makan dan pemilihan bahan makanan non-iritan untuk menjaga pH lambung tetap stabil serta mendukung perbaikan mukosa dinding lambung.',
        'menu': 'Sarapan: Bubur ayam / oatmeal halus. Makan Siang: Nasi lembek, sup ayam bening, tahu tim. Makan Malam: Kentang tumbuk & ikan kukus.',
        'gaya_hidup': 'Terapkan pola makan porsi kecil tapi sering (4-5x sehari). Hindari rebahan atau tidur minimal 2 jam setelah makan. Kurangi drastis kopi, pedas, dan makanan asam.'
    },
    'D04': {
        'nama': 'Manajemen Glikemik & Kontrol Gula',
        'deskripsi': 'Strategi gizi untuk mengontrol lonjakan insulin dan gula darah, sangat krusial bagi yang sering mengonsumsi manis berlebih atau memiliki riwayat resistensi insulin.',
        'menu': 'Sarapan: Roti gandum utuh & putih telur. Makan Siang: Nasi merah (porsi terkontrol), pepes ikan, & sayur berserat tinggi. Makan Malam: Brokoli kukus & dada ayam panggang.',
        'gaya_hidup': 'Pangkas konsumsi gula cair (minuman manis kemasan/kopi kekinian). Biasakan berjalan kaki 10-15 menit setiap selesai makan besar untuk membantu otot menyerap glukosa.'
    },
    'D05': {
        'nama': 'Pemeliharaan Kebugaran & Gizi Seimbang',
        'deskripsi': 'Berat badan Anda sudah ideal, namun kurangnya aktivitas fisik dapat menurunkan metabolisme. Fokus pada komposisi gizi seimbang harian.',
        'menu': 'Sarapan: Roti gandum & telur rebus. Makan Siang: Nasi porsi sedang, ayam bakar, sup sayur. Makan Malam: Buah-buahan & susu rendah lemak.',
        'gaya_hidup': 'Mulai rutinitas peregangan (stretching) 10 menit setiap pagi dan usahakan berjalan setidaknya 5.000 langkah per hari untuk melancarkan sirkulasi darah.'
    },
    'D06': {
        'nama': 'Optimalisasi Performa (Atletis & Aktif)',
        'deskripsi': 'Dengan berat badan ideal dan aktivitas fisik tinggi, fokus utama Anda adalah menjaga asupan cairan dan glikogen otot untuk pemulihan (recovery).',
        'menu': 'Sarapan: Pisang, susu, & oat. Makan Siang: Pasta/Nasi, daging tanpa lemak, sayur. Makan Malam: Ikan laut & ubi jalar.',
        'gaya_hidup': 'Pertahankan rutinitas olahraga Anda. Pastikan pemanasan yang cukup dan penuhi asupan protein harian untuk memperbaiki jaringan otot.'
    }
}

RULES = [
    {'id': 'R1', 'kondisi': ['K01', 'K05'], 'kesimpulan': 'D01', 'mb': 0.8},
    {'id': 'R2', 'kondisi': ['K02', 'K06'], 'kesimpulan': 'D02', 'mb': 0.9},
    {'id': 'R3', 'kondisi': ['K03'], 'kesimpulan': 'D03', 'mb': 0.85},
    {'id': 'R4', 'kondisi': ['K04'], 'kesimpulan': 'D04', 'mb': 0.9},
    {'id': 'R5', 'kondisi': ['K07', 'K05'], 'kesimpulan': 'D05', 'mb': 0.8}, 
    {'id': 'R6', 'kondisi': ['K07', 'K06'], 'kesimpulan': 'D06', 'mb': 0.9}  
]