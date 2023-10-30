import streamlit as st

# sidebar
# title dari sidebar
st.sidebar.title("Navigation")
# membuat select radio
menu = st.sidebar.radio('goto', ["Beranda", "Perbandingan"])

if menu == "Beranda":
    # mengambil filke beranda.py
    import beranda
    # menampilkan tampilan beranda diambil dari function tampil
    beranda.tampil()

elif menu == "Perbandingan":
    # mengambil filke perbandingan.py
    import perbandingan
    # menampilkan tampilan perbandingan diambil dari function tampil
    perbandingan.tampil()


