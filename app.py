from flask import Flask, render_template, request
from knowledge_base import KONDISI
from inference_engine import hitung_certainty_factor

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = None
    input_kosong = False
    
    if request.method == 'POST':
        user_responses = {}
        total_skor = 0
        
        for kode in KONDISI.keys():
            val = float(request.form.get(kode, 0))
            total_skor += val
            if val > 0:
                user_responses[kode] = val
        
        # Handle input kosong/semua nol
        if total_skor == 0:
            input_kosong = True
            hasil = []
        else:
            hasil = hitung_certainty_factor(user_responses)
        
    return render_template('index.html', kondisi=KONDISI, hasil=hasil, input_kosong=input_kosong)

if __name__ == '__main__':
    app.run(debug=True)