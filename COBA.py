
import streamlit as st
import uuid

st.set_page_config(
    page_title="Barkas Marketplace",
    page_icon="🛍️",
    layout="wide"
)

# ==========================================
# CSS DESIGN
# ==========================================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#e8f3ff,#f8fbff,#e4efff);
    color: #183153;
}
.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#153765,#10294e);
}
[data-testid="stSidebar"] * {
    color: white !important;
}
h1,h2,h3 { color: #183153 !important; }
.hero {
    background: linear-gradient(120deg,#153765,#2878d0);
    padding: 35px;
    border-radius: 25px;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0 12px 30px #18315320;
}
.hero h1 {
    color: white !important;
    font-size: 44px;
    font-weight: 850;
}
.hero p { color: #e3efff; }
div.stButton > button {
    background: linear-gradient(110deg,#3989ed,#1764c0);
    color: white !important;
    border: none;
    border-radius: 14px;
    min-height: 44px;
    font-weight: 700;
    transition: 0.2s;
}
div.stButton > button:hover {
    background: #103e80;
    color: white !important;
    transform: translateY(-2px);
}
[data-testid="stVerticalBlockBorderWrapper"] {
    background: white;
    border: 1px solid #d8e8f8;
    border-radius: 18px;
    box-shadow: 0 5px 20px #1831530b;
}
.price {
    color: #176ed0;
    font-size: 25px;
    font-weight: 800;
}
div[data-baseweb="input"] > div,
div[data-baseweb="textarea"] > div,
div[data-baseweb="select"] > div {
    border-radius: 12px;
    background: white;
}
.footer {
    text-align: center;
    color: #6c829e;
    padding: 25px;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# DATA AWAL
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
            "deskripsi": "Tanktop basic untuk outfit sehari-hari.",
            "penjual": "Barkas Store",
            "foto": None
        }
    }

if "cart" not in st.session_state:
    st.session_state.cart = {}

if "orders" not in st.session_state:
    st.session_state.orders = []

if "last_order" not in st.session_state:
    st.session_state.last_order = None

if "seller_name" not in st.session_state:
    st.session_state.seller_name = ""

products = st.session_state.products

# ==========================================
# HELPER
# ==========================================
def rupiah(n):
    return "Rp" + f"{n:,}".replace(",", ".")

def subtotal_cart():
    return sum(
        products[pid]["harga"] * qty
        for pid, qty in st.session_state.cart.items()
        if pid in products
    )

# ==========================================
# SIDEBAR
# ==========================================
st.sidebar.markdown("# 🛍️ BARKAS")
st.sidebar.caption("Find your style, find your favorite.")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "MENU",
    [
        "Home",
        "Jual Barang",
        "Lapak Saya",
        "My Bag",
        "Checkout",
        "Pesanan Saya"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    f"🛒 Keranjang: {sum(st.session_state.cart.values())} barang"
)

st.sidebar.caption("BARKAS MARKETPLACE")

# ==========================================
# HOME / KATALOG
# ==========================================
if menu == "Home":

    st.markdown("""
    <div class="hero">
        <p style="letter-spacing:2px;font-size:12px;">
            BUY • SELL • REPEAT
        </p>
        <h1>Welcome to Barkas ✨</h1>
        <p>
            Temukan barang favoritmu atau jual barangmu di sini.
            <br>Good finds, better prices.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Discover Products")
    st.caption("Jelajahi barang pilihan dari para penjual Barkas.")

    cari = st.text_input(
        "🔎 Cari barang",
        placeholder="Cari nama produk..."
    )

    kategori_filter = st.selectbox(
        "Kategori",
        ["Semua"] + sorted(set(
            p["kategori"] for p in products.values()
        ))
    )

    hasil = [
        (pid, p) for pid, p in products.items()
        if cari.lower() in p["nama"].lower()
        and (kategori_filter == "Semua"
             or p["kategori"] == kategori_filter)
    ]

    if not hasil:
        st.info("Produk belum tersedia.")

    cols = st.columns(2)

    for i, (pid, p) in enumerate(hasil):

        with cols[i % 2]:

            with st.container(border=True):

                if p.get("foto") is not None:
                    st.image(p["foto"], use_container_width=True)
                else:
                    st.markdown(
                        "<div style='background:#edf5ff;"
                        "border-radius:15px;padding:25px;"
                        "text-align:center;font-size:60px;'>"
                        "🛍️</div>",
                        unsafe_allow_html=True
                    )

                st.subheader(p["nama"])

                st.markdown(
                    f"<div class='price'>{rupiah(p['harga'])}</div>",
                    unsafe_allow_html=True
                )

                st.caption(
                    f"{p['kategori']} • {p['kondisi']}"
                )
                st.write("Ukuran:", p["ukuran"])
                st.write("Penjual:", p["penjual"])
                st.write(p["deskripsi"])
                st.caption(f"Stok: {p['stok']} pcs")

                if p["stok"] > 0:

                    qty = st.number_input(
                        "Jumlah",
                        min_value=1,
                        max_value=p["stok"],
                        value=1,
                        key="qty_" + pid
                    )

                    if st.button(
                        "🛍️ Add to Bag",
                        key="add_" + pid,
                        use_container_width=True
                    ):
                        current = st.session_state.cart.get(pid, 0)

                        if current + qty <= p["stok"]:
                            st.session_state.cart[pid] = current + qty
                            st.toast("Produk masuk keranjang!")
                        else:
                            st.error("Stok tidak mencukupi.")
                else:
                    st.warning("Stok habis.")

    st.markdown(
        "<div class='footer'>BARKAS MARKETPLACE</div>",
        unsafe_allow_html=True
    )

# ==========================================
# JUAL BARANG
# ==========================================
elif menu == "Jual Barang":

    st.title("💙 Jual Barang di Barkas")
    st.write("Punya barang yang sudah tidak dipakai? Yuk, jual di sini!")

    st.info(
        "Isi informasi produk dengan benar. "
        "Foto produk opsional untuk demo ini."
    )

    with st.form("form_jual", clear_on_submit=True):

        nama_penjual = st.text_input("Nama Penjual")
        nama_barang = st.text_input("Nama Barang")

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
            "Harga Jual (Rp)",
            min_value=1000,
            value=25000,
            step=1000
        )

        ukuran = st.text_input(
            "Ukuran / Spesifikasi",
            placeholder="Misalnya M, 38, atau tidak ada"
        )

        kondisi = st.selectbox(
            "Kondisi Barang",
            [
                "Baru",
                "Like New",
                "Very Good",
                "Good Condition",
                "Fair Condition"
            ]
        )

        stok = st.number_input(
            "Jumlah Stok",
            min_value=1,
            max_value=1000,
            value=1
        )

        deskripsi = st.text_area(
            "Deskripsi Barang",
            placeholder="Jelaskan kondisi, warna, minus, dll."
        )

        foto = st.file_uploader(
            "Foto Barang (opsional)",
            type=["jpg", "jpeg", "png", "webp"]
        )

        setuju = st.checkbox(
            "Saya memastikan informasi barang yang dijual benar."
        )

        submit_jual = st.form_submit_button(
            "✨ Pasang Barang",
            use_container_width=True
        )

    if submit_jual:

        if not nama_penjual.strip() or not nama_barang.strip():
            st.error("Nama penjual dan nama barang wajib diisi.")

        elif not ukuran.strip() or not deskripsi.strip():
            st.error("Lengkapi ukuran/spesifikasi dan deskripsi.")

        elif not setuju:
            st.error("Silakan centang pernyataan terlebih dahulu.")

        else:
            pid = "BRK-" + uuid.uuid4().hex[:8].upper()

            foto_bytes = foto.getvalue() if foto else None

            st.session_state.products[pid] = {
                "nama": nama_barang.strip(),
                "harga": int(harga),
                "kategori": kategori,
                "ukuran": ukuran.strip(),
                "kondisi": kondisi,
                "stok": int(stok),
                "deskripsi": deskripsi.strip(),
                "penjual": nama_penjual.strip(),
                "foto": foto_bytes
            }

            st.session_state.seller_name = nama_penjual.strip()

            st.success("🎉 Barang berhasil dipasang di Barkas!")
            st.write("ID Produk:", pid)
            st.info("Cek barangmu di menu Home atau Lapak Saya.")

# ==========================================
# LAPAK SAYA
# ==========================================
elif menu == "Lapak Saya":

    st.title("🏪 Lapak Saya")
    st.caption("Kelola barang yang kamu jual.")

    pemilik = st.text_input(
        "Masukkan nama penjual",
        value=st.session_state.seller_name,
        key="pemilik_lapak"
    )

    if st.button("Lihat Lapak", use_container_width=True):

        st.session_state.seller_name = pemilik.strip()
        st.session_state.show_lapak = True

    if st.session_state.get("show_lapak", False):

        if not pemilik.strip():
            st.warning("Masukkan nama penjual.")
        else:
            listing = [
                (pid, p)
                for pid, p in st.session_state.products.items()
                if p["penjual"].casefold() == pemilik.strip().casefold()
            ]

            if not listing:
                st.info("Belum ada barang dari nama penjual ini.")

            for pid, p in listing:

                with st.container(border=True):

                    if p.get("foto") is not None:
                        st.image(p["foto"], width=180)

                    st.subheader(p["nama"])
                    st.markdown(
                        f"<div class='price'>{rupiah(p['harga'])}</div>",
                        unsafe_allow_html=True
                    )

                    st.write("ID:", pid)
                    st.write("Stok:", p["stok"])
                    st.write("Kondisi:", p["kondisi"])

                    # Listing bawaan tidak dapat dihapus
                    if not pid.startswith("BRK-"):
                        st.caption("Produk contoh Barkas.")
                    else:
                        konfirmasi = st.checkbox(
                            "Saya ingin menghapus listing ini",
                            key="confirm_" + pid
                        )

                        if st.button(
                            "🗑️ Hapus Barang",
                            key="del_" + pid
                        ):
                            if konfirmasi:
                                # Hanya hapus jika bukan produk dalam pesanan
                                sudah_dipesan = any(
                                    pid in order["items"]
                                    for order in st.session_state.orders
                                )

                                if sudah_dipesan:
                                    st.error(
                                        "Produk sudah memiliki riwayat pesanan. "
                                        "Hubungi admin untuk pengelolaan."
                                    )
                                else:
                                    del st.session_state.products[pid]
                                    st.session_state.cart.pop(pid, None)
                                    st.success("Listing berhasil dihapus.")
                                    st.rerun()
                            else:
                                st.warning("Centang konfirmasi dahulu.")

# ==========================================
# MY BAG
# ==========================================
elif menu == "My Bag":

    st.title("🛍️ My Bag")
    st.caption("Periksa barang pilihanmu.")

    cart = st.session_state.cart

    if not cart:
        st.info("Keranjang masih kosong.")
    else:

        for pid, qty in list(cart.items()):

            if pid not in products:
                continue

            p = products[pid]

            with st.container(border=True):

                c1, c2 = st.columns([3, 1])

                with c1:
                    st.subheader(p["nama"])
                    st.write(f"{rupiah(p['harga'])} × {qty}")
                    st.write(
                        "Subtotal:",
                        rupiah(p["harga"] * qty)
                    )
                    st.caption("Penjual: " + p["penjual"])

                with c2:
                    if st.button("🗑️ Hapus", key="remove_" + pid):
                        del st.session_state.cart[pid]
                        st.rerun()

        st.divider()
        st.metric("Total Belanja", rupiah(subtotal_cart()))
        st.info("Buka menu Checkout untuk melanjutkan.")

# ==========================================
# CHECKOUT
# ==========================================
elif menu == "Checkout":

    st.title("💳 Checkout")

    cart = st.session_state.cart

    if not cart:
        st.info("Keranjang masih kosong.")
    else:

        valid_cart = {
            pid: qty for pid, qty in cart.items()
            if pid in products
        }

        subtotal = sum(
            products[pid]["harga"] * qty
            for pid, qty in valid_cart.items()
        )

        st.subheader("Ringkasan Pesanan")

        for pid, qty in valid_cart.items():
            p = products[pid]
            st.write(
                f"- {p['nama']} × {qty} "
                f"— {rupiah(p['harga'] * qty)}"
            )

        st.divider()

        with st.form("form_checkout"):

            nama = st.text_input("Nama Penerima")
            telepon = st.text_input("Nomor Telepon")
            alamat = st.text_area("Alamat Lengkap")

            kurir = st.selectbox(
                "Pengiriman",
                ["Reguler", "Express"]
            )

            metode = st.selectbox(
                "Metode Pembayaran",
                ["Transfer (Simulasi)", "COD"]
            )

            ongkir = 15000 if kurir == "Reguler" else 25000
            total = subtotal + ongkir

            st.write("Subtotal:", rupiah(subtotal))
            st.write("Ongkir simulasi:", rupiah(ongkir))

            st.markdown(
                f"<div style='background:white;padding:20px;"
                f"border-radius:18px;'>"
                f"<div style='color:#526a85;'>TOTAL PEMBAYARAN</div>"
                f"<div style='font-size:30px;font-weight:800;"
                f"color:#176ed0;'>{rupiah(total)}</div></div>",
                unsafe_allow_html=True
            )

            submit_order = st.form_submit_button(
                "💙 Buat Pesanan",
                use_container_width=True
            )

        if submit_order:

            phone = (
                telepon.strip()
                .replace("+", "")
                .replace("-", "")
                .replace(" ", "")
            )

            if not nama.strip() or not telepon.strip() or not alamat.strip():
                st.error("Lengkapi data penerima.")
            elif not phone.isdigit():
                st.error("Nomor telepon tidak valid.")
            elif any(
                qty > products[pid]["stok"]
                for pid, qty in valid_cart.items()
            ):
                st.error("Stok tidak mencukupi. Periksa kembali.")
            else:
                # Kurangi stok setelah validasi
                for pid, qty in valid_cart.items():
                    products[pid]["stok"] -= qty

                order = {
                    "nomor": "BRK-" + uuid.uuid4().hex[:8].upper(),
                    "nama": nama,
                    "telepon": telepon,
                    "alamat": alamat,
                    "kurir": kurir,
                    "metode": metode,
                    "subtotal": subtotal,
                    "ongkir": ongkir,
                    "total": total,
                    "items": dict(valid_cart),
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

    if st.session_state.last_order:
        order = st.session_state.last_order

        st.success("🎉 Pesanan berhasil dibuat!")
        st.subheader("Konfirmasi Pesanan")
        st.write("Nomor:", order["nomor"])
        st.write("Nama:", order["nama"])
        st.write("Total:", rupiah(order["total"]))
        st.info("Status: " + order["status"])
        st.caption("Pembayaran masih simulasi.")

# ==========================================
# PESANAN SAYA
# ==========================================
elif menu == "Pesanan Saya":

    st.title("📦 Pesanan Saya")

    if not st.session_state.orders:
        st.info("Belum ada pesanan.")
    else:
        for order in reversed(st.session_state.orders):

            with st.container(border=True):

                st.subheader("Order " + order["nomor"])
                st.write("Nama:", order["nama"])

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

                st.caption("Status pesanan merupakan simulasi.")

# ==========================================
# FOOTER
# ==========================================
st.sidebar.markdown("---")
st.sidebar.caption("© BARKAS MARKETPLACE")
