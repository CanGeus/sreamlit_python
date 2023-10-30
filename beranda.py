import streamlit as st
import pandas as pd
import plotly.express as px

def tampil():
    # membaca data di file csv
    df = pd.read_csv('data.csv')

    # menampilkan title
    st.title('Grafik Indeks Pendidikan Berdasarkan Tahun')

    # tampilan select box pilih tahun
    selected_year = st.selectbox('Pilih Tahun:', df['tahun'].unique())

    # filter data sesuai select box tahun
    filtered_df = df[df['tahun'] == selected_year]

    # fungsi untuk membuat diagram batang
    fig = px.bar(
        filtered_df,
        x='provinsi',
        y='indeks_pendidikan',
        labels={'indeks_pendidikan': 'Indeks Pendidikan'},
        title=f'Grafik Indeks Pendidikan Tahun {selected_year}'
    )

    # menampilakn diagram batang
    st.plotly_chart(fig)

    # menampilkan index pendidikan tertinggi
    index_max = filtered_df['indeks_pendidikan'].max()
    # mengambil index pendidikan provinsi tertinggi
    provinsi_max = filtered_df.loc[filtered_df['indeks_pendidikan'].idxmax()]['provinsi']
    # menampilkan text
    st.text(f'Indeks Pendidikan Tertinggi Tahun {selected_year} adalah {index_max} di Provinsi {provinsi_max}')
