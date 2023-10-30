import streamlit as st
import pandas as pd
import plotly.express as px

def tampil():
    # mengambil data dari file csv
    data = pd.read_csv("data.csv")

    # menampilkan title
    st.title("Perbandingan Indeks Pendidikan antara Dua Provinsi")

    # tampilan select box pilih tahun
    selected_year = st.selectbox("Tahun:", data["tahun"].unique())

    # filter data sesuai select box
    filtered_data = data[data["tahun"] == selected_year]

    # parameter untuk membandingkan 2 provinsi
    province1 = st.selectbox("Pilih Provinsi Pertama:", filtered_data["provinsi"].unique())
    province2 = st.selectbox("Pilih Provinsi Kedua:", filtered_data["provinsi"].unique())

    # filter data sesuai data select box provinsi
    province1_data = filtered_data[filtered_data["provinsi"] == province1]
    province2_data = filtered_data[filtered_data["provinsi"] == province2]

    # membuat diagram lingkaran
    fig = px.pie(
        values=[province1_data["indeks_pendidikan"].sum(), province2_data["indeks_pendidikan"].sum()],
        names=[province1, province2],
        title=f"Perbandingan Indeks Pendidikan antara {province1} dan {province2} ({selected_year})"
    )

    # menampilkan diagram lingkaran
    st.plotly_chart(fig)

    # menampilkan table berdasarkan provinsi yang di bandingkan dan tahun yang dipilih
    st.write(f"Data Tabel untuk {province1} dan {province2}:")
    st.write(pd.concat([province1_data, province2_data]))

    # Hitung selisih indeks pendidikan antara 2 provinsi yang di bandinglkan
    margin_indeks = abs(province1_data["indeks_pendidikan"].sum() - province2_data["indeks_pendidikan"].sum())
    margin_indeks = round(margin_indeks, 2)

    if province1_data["indeks_pendidikan"].sum() > province2_data["indeks_pendidikan"].sum():
        st.title(f"Indeks pendidikan provinsi {province1} lebih besar {margin_indeks} dari provinsi {province2}")

    elif province1_data["indeks_pendidikan"].sum() < province2_data["indeks_pendidikan"].sum():
        st.title(f"Indeks pendidikan provinsi {province2} lebih besar {margin_indeks} dari provinsi {province1}")
