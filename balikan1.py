
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Balikan Yuk 💗",
    page_icon="💌",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ffe0ec, #f4dfff);
}
h1, h2, p {
    color: #e75480;
}
</style>
""", unsafe_allow_html=True)

st.title("💌 Ajakan Balikan 💌")

nama = st.text_input("Masukkan nama kamu 🥹")

if nama:
    st.markdown(f"### Hai, {nama}! 💗")
    st.write("Aku masih sayang kamu...")
    st.subheader("Balikan sama kania imut lusyu menggemaskan mau? 🥺❤️")

    # Tombol dan efek dibuat di komponen HTML
    html = """
    <div style="text-align:center; padding:20px;
                background:#fff0f6; border-radius:20px;
                font-family:Arial;">
      <h2 style="color:#e75480;">Pilih jawabanmu 💕</h2>

      <div style="position:relative;height:150px;"
           id="area">
        <button id="yes" onclick="sayYes()"
          style="position:absolute;left:15%;top:25px;
          background:#ff6194;color:white;border:0;
          border-radius:12px;padding:13px 22px;
          font-size:17px;cursor:pointer;">
          Mau banget ❤️
        </button>

        <button id="no"
          style="position:absolute;left:55%;top:25px;
          background:#ddd;border:0;border-radius:12px;
          padding:13px 22px;font-size:17px;cursor:pointer;">
          Gamau 😝
        </button>
      </div>

      <div id="result" style="color:#e75480;
          font-size:22px;font-weight:bold;"></div>

      <script>
      const no = document.getElementById('no');
      const area = document.getElementById('area');

      function runAway() {
        const maxX = Math.max(0, area.clientWidth - no.offsetWidth);
        const maxY = Math.max(0, area.clientHeight - no.offsetHeight);
        no.style.left = Math.random() * maxX + 'px';
        no.style.top = Math.random() * maxY + 'px';
      }

      no.addEventListener('mouseenter', runAway);
      no.addEventListener('click', runAway);
      no.addEventListener('touchstart', function(e) {
        e.preventDefault();
        runAway();
      }, {passive:false});

      function sayYes() {
        document.getElementById('area').style.display = 'none';
        document.getElementById('result').innerHTML =
          'TAPI BOONG WLEEEEEE';

        const emojis = ['🖕','🤪','🤣','😝','🤡','💩','😏','🙄'];
        for (let i = 0; i < 70; i++) {
          setTimeout(() => {
            const h = document.createElement('span');
            h.innerText = emojis[Math.floor(Math.random()*emojis.length)];
            h.style.cssText = 'position:fixed;top:-30px;left:' +
              Math.random()*95 + 'vw;font-size:28px;z-index:9999;' +
              'pointer-events:none;animation:fall 4s linear forwards;';
            document.body.appendChild(h);
            setTimeout(() => h.remove(), 4100);
          }, i * 70);
        }
      }

      const style = document.createElement('style');
      style.innerHTML = '@keyframes fall {to {transform:translateY(100vh) rotate(600deg);opacity:0;}}';
      document.head.appendChild(style);
      </script>
    </div>
    """

    components.html(html, height=320, scrolling=False)

else:
    st.info("Isi nama dulu untuk membuka surat cinta 💌")
