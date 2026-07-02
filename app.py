from flask import Flask, render_template, request
from knowledge_base import KONDISI
from inference_engine import hitung_certainty_factor
from distance_classifier import klasifikasi_minimum_distance

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = None
    hasil_distance = None
    input_kosong = False
    
    if request.method == 'POST':
        # --- ALUR LOGIKA CERTAINTY FACTOR ---
        user_responses = {}
        total_skor = 0
        
        for kode in KONDISI.keys():
            val = float(request.form.get(kode, 0))
            total_skor += val
            if val > 0:
                user_responses[kode] = val
                
        if total_skor > 0:
            hasil = hitung_certainty_factor(user_responses)
            
        # --- ALUR LOGIKA MINIMUM DISTANCE CLASSIFIER (DENGAN VALIDASI) ---
        bmi_inp = request.form.get('bmi_value')
        gula_inp = request.form.get('gula_value')
        aktivitas_inp = request.form.get('aktivitas_value')
        
        if bmi_inp and gula_inp and aktivitas_inp:
            try:
                # Mengonversi string ke float/int secara aman
                user_numerik = {
                    'bmi': float(bmi_inp),
                    'gula': float(gula_inp),
                    'aktivitas': float(aktivitas_inp)
                }
                hasil_distance = klasifikasi_minimum_distance(user_numerik)
            except ValueError:
                # Menangani error jika user memasukkan karakter ilegal/bukan angka
                hasil_distance = None
            
        # Handle jika seluruh form kosong total
        if total_skor == 0 and not (hasil_distance):
            input_kosong = True
            hasil = []
            
    return render_template(
        'index.html', 
        kondisi=KONDISI, 
        hasil=hasil, 
        hasil_distance=hasil_distance, 
        input_kosong=input_kosong
    )

if __name__ == '__main__':
    app.run(debug=True)