
import streamlit as st
import uuid
import html

st.set_page_config(
    page_title="Barkas | Marketplace",
    page_icon="B",
    layout="wide"
)

# ==========================================
# DESIGN SYSTEM
# ==========================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background: #f5f8fc;
    color: #1b2b45;
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 1280px;
    padding: 1.7rem 2rem 3rem;
}

[data-testid="stSidebar"] {
    background: #102744;
}

[data-testid="stSidebar"] * {
    color: #eef5ff !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label {
    border-radius: 9px;
    padding: 7px 10px;
}

[data-testid="stSidebar"] hr {
    border-color: #304967;
}

h1, h2, h3 {
    color: #172c49 !important;
    letter-spacing: -0.7px;
}

h1 {
    font-weight: 800 !important;
}

p, label {
    color: #536780;
}

[data-testid="stCaptionContainer"] p {
    color: #71829a;
}

.brand {
    color: white;
    font-size: 29px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 0;
}

.brand-sub {
    font-size: 12px;
    color: #b7cae2;
    letter-spacing: 1px;
}

.hero {
    background: linear-gradient(115deg, #102744, #245a91);
    padding: 45px 42px;
    border-radius: 20px;
    color: white;
    margin: 8px 0 32px;
    box-shadow: 0 12px 35px rgba(16,39,68,.12);
}

.hero .eyebrow {
    font-size: 11px;
    color: #bcd6f5;
    font-weight: 700;
    letter-spacing: 2px;
}

.hero h1 {
    color: white !important;
    font-size: clamp(30px, 4vw, 46px);
    line-height: 1.12;
    margin: 12px 0;
}

.hero p {
    color: #d7e6f8;
    font-size: 15px;
    max-width: 540px;
    line-height: 1.8;
}

.section-title {
    font-size: 23px;
    font-weight: 750;
    color: #172c49;
}

.product-name {
    color: #172c49;
    font-size: 17px;
    font-weight: 700;
    line-height: 1.4;
}

.product-price {
    color: #175da8;
    font-size: 23px;
    font-weight: 800;
    margin: 8px 0;
}

.product-meta {
    font-size: 12px;
    color: #77879b;
}

.seller-label {
    font-size: 12px;
    color: #71829a;
}

[data-testid="stVerticalBlockBorderWrapper"] {
    background: #ffffff;
    border: 1px solid #e4eaf2;
    border-radius: 16px;
    box-shadow: 0 4px 15px rgba(25,52,85,.035);
}

div.stButton > button {
    background: #175da8;
    color: #ffffff !important;
    border: 1px solid #175da8;
    border-radius: 10px;
    min-height: 43px;
    font-size: 14px;
    font-weight: 650;
    transition: all .18s ease;
}

div.stButton > button:hover {
    background: #10477f;
    border-color: #10477f;
    color: #ffffff !important;
    transform: translateY(-1px);
}

div.stButton > button:disabled {
    background: #dfe6ef;
    color: #7b899a !important;
    border-color: #dfe6ef;
}

div[data-testid="stFormSubmitButton"] button {
    background: #175da8;
    color: white !important;
    border-radius: 10px;
    min-height: 46px;
    font-weight: 700;
}

div[data-testid="stFormSubmitButton"] button:hover {
    background: #10477f;
    color: white !important;
}

div[data-baseweb="input"] > div,
div[data-baseweb="textarea"] > div,
div[data-baseweb="select"] > div {
    border-radius: 10px;
    background: white;
    border-color: #dbe4ef;
}

div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea {
    color: #1b2b45;
}

div[data-testid="stFileUploader"] {
    background: white;
    border-radius: 12px;
}

[data-testid="stMetric"] {
    background: white;
    padding: 18px;
    border: 1px solid #e4eaf2;
    border-radius: 14px;
}

hr {
    border-color: #e2eaf4;
}

.footer {
    text-align: center;
    font-size: 12px;
    color: #8997a9;
    padding: 30px 0 10px;
}

.badge {
    display: inline-block;
    color: #175da8;
    background: #edf5ff;
    padding: 5px 9px;
    border-radius: 5px;
    font-size: 11px;
    font-weight: 650;
}

@media (max-width: 768px) {
    .block-container {
        padding: 1rem;
    }

    .hero {
        padding: 26px 22px;
    }
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# DATA PRODUK
# ==========================================
if "products" not in st.session_state:
    st.session_state.products = {
        "BRK001": {
            "nama": "Korean Cardigan",
            "harga": 85000,
            "kategori": "Pakaian",
            "ukuran": "M",
            "kondisi": "Good Condition",
            "stok": 5,
            "deskripsi": "Cardigan simpel untuk daily outfit.",
            "penjual": "Barkas Store",
            "foto": None
        },
        "BRK002": {
            "nama": "Vintage Denim Skirt",
            "harga": 55000,
            "kategori": "Pakaian",
            "ukuran": "S",
            "kondisi": "Very Good",
            "stok": 3,
            "deskripsi": "Rok denim vintage yang stylish.",
            "penjual": "Barkas Store",
            "foto": None
        },
        "BRK003": {
            "nama": "Basic Tanktop",
            "harga": 25000,
            "kategori": "Pakaian",
            "ukuran": "All Size",
            "kondisi": "Good Condition",
            "stok": 8,
            "deskripsi": "Tanktop basic untuk sehari-hari.",
            "penjual": "Barkas Store",
            "foto": None
        },
        "BRK004": {
            "nama": "Vintage Shirt",
            "harga": 45000,
            "kategori": "Pakaian",
            "ukuran": "L",
            "kondisi": "Good Condition",
            "stok": 4,
            "deskripsi": "Kemeja vintage dengan gaya casual.",
            "penjual": "Barkas Store",
            "foto": None
        }
    }

if "cart" not in st.session_state:
    st.session_state.cart = {}

if "orders" not in st.session_state:
    st.session_state.orders = []

if "seller_name" not in st.session_state:
    st.session_state.seller_name = ""

if "last_order" not in st.session_state:
    st.session_state.last_order = None

if "show_lapak" not in st.session_state:
    st.session_state.show_lapak = False

products = st.session_state.products

# ==========================================
# HELPER
# ==========================================
def rupiah(n):
    return "Rp" + f"{n:,}".replace(",", ".")

def get_subtotal():
    return sum(
        products[pid]["harga"] * qty
        for pid, qty in st.session_state.cart.items()
        if pid in products
    )

def safe_text(value):
    return html.escape(str(value))

# ==========================================
# SIDEBAR
# ==========================================
st.sidebar.markdown(
    '<div class="brand">BARKAS</div>'
    '<div class="brand-sub">MARKETPLACE</div>',
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "NAVIGATION",
    [
        "Home",
        "Jual Barang",
        "Lapak Saya",
        "Keranjang",
        "Checkout",
        "Pesanan"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption(
    f"Barang di keranjang: {sum(st.session_state.cart.values())}"
)
st.sidebar.markdown("---")
st.sidebar.caption("Barkas Marketplace")
st.sidebar.caption("Buy and sell with ease.")

# ==========================================
# HOME
# ==========================================
if menu == "Home":

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">BARKAS MARKETPLACE</div>
        <h1>Find something<br>worth keeping.</h1>
        <p>
            Temukan barang favoritmu atau berikan kesempatan
            baru untuk barang yang sudah tidak kamu gunakan.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Explore products</div>',
        unsafe_allow_html=True
    )
    st.caption("Temukan berbagai pilihan barang dari penjual Barkas.")

    c1, c2 = st.columns([3, 1])

    with c1:
        cari = st.text_input(
            "Cari barang",
            placeholder="Cari nama produk..."
        )

    with c2:
        kategori_filter = st.selectbox(
            "Kategori",
            ["Semua"] + sorted(set(
                p["kategori"] for p in products.values()
            ))
        )

    listing = [
        (pid, p)
        for pid, p in products.items()
        if cari.lower() in p["nama"].lower()
        and (
            kategori_filter == "Semua"
            or kategori_filter == p["kategori"]
        )
    ]

    if not listing:
        st.info("Belum ada produk yang sesuai.")

    cols = st.columns(3)

    for i, (pid, p) in enumerate(listing):

        with cols[i % 3]:

            with st.container(border=True):

                # Product image
                if p.get("foto"):
                    st.image(
                        p["foto"],
                        use_container_width=True
                    )
                else:
                    st.markdown(
                        """
                        <div style="
                        background:#edf3fa;
                        border-radius:12px;
                        height:185px;
                        display:flex;
                        align-items:center;
                        justify-content:center;
                        color:#8ca0b9;
                        font-size:14px;">
                        Product image
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                st.markdown(
                    f'<div class="product-name">'
                    f'{safe_text(p["nama"])}</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="product-price">'
                    f'{rupiah(p["harga"])}</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<span class="badge">'
                    f'{safe_text(p["kondisi"])}</span>',
                    unsafe_allow_html=True
                )

                st.write("")
                st.caption(
                    f'{p["kategori"]} · Ukuran {p["ukuran"]}'
                )
                st.caption("Penjual: " + p["penjual"])
                st.caption(f'Stok: {p["stok"]} pcs')

                st.write(p["deskripsi"])

                if p["stok"] > 0:

                    qty = st.number_input(
                        "Jumlah",
                        min_value=1,
                        max_value=p["stok"],
                        value=1,
                        step=1,
                        key="qty_" + pid
                    )

                    if st.button(
                        "Tambah ke keranjang",
                        key="add_" + pid,
                        use_container_width=True
                    ):
                        current = st.session_state.cart.get(pid, 0)

                        if current + qty <= p["stok"]:
                            st.session_state.cart[pid] = current + qty
                            st.toast("Produk ditambahkan.")
                        else:
                            st.error("Stok tidak mencukupi.")

                else:
                    st.button(
                        "Stok habis",
                        disabled=True,
                        key="sold_" + pid,
                        use_container_width=True
                    )

    st.markdown(
        '<div class="footer">BARKAS MARKETPLACE · BUY AND SELL</div>',
        unsafe_allow_html=True
    )

# ==========================================
# JUAL BARANG
# ==========================================
elif menu == "Jual Barang":

    st.title("Jual barang")
    st.caption("Pasang barangmu dan temukan pembeli di Barkas.")

    with st.container(border=True):

        st.subheader("Informasi produk")
        st.caption("Lengkapi detail barang yang ingin kamu jual.")

        with st.form("form_jual", clear_on_submit=True):

            penjual = st.text_input("Nama penjual")
            nama_barang = st.text_input("Nama barang")

            col1, col2 = st.columns(2)

            with col1:
                kategori = st.selectbox(
                    "Kategori",
                    [
                        "Pakaian",
                        "Sepatu",
                        "Tas",
                        "Aksesoris",
                        "Elektronik",
                        "Rumah Tangga",
                        "Lainnya"
                    ]
                )

                harga = st.number_input(
                    "Harga jual (Rp)",
                    min_value=1000,
                    value=25000,
                    step=1000
                )

                ukuran = st.text_input(
                    "Ukuran / spesifikasi"
                )

            with col2:
                kondisi = st.selectbox(
                    "Kondisi barang",
                    [
                        "Baru",
                        "Like New",
                        "Very Good",
                        "Good Condition",
                        "Fair Condition"
                    ]
                )

                stok = st.number_input(
                    "Jumlah stok",
                    min_value=1,
                    max_value=1000,
                    value=1
                )

            deskripsi = st.text_area(
                "Deskripsi produk",
                placeholder="Jelaskan warna, kondisi, minus, dan detail lainnya."
            )

            foto = st.file_uploader(
                "Foto produk",
                type=["jpg", "jpeg", "png", "webp"]
            )

            setuju = st.checkbox(
                "Saya memastikan barang dan deskripsi yang saya berikan benar."
            )

            submit = st.form_submit_button(
                "Pasang produk",
                use_container_width=True
            )

    if submit:

        if not penjual.strip() or not nama_barang.strip():
            st.error("Nama penjual dan nama barang wajib diisi.")

        elif not ukuran.strip() or not deskripsi.strip():
            st.error("Lengkapi ukuran dan deskripsi produk.")

        elif not setuju:
            st.error("Mohon setujui pernyataan terlebih dahulu.")

        else:
            pid = "BRK-" + uuid.uuid4().hex[:8].upper()

            foto_data = foto.getvalue() if foto else None

            st.session_state.products[pid] = {
                "nama": nama_barang.strip(),
                "harga": int(harga),
                "kategori": kategori,
                "ukuran": ukuran.strip(),
                "kondisi": kondisi,
                "stok": int(stok),
                "deskripsi": deskripsi.strip(),
                "penjual": penjual.strip(),
                "foto": foto_data
            }

            st.session_state.seller_name = penjual.strip()

            st.success("Produk berhasil ditambahkan.")
            st.write("ID produk:", pid)
            st.info("Produk sudah tersedia di katalog demo.")

# ==========================================
# LAPAK SAYA
# ==========================================
elif menu == "Lapak Saya":

    st.title("Lapak saya")
    st.caption("Kelola listing barang yang kamu pasang.")

    pemilik = st.text_input(
        "Nama penjual",
        value=st.session_state.seller_name
    )

    if st.button("Tampilkan lapak"):
        st.session_state.seller_name = pemilik.strip()
        st.session_state.show_lapak = True

    if st.session_state.show_lapak:

        listing = [
            (pid, p)
            for pid, p in products.items()
            if p["penjual"].casefold() == pemilik.strip().casefold()
        ]

        if not pemilik.strip():
            st.warning("Masukkan nama penjual.")

        elif not listing:
            st.info("Belum ada produk di lapak ini.")

        for pid, p in listing:

            with st.container(border=True):

                c1, c2 = st.columns([1, 3])

                with c1:
                    if p.get("foto"):
                        st.image(p["foto"], use_container_width=True)
                    else:
                        st.markdown("**Product image**")

                with c2:
                    st.subheader(p["nama"])
                    st.markdown(
                        f'<div class="product-price">'
                        f'{rupiah(p["harga"])}</div>',
                        unsafe_allow_html=True
                    )
                    st.caption("ID: " + pid)
                    st.caption(
                        f'Stok: {p["stok"]} · {p["kondisi"]}'
                    )

                    if pid.startswith("BRK-"):

                        confirm = st.checkbox(
                            "Konfirmasi hapus listing",
                            key="confirm_" + pid
                        )

                        if st.button(
                            "Hapus listing",
                            key="delete_" + pid
                        ):
                            ordered = any(
                                pid in order["items"]
                                for order in st.session_state.orders
                            )

                            if not confirm:
                                st.warning("Centang konfirmasi terlebih dahulu.")
                            elif ordered:
                                st.error(
                                    "Produk sudah memiliki riwayat pesanan. "
                                    "Tidak dapat dihapus pada demo ini."
                                )
                            else:
                                del st.session_state.products[pid]
                                st.session_state.cart.pop(pid, None)
                                st.success("Listing dihapus.")
                                st.rerun()
                    else:
                        st.caption("Produk contoh Barkas.")

# ==========================================
# KERANJANG
# ==========================================
elif menu == "Keranjang":

    st.title("Keranjang belanja")
    st.caption("Periksa produk pilihanmu sebelum checkout.")

    cart = st.session_state.cart

    if not cart:
        st.info("Keranjang masih kosong.")
    else:

        for pid, qty in list(cart.items()):

            if pid not in products:
                continue

            p = products[pid]

            with st.container(border=True):

                c1, c2 = st.columns([4, 1])

                with c1:
                    st.subheader(p["nama"])
                    st.caption("Penjual: " + p["penjual"])
                    st.write(
                        f'{rupiah(p["harga"])} × {qty}'
                    )
                    st.write(
                        "**Subtotal:**",
                        rupiah(p["harga"] * qty)
                    )

                with c2:
                    if st.button("Hapus", key="remove_" + pid):
                        del st.session_state.cart[pid]
                        st.rerun()

        st.divider()
        st.metric("Total belanja", rupiah(get_subtotal()))
        st.caption("Lanjutkan melalui menu Checkout.")

# ==========================================
# CHECKOUT
# ==========================================
elif menu == "Checkout":

    st.title("Checkout")
    st.caption("Lengkapi informasi pengiriman dan pembayaran.")

    cart = {
        pid: qty
        for pid, qty in st.session_state.cart.items()
        if pid in products
    }

    if not cart:
        st.info("Keranjang masih kosong.")
    else:

        subtotal = sum(
            products[pid]["harga"] * qty
            for pid, qty in cart.items()
        )

        st.subheader("Ringkasan pesanan")

        for pid, qty in cart.items():
            p = products[pid]
            st.write(
                f'**{p["nama"]}** × {qty} — '
                f'{rupiah(p["harga"] * qty)}'
            )
            st.caption("Penjual: " + p["penjual"])

        st.divider()

        with st.form("checkout_form"):

            nama = st.text_input("Nama penerima")
            telepon = st.text_input("Nomor telepon")
            alamat = st.text_area("Alamat lengkap")

            kurir = st.selectbox(
                "Pengiriman",
                ["Reguler", "Express"]
            )

            metode = st.selectbox(
                "Metode pembayaran",
                ["Transfer (Simulasi)", "COD"]
            )

            ongkir = 15000 if kurir == "Reguler" else 25000
            total = subtotal + ongkir

            st.write("Subtotal:", rupiah(subtotal))
            st.write("Ongkir simulasi:", rupiah(ongkir))

            st.markdown(
                f"""
                <div style="background:white;padding:20px;
                border:1px solid #e4eaf2;border-radius:14px;">
                    <div style="color:#71829a;font-size:12px;">
                        TOTAL PEMBAYARAN
                    </div>
                    <div style="font-size:29px;font-weight:800;
                    color:#175da8;">
                        {rupiah(total)}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            submit_order = st.form_submit_button(
                "Buat pesanan",
                use_container_width=True
            )

        if submit_order:

            phone = (
                telepon.strip()
                .replace("+", "")
                .replace("-", "")
                .replace(" ", "")
            )

            if not nama.strip() or not phone or not alamat.strip():
                st.error("Lengkapi seluruh data penerima.")

            elif not phone.isdigit():
                st.error("Nomor telepon tidak valid.")

            elif any(
                qty > products[pid]["stok"]
                for pid, qty in cart.items()
            ):
                st.error("Stok tidak mencukupi.")

            else:
                nomor = "BRK-" + uuid.uuid4().hex[:8].upper()

                for pid, qty in cart.items():
                    products[pid]["stok"] -= qty

                order = {
                    "nomor": nomor,
                    "nama": nama.strip(),
                    "telepon": telepon,
                    "alamat": alamat,
                    "kurir": kurir,
                    "metode": metode,
                    "subtotal": subtotal,
                    "ongkir": ongkir,
                    "total": total,
                    "items": dict(cart),
                    "status": (
                        "Menunggu Konfirmasi"
                        if metode == "COD"
                        else "Menunggu Pembayaran (Simulasi)"
                    )
                }

                st.session_state.orders.append(order)
                st.session_state.last_order = order
                st.session_state.cart = {}
                st.rerun()

    order = st.session_state.last_order

    if order:
        st.success("Pesanan berhasil dibuat.")

        with st.container(border=True):
            st.subheader("Konfirmasi pesanan")
            st.write("Nomor pesanan:", order["nomor"])
            st.write("Nama:", order["nama"])
            st.write("Total:", rupiah(order["total"]))
            st.write("Metode:", order["metode"])
            st.info("Status: " + order["status"])
            st.caption("Transaksi ini masih berupa simulasi.")

# ==========================================
# PESANAN
# ==========================================
elif menu == "Pesanan":

    st.title("Riwayat pesanan")

    if not st.session_state.orders:
        st.info("Belum ada pesanan.")
    else:
        for order in reversed(st.session_state.orders):

            with st.container(border=True):

                st.subheader("Pesanan " + order["nomor"])
                st.caption(order["nama"])

                for pid, qty in order["items"].items():
                    nama_produk = (
                        products[pid]["nama"]
                        if pid in products
                        else "Produk"
                    )
                    st.write(f"- {nama_produk} × {qty}")

                st.write("Total:", rupiah(order["total"]))
                st.write("Pembayaran:", order["metode"])
                st.info("Status: " + order["status"])

                st.caption("Status pesanan demo.")

# ==========================================
# FOOTER
# ==========================================
st.sidebar.markdown("---")
st.sidebar.caption("BARKAS MARKETPLACE")
st.sidebar.caption("A better way to buy and sell.")

st.markdown(
    '<div class="footer">'
    'BARKAS · Marketplace Demo · Buy and Sell'
    '</div>',
    unsafe_allow_html=True
)
