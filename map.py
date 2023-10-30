import streamlit as st
import plotly.express as px

def tampil():
    # Buat data contoh
    data = px.data.gapminder()

    # Buat peta dengan Plotly Express
    fig = px.scatter_geo(data, locations="iso_alpha", color="continent",
                         hover_name="country", size="pop",
                         projection="natural earth")

    # Tampilkan peta dalam aplikasi Streamlit
    st.title("Visualisasi Data Peta dengan Streamlit dan Plotly")
    st.write("Ini adalah contoh sederhana.")
    st.plotly_chart(fig)
