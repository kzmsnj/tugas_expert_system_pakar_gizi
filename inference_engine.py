from knowledge_base import RULES, DIET_PLANS

def hitung_certainty_factor(user_responses):
    hasil_diet = {}

    for rule in RULES:
        kondisi_rule = rule['kondisi']
        kesimpulan = rule['kesimpulan']
        mb_pakar = rule['mb']
        
        # Cek rule terpicu (Kaidah AND)
        if all(k in user_responses and user_responses[k] > 0 for k in kondisi_rule):
            cf_user_min = min(user_responses[k] for k in kondisi_rule)
            cf_rule = cf_user_min * mb_pakar
            
            # Kombinasi CF jika ada lebih dari 1 rule mengarah ke kesimpulan yang sama
            if kesimpulan in hasil_diet:
                cf_lama = hasil_diet[kesimpulan]
                cf_baru = cf_lama + cf_rule * (1 - cf_lama)
                hasil_diet[kesimpulan] = cf_baru
            else:
                hasil_diet[kesimpulan] = cf_rule

    rekomendasi_akhir = []
    
    # Mapping output
    for kode, cf_nilai in hasil_diet.items():
        if cf_nilai > 0:
            rekomendasi_akhir.append({
                'nama': DIET_PLANS[kode]['nama'],
                'deskripsi': DIET_PLANS[kode]['deskripsi'],
                'menu': DIET_PLANS[kode]['menu'],
                'keyakinan': round(cf_nilai * 100, 2)
            })
            
    # Sort descending berdasar persentase keyakinan
    return sorted(rekomendasi_akhir, key=lambda x: x['keyakinan'], reverse=True)