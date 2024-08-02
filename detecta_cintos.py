from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image
import os

# Carregar o modelo salvo
model = load_model('cinto_seguranca_model.h5')

def prepare_image(img_path, target_size=(150, 150)):
    # Carregar a imagem
    img = image.load_img(img_path, target_size=target_size)
    # Converter a imagem para um array
    img_array = image.img_to_array(img)
    # Expandir a dimensão da imagem para (1, 150, 150, 3)
    img_array = np.expand_dims(img_array, axis=0)
    # Escalar a imagem (opcional se você usou rescale=1./255 no treinamento)
    img_array /= 255.0
    return img_array

def predict_image(model, img_path):
    img_array = prepare_image(img_path)
    # A previsão retorna um valor entre 0 e 1
    prediction = model.predict(img_array)
    
    confidence = prediction[0][0] * 100
    
    if confidence > 20:
        return 'Sem cinto', confidence
    else:
        return 'Com cinto', 100 - confidence
    

img_path = '.\img_to_predict'

for filename in os.listdir(img_path):
    f = os.path.join(img_path, filename)

    if os.path.isfile(f):
        result, confidence  = predict_image(model, f)
        print(f'Imagem {f}: {result} (Confiança: {confidence:.2f}%)')