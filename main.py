from flask import Flask, render_template, request
import cv2
from keras.models import load_model
import numpy as np
import base64

app = Flask(__name__, static_url_path='/src', static_folder='src')

model = load_model('modelo.h5')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', message='No file part')
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', message='No selected file')
        if file:
            img_bytes = file.read()
            nparr = np.fromstring(img_bytes, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (64, 64))
            img = np.array(img).reshape(-1, 64, 64, 1)
            prediction = model.predict(img)
            classes = ['usb hembra', 'usb macho', 'hdmi hembra', 'hdmi macho', 'enchufe tipo a hembra', 'enchufe tipo a macho', 'enchufe tipo c macho', 'enchufe tipo c hembra', 'vga macho', 'vga hembra', 'ethernet hembra', 'ethernet macho']
            prediction_class = classes[np.argmax(prediction)]
            return render_template('result.html', predicted_class=prediction_class)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
