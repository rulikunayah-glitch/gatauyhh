import streamlit as st

st.title("💌 FORM AJAKAN BALIKAN 💌")
st.write("---")

nama = st.text_input("Nama :", placeholder="Ketik nama kamu di sini...")

st.subheader("Pertanyaan: Balikan?")

col1, col2 = st.columns(2)

with col1:
    if st.button("Iyaa mau 🥰"):
        nama_fix = nama if nama else "Kamu"
        st.balloons()
        st.success(f"🎉 YEEEY! {nama_fix} bilang: 'Iyaa mau'! Makasih yaaa ❤️✨")

with col2:
    if st.button("Mau banget! 😍"):
        nama_fix = nama if nama else "Kamu"
        st.balloons()
        st.success(f"💖 SWEET BANGET! {nama_fix} bilang: 'Mau banget!' Love you! 🥰👩‍❤️‍👨")
