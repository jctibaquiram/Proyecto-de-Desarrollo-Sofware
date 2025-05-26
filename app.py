import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
car_data = pd.read_csv("vehicles_us.csv")

st.subheader("¿Cómo es la distribución de los datos respecto al valor de odómetro?")

hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

st.title("Análisis de autos")

build_histogram = st.checkbox('Construir un histograma (odómetro)')

build_scatter = st.checkbox('Construir un diagrama de dispersión (odómetro vs precio)')

if build_histogram:
    st.write('Histograma del odómetro:')
    fig, px = plt.subplots()
    px.hist(car_data["odometer"], bins=10, color='skyblue', edgecolor='black')                  
    px.set_xlabel('Odómetro')
    px.set_ylabel('Frecuencia')
    st.pyplot(fig)

if build_scatter:
    st.write('Diagrama de dispersión: odómetro vs precio')
    fig, px = plt.subplots()
    px.scatter(car_data["odometer"], car_data["price"], color='green')
    px.set_xlabel('Odómetro')
    px.set_ylabel('Precio')
    st.pyplot(fig)