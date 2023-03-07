import streamlit as st
import cv2
import numpy as np
import time
import imutils
from tensorflow import keras
from tensorflow.keras.optimizers import RMSprop
from functions import *

#PageConfig
page_config = importar_config()

st.markdown("<h1 style='text-align: center; color: black;'>Predicción de Tumores Cerebrales</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;'>Proyecto Deep Learning</h2>", unsafe_allow_html=True)

image = 'img/cerebro.png'
image_2 = 'img/MRI.gif'

col1, col2, col3 = st.columns([11,5,11])

with col1:
    st.write("")

with col2:
    st.image(image, use_column_width='auto')

with col3:
    st.write("")


# Función para procesar la imagen y realizar la predicción
def process_image(image):
    # Redimensiona la imagen a las dimensiones de entrada del modelo
    image = cv2.resize(image, (224, 224))
    # Convierte la imagen a escala de grises
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Normaliza los valores de los píxeles
    image = image / 255.0
    # Añade una dimensión adicional para la dimensión del batch
    image = np.expand_dims(image, axis=0)
    # Realiza la predicción
    prediction = keras_model.predict(image)
    # Devuelve la clase con la mayor probabilidad
    return np.argmax(prediction)

# Carga la imagen con Streamlit y muestra la predicción
uploaded_file = st.file_uploader("Cargar imagen", type=["jpg", "jpeg", "png"])
if not uploaded_file:
    st.warning("Por favor, carga una imagen para continuar.")
else:
    try:
        # Lee la imagen cargada y la convierte a un array NumPy
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)

        # Carga el modelo previamente entrenado
        with st.spinner('Cargando modelo...'):
            time.sleep(1)
            keras_model = keras.models.load_model('model/Brain_model.h5')

            keras_model.compile(optimizer=RMSprop(learning_rate=1e-4),
                            loss='sparse_categorical_crossentropy',
                            metrics=['acc'])

        # Agrega un botón para realizar la predicción, solo este visible cuando se cargue la imagen 
        button_clicked = st.button("Realizar predicción")
        if button_clicked:
            # Crea un placeholder para la imagen gif
            placeholder = st.empty()
            # Muestra el spinner antes de la predicción
            with st.spinner('Realizando predicción...'):
                # Muestra la imagen gif en el placeholder
                gif_ref = placeholder.image(image_2)
                 # Espera 5 segundos para simular el procesamiento
                time.sleep(5)
                # Elimina la imagen gif del placeholder
                del gif_ref
                 # Espera 5 segundos para simular el procesamiento
                time.sleep(1)
                # Optimiza la imagen para acelerar la predicción
                processed_image = imutils.resize(image, width=400)
                # Realiza la predicción y muestra el resultado en la interfaz
                prediction = process_image(processed_image)
                # Elimina el placeholder
                placeholder.empty()
                # Muestra la imagen en la interfaz
                st.image(image, channels="BGR", caption="Imagen cargada")
                # Realiza la predicción y muestra el resultado en la interfaz
                prediction = process_image(image)
                if prediction == 0:
                    st.write("La imagen corresponde a un cerebro con tumor tipo glioma")
                elif prediction == 1:  
                    st.write("La imagen corresponde a un cerebro con tumor tipo menignoma")

    except:
        st.error("Ocurrió un error al leer la imagen cargada. Por favor, asegúrate de que el archivo que estás cargando es una imagen.")
#CCS
css = importar_css()
