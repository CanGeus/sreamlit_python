import streamlit as st
import pandas as pd
import plotly.express as px

# Load data from the CSV file
df = pd.read_csv('data.csv')  # Ganti 'data.csv' dengan nama file CSV yang sesuai

# Set the title of the web app
st.title('Grafik Indeks Pendidikan Berdasarkan Tahun')

# Dropdown input for selecting a year
selected_year = st.selectbox('Pilih Tahun:', df['tahun'].unique())

# Filter data based on the selected year
filtered_df = df[df['tahun'] == selected_year]

# Create a Plotly bar chart
fig = px.bar(
    filtered_df,
    x='provinsi',
    y='indeks_pendidikan',
    labels={'indeks_pendidikan': 'Indeks Pendidikan'},
    title=f'Grafik Indeks Pendidikan Tahun {selected_year}'
)

# Display the chart
st.plotly_chart(fig)
