import streamlit as st
#ini judul web
st.title("Kalkulator Aing ni bos")
st.write("aplikasi kalkulator sederhana anjay")

#input angka disini
angka1 = st.number_input("Masukkan Angka Pertama:", value=0.0)
angka2 = st.number_input("Masukkan Angka Kedua:", value=0.0)

#baris ini pilih operasi matematika
operasi = st.selectbox(
    "Pilih operasi Matematika:",
    ["Penjumlahan (+)", "Pengurangan (-)", "Perkalian (*)", "Pembagian (/)"]
)

# buat tombbol menghitung
if st.button("Hitung Hasil"):
    if operasi == "Penjumlahan (+)":
        hasil = angka1 + angka2 
        st.success(f"Hasil: {angka1} + {angka2} = {hasil}")
    elif operasi == "Pengurangan (-)":
        hasil = angka1 - angka2
        st.success(f"Hasil: {angka1} - {angka2} = {hasil}")
    elif operasi == "Perkalian (*)":
        hasil = angka1 * angka2
        st.success(f"Hasil: {angka1} * {angka2} = {hasil}")
    elif operasi == "Pembagian (/)":
        if angka2 != 0:
            hasil = angka1 / angka2
            st.success(f"Hasil: {angka1} / {angka2} = {hasil}")
        else:
            st.error("Error: nyoba lagi lu bagi make 0")