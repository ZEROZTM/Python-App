import streamlit as st

st.write("""
# Aplikasi Luas Segitiga
Ini adalah aplikasi menghitung luas segitiga sederhana menggunakan Python
""")

alas = st.number_input("Masukkan alas segitiga", 0)
tinggi = st.number_input("Masukkan tinggi segitiga", 0)
hitung =- st.button("Hitung Luas")

if hitung:
    luas = alas*tinggi/2
    st.write("Luas segitiga adalah ",luas)
