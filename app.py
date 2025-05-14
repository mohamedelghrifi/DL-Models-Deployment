import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

model = tf.keras.models.load_model('model_cifar10.h5')
class_names = ['avion','auto','oiseau','chat','cerf','chien','grenouille','cheval','bateau','camion']

st.title("Démo de classification d'images - CIFAR-10")

uploaded_file = st.file_uploader("Choisissez une image...", type=["jpg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).resize((32, 32))
    st.image(image, caption='Image chargée', use_column_width=True)
    img_array = np.expand_dims(np.array(image) / 255.0, axis=0)
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]
    st.write(f"**Classe prédite :** {predicted_class}")