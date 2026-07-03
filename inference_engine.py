from knowledge_base import RULES, REKOMENDASI_GIZI

def hitung_certainty_factor(user_responses):
    hasil_diet = {}

    for rule in RULES:
        kondisi_rule = rule['kondisi']
        kesimpulan = rule['kesimpulan']
        mb_pakar = rule['mb']
        
        if all(k in user_responses and user_responses[k] > 0 for k in kondisi_rule):
            cf_user_min = min(user_responses[k] for k in kondisi_rule)
            cf_rule = cf_user_min * mb_pakar
            
            if kesimpulan in hasil_diet:
                cf_lama = hasil_diet[kesimpulan]
                cf_baru = cf_lama + cf_rule * (1 - cf_lama)
                hasil_diet[kesimpulan] = cf_baru
            else:
                hasil_diet[kesimpulan] = cf_rule

    rekomendasi_akhir = []
    
    for kode, cf_nilai in hasil_diet.items():
        if cf_nilai > 0:
            rekomendasi_akhir.append({
                'kode': kode,
                'nama': REKOMENDASI_GIZI[kode]['nama'],
                'deskripsi': REKOMENDASI_GIZI[kode]['deskripsi'],
                'menu': REKOMENDASI_GIZI[kode]['menu'],
                'gaya_hidup': REKOMENDASI_GIZI[kode]['gaya_hidup'], 
                'keyakinan': round(cf_nilai * 100, 2)
            })
            
    return sorted(rekomendasi_akhir, key=lambda x: x['keyakinan'], reverse=True)