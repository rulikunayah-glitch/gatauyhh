
import streamlit as st

st.set_page_config(
    page_title="Barkas | Online Shop",
    page_icon="🛍️",
    layout="wide"
)

# ==========================
# CUSTOM DESIGN
# ==========================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #dceeff, #f2f8ff);
    color: #183153;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

[data-testid="stSidebar"] {
    background-color: #183153;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

.hero {
    background: linear-gradient(120deg, #183153, #2878c8);
    padding: 35px;
    border-radius: 24px;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0 8px 25px #18315322;
}

.hero h1 {
    font-size: 48px;
    margin: 0;
    color: white;
}

.hero p {
    color: #e0efff;
    font-size: 17px;
}

.product-card {
    background: white;
    padding: 22px;
    border-radius: 20px;
    border: 1px solid #d4e5f8;
    box-shadow: 0 5px 20px #18315310;
    min-height: 210px;
    margin-bottom: 10px;
}

.product-name {
    font-size: 21px;
    font-weight: 700;
    color: #183153;
}

.price {
    color: #1874cf;
    font-size: 24px;
    font-weight: 800;
    margin: 12px 0;
}

.tag {
    display: inline-block;
    background: #e4f1ff;
    color: #2264a0;
    padding: 5px 11px;
    border-radius: 30px;
    font-size: 12px;
}

div.stButton > button {
    background-color: #2878c8;
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px;
    font-weight: 600;
    transition: 0.2s;
}

div.stButton > button:hover {
    background-color: #183153;
    color: white;
    border: none;
}

h1, h2, h3 {
    color: #183153;
}

[data-testid="stMetric"] {
    background: white;
    padding: 18px;
    border-radius: 16px;
    border: 1px solid #d4e5f8;
}

hr {
    border-color: #c8def5;
}
</style>
""", unsafe_allow_html=True)

# ==========================
# DATA PRODUK
# ==========================
if "products" not in st.session_state:
    st.session_state.products = {
        "Korean Cardigan": {
            "harga": 85000,
            "ukuran": "M",
            "kondisi": "Good Condition",
            "stok": 5,
            "emoji": "🧥",
            "deskripsi": "Cardigan simpel untuk daily outfit."
        },
        "Vintage Denim Skirt": {
            "harga": 55000,
            "ukuran": "S",
            "kondisi": "Very Good",
            "stok": 3,
            "emoji": "👗",
            "deskripsi": "Rok denim vintage yang stylish."
        },
        "Basic Tanktop": {
            "harga": 25000,
            "ukuran": "All Size",
            "kondisi": "Good Condition",
            "stok": 8,
            "emoji": "👚",
            "deskripsi": "Tanktop basic yang mudah dipadukan."
        },
        "Vintage Shirt": {
            "harga": 45000,
            "ukuran": "L",
            "kondisi": "Good Condition",
            "stok": 4,
            "emoji": "👕",
            "deskripsi": "Kemeja vintage untuk tampilan casual."
        }
    }

if "cart" not in st.session_state:
    st.session_state.cart = {}

if "order" not in st.session_state:
    st.session_state.order = None

products = st.session_state.products

def rupiah(n):
    return "Rp" + f"{n:,}".replace(",", ".")

# ==========================
# SIDEBAR
# ==========================
st.sidebar.markdown("# 🛍️ BARKAS")
st.sidebar.caption("Your favorite finds.")
menu = st.sidebar.radio(
    "NAVIGATION",
    ["Home", "Keranjang", "Checkout"]
)

jumlah_cart = sum(st.session_state.cart.values())
st.sidebar.markdown("---")
st.sidebar.markdown(f"🛒 Isi keranjang: **{jumlah_cart} barang**")
st.sidebar.markdown("---")
st.sidebar.caption("Barkas Online Store")

# ==========================
# HOME
# ==========================
if menu == "Home":

    st.markdown("""
    <div class="hero">
        <h1>🛍️ BARKAS</h1>
        <p>Find your style, find your favorite.</p>
        <p>Temukan barang favoritmu dengan harga bersahabat.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Explore Our Collection")
    st.write("Pilihan barang yang bisa kamu temukan di Barkas.")

    cari = st.text_input(
        "🔎 Cari produk",
        placeholder="Cari cardigan, skirt, tanktop..."
    )

    daftar = [
        (nama, p) for nama, p in products.items()
        if cari.lower() in nama.lower()
    ]

    if not daftar:
        st.info("Produk tidak ditemukan.")

    cols = st.columns(2)

    for i, (nama, p) in enumerate(daftar):
        with cols[i % 2]:
            with st.container(border=True):
                st.markdown(
                    f"""
                    <div style="text-align:center; padding:10px;">
                        <div style="font-size:65px;">
                            {p['emoji']}
                        </div>
                        <div class="product-name">{nama}</div>
                        <div class="price">{rupiah(p['harga'])}</div>
                        <span class="tag">{p['kondisi']}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.write(p["deskripsi"])
                st.caption(
                    f"Ukuran: {p['ukuran']} | Stok: {p['stok']}"
                )

                qty = st.number_input(
                    "Jumlah",
                    min_value=1,
                    max_value=max(1, p["stok"]),
                    value=1,
                    key="qty_" + nama,
                    disabled=p["stok"] == 0
                )

                if p["stok"] == 0:
                    st.error("Stok habis.")
                elif st.button(
                    "＋ Tambah ke Keranjang",
                    key="add_" + nama,
                    use_container_width=True
                ):
                    sudah = st.session_state.cart.get(nama, 0)

                    if sudah + qty <= p["stok"]:
                        st.session_state.cart[nama] = sudah + qty
                        st.toast("Produk berhasil ditambahkan!")
                    else:
                        st.error("Jumlah melebihi stok tersedia.")

    st.markdown("---")
    st.caption("BARKAS © Online Store Demo")

# ==========================
# KERANJANG
# ==========================
elif menu == "Keranjang":

    st.markdown("## 🛒 Keranjang Belanja")
    cart = st.session_state.cart

    if not cart:
        st.info("Keranjangmu masih kosong. Yuk, pilih produk!")
    else:
        total = 0

        for nama, qty in list(cart.items()):
            p = products[nama]
            subtotal = p["harga"] * qty
            total += subtotal

            with st.container(border=True):
                c1, c2 = st.columns([3, 1])

                with c1:
                    st.markdown(f"### {p['emoji']} {nama}")
                    st.write(f"{rupiah(p['harga'])} × {qty}")
                    st.write(f"Subtotal: **{rupiah(subtotal)}**")

                with c2:
                    if st.button("Hapus", key="hapus_" + nama):
                        del st.session_state.cart[nama]
                        st.rerun()

        st.divider()
        st.metric("Total Belanja", rupiah(total))

        st.info("Pilih menu Checkout di sidebar untuk melanjutkan.")

# ==========================
# CHECKOUT
# ==========================
elif menu == "Checkout":

    st.markdown("## 💳 Checkout")
    cart = st.session_state.cart

    if not cart:
        st.info("Keranjang masih kosong.")
    else:
        subtotal = sum(
            products[nama]["harga"] * qty
            for nama, qty in cart.items()
        )

        st.markdown("### Ringkasan Pesanan")

        for nama, qty in cart.items():
            p = products[nama]
            st.write(
                f"- {nama} × {qty} — "
                f"{rupiah(p['harga'] * qty)}"
            )

        st.divider()

        nama_pembeli = st.text_input("Nama Penerima")
        telepon = st.text_input("Nomor Telepon")
        alamat = st.text_area("Alamat Lengkap")

        kurir = st.selectbox(
            "Pengiriman",
            ["Reguler", "Express"]
        )

        ongkir = 15000 if kurir == "Reguler" else 25000

        metode = st.selectbox(
            "Metode Pembayaran",
            ["Transfer (Simulasi)", "COD"]
        )

        st.markdown("### Rincian Pembayaran")
        st.write("Subtotal:", rupiah(subtotal))
        st.write("Ongkir:", rupiah(ongkir))

        st.markdown(
            f"<div class='product-card'>"
            f"<div>Total Pembayaran</div>"
            f"<div class='price'>{rupiah(subtotal + ongkir)}</div>"
            f"</div>",
            unsafe_allow_html=True
        )

        if st.button("Buat Pesanan", use_container_width=True):

            if not nama_pembeli.strip() or not telepon.strip() or not alamat.strip():
                st.error("Mohon lengkapi semua data.")
            elif not telepon.strip().replace("+", "").replace("-", "").replace(" ", "").isdigit():
                st.error("Nomor telepon tidak valid.")
            elif any(
                qty > products[nama]["stok"]
                for nama, qty in cart.items()
            ):
                st.error("Stok tidak mencukupi.")
            else:
                for nama, qty in cart.items():
                    products[nama]["stok"] -= qty

                st.session_state.order = {
                    "nama": nama_pembeli,
                    "total": subtotal + ongkir,
                    "metode": metode,
                    "status": (
                        "Menunggu Konfirmasi"
                        if metode == "COD"
                        else "Menunggu Pembayaran (Simulasi)"
                    )
                }

                st.session_state.cart = {}
                st.rerun()

    if st.session_state.order:
        order = st.session_state.order

        st.success("Pesanan berhasil dibuat!")
        st.markdown("### 🎉 Order Summary")
        st.write("Nama:", order["nama"])
        st.write("Total:", rupiah(order["total"]))
        st.write("Pembayaran:", order["metode"])
        st.info("Status: " + order["status"])
        st.caption(
            "Ini hanya simulasi. Belum ada pembayaran "
            "atau pengiriman sungguhan."
        )
