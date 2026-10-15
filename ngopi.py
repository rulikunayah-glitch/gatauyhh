import streamlit as st
import random

# Konfigurasi Halaman
st.set_page_config(page_title="Ajakan Ngopi Princess Kania ☕", page_icon="👑", layout="centered")

# Judul Utama
st.title("👑 AJAKAN NGOPI BERSAMA PRINCESS KANIA ☕")
st.write("---")

# Input Nama
nama = st.text_input("Nama :", placeholder="Tulis nama kamu di sini...")

st.subheader("Pertanyaan: Besok free ga?")

# Daftar Tempat Ngopi Khusus (Random Antara Mosu dan Kru)
daftar_tempat = [
    "Mosu ☕✨",
    "Kru ☕✨"
]

# Tombol Pilihan Jawaban
col1, col2 = st.columns(2)

with col1:
    if st.button("Free sih 😊"):
        nama_fix = nama if nama else "Kamu"
        tempat = random.choice(daftar_tempat)
        st.balloons()
        st.success(f"🎉 yeyyy {nama_fix}! Jadi besok kamu: **'Free sih'**!")
        st.info(f"📍 **Tempat ngopi pilihan kita :** {tempat}\n\n⚠️ *jangan lupa kalo lupa aku cubit*")

with col2:
    if st.button("Free trs buat Kania 💖"):
        nama_fix = nama if nama else "Kamu"
        tempat = random.choice(daftar_tempat)
        st.snow()
        st.success(f"💖 Aww sweet banget! {nama_fix} bilang: **'Free trs buat Kania'** 🥰👩‍❤️‍👨")
        st.info(f"📍 **Tempat ngopi spesial pilihan kita:** {tempat}\n\n⚠️ *jangan lupa kalo lupa aku banting km*")
