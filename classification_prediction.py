# # -*- coding: utf-8 -*-
#
# from keras.models import load_model
# import cv2
# import numpy as np
#
# model = load_model('modelo.h5')
#
# image_path = input("Por favor, ingrese la ruta de la imagen: ")
#
# image_path = image_path.strip('"')
#
# img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#
# img = cv2.resize(img, (64, 64))
# img = np.array(img).reshape(-1, 64, 64, 1)
#
# #HACER LA PREDICCION
# print(img)
# prediction = model.predict(img)
#
# #OBTENER LA CLASE PREDICHA
# classes = ['usb_female', 'usb_male', 'hdmi_female', 'hdmi_male', 'plug_type_a_female', 'plug_type_a_male', 'plug_type_c_male', 'plug_type_c_female', 'vga_male', 'vga_female', 'ethernet_female', 'ethernet_male']
# prediction_class = classes[np.argmax(prediction)]
#
# print(f'la clase predicha es:{prediction_class}')


# from flask import Flask, request, jsonify
#
# from keras.models import load_model
# import cv2
# import numpy as np
#
# app = Flask(__name__)
#
# model = load_model('modelo.h5')
#
# @app.route('/predict', methods=['POST'])
# def predict():
#     # Obtener la ruta de la imagen del cuerpo de la solicitud POST
#     image_data = request.json['image_data']
#
#     # Convertir los datos de la imagen de base64 a una matriz de numpy
#     img_bytes = image_data.split(',')[1]
#     nparr = np.frombuffer(img_bytes.decode('base64'), np.uint8)
#     img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
#
#     img = cv2.resize(img, (64, 64))
#     img = np.array(img).reshape(-1, 64, 64, 1)
#
#     # Hacer la predicción
#     prediction = model.predict(img)
#
#     # Obtener la clase predicha
#     classes = ['usb_female', 'usb_male', 'hdmi_female', 'hdmi_male', 'plug_type_a_female', 'plug_type_a_male',
#                'plug_type_c_male', 'plug_type_c_female', 'vga_male', 'vga_female', 'ethernet_female', 'ethernet_male']
#     prediction_class = classes[np.argmax(prediction)]
#
#     # Devolver la clase predicha como respuesta
#     return jsonify({'result': prediction_class})
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
