import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv(
    'vehicles_us.csv')  # leer los datos

st.header('proyecto_car_data')

hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

hist_button_2 = st.checkbox(
    'Construir diagrama de dispersión')  # crear un botón

if hist_button_2:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig_2 = px.scatter(car_data, x='price', y='odometer')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_2, use_container_width=True)
