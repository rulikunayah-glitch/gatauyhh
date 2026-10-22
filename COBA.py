
import streamlit as st

st.set_page_config(page_title="Wear Reworn", page_icon="🛍️")

st.title("WEAR REWORN")
st.caption("Little finds, carefully chosen")

# Data produk
produk = {
    "Korean Cardigan": {
        "harga": 85000,
        "ukuran": "M",
        "kondisi": "Preloved - Good Condition",
        "stok": 5
    },
    "Vintage Denim Skirt": {
        "harga": 55000,
        "ukuran": "S",
        "kondisi": "Preloved - Very Good",
        "stok": 3
    },
    "Basic Tanktop": {
        "harga": 25000,
        "ukuran": "All Size",
        "kondisi": "Preloved - Good Condition",
        "stok": 8
    }
}

if "cart" not in st.session_state:
    st.session_state.cart = {}

def rupiah(n):
    return f"Rp{n:,}".replace(",", ".")

menu = st.sidebar.radio(
    "Menu",
    ["Beranda", "Keranjang", "Checkout"]
)

# BERANDA
if menu == "Beranda":
    st.header("Katalog Produk")

    for nama, p in produk.items():
        with st.container(border=True):
            st.subheader(nama)
            st.write("Harga:", rupiah(p["harga"]))
            st.write("Ukuran:", p["ukuran"])
            st.write("Kondisi:", p["kondisi"])
            st.write("Stok:", p["stok"])

            jumlah = st.number_input(
                f"Jumlah - {nama}",
                min_value=1,
                max_value=p["stok"],
                value=1,
                key=nama
            )

            if st.button("Tambah ke Keranjang", key="add_" + nama):
                qty = st.session_state.cart.get(nama, 0)

                if qty + jumlah <= p["stok"]:
                    st.session_state.cart[nama] = qty + jumlah
                    st.success("Produk ditambahkan!")
                else:
                    st.error("Stok tidak mencukupi.")

# KERANJANG
elif menu == "Keranjang":
    st.header("Keranjang Belanja")

    cart = st.session_state.cart

    if not cart:
        st.info("Keranjang masih kosong.")
    else:
        total = 0

        for nama, qty in list(cart.items()):
            subtotal = produk[nama]["harga"] * qty
            total += subtotal

            st.write(f"**{nama}** x{qty}")
            st.write("Subtotal:", rupiah(subtotal))

            if st.button("Hapus", key="del_" + nama):
                del st.session_state.cart[nama]
                st.rerun()

        st.divider()
        st.subheader("Total: " + rupiah(total))

# CHECKOUT
else:
    st.header("Checkout")

    cart = st.session_state.cart

    if not cart:
        st.info("Keranjang masih kosong.")
    else:
        subtotal = sum(
            produk[nama]["harga"] * qty
            for nama, qty in cart.items()
        )

        st.write("Subtotal:", rupiah(subtotal))

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

        st.write("Ongkir (simulasi):", rupiah(ongkir))
        st.subheader("Total:", rupiah(subtotal + ongkir))

        if st.button("Buat Pesanan"):
            if not nama_pembeli.strip() or not telepon.strip() or not alamat.strip():
                st.error("Lengkapi semua data pembeli.")
            elif not telepon.strip().replace("+", "").replace("-", "").replace(" ", "").isdigit():
                st.error("Nomor telepon tidak valid.")
            elif any(
                qty > produk[nama]["stok"]
                for nama, qty in cart.items()
            ):
                st.error("Stok tidak mencukupi.")
            else:
                # Validasi dan kurangi stok
                for nama, qty in cart.items():
                    produk[nama]["stok"] -= qty

                st.success("Pesanan berhasil dibuat!")

                st.write("Nama:", nama_pembeli)
                st.write("Alamat:", alamat)
                st.write("Nomor Telepon:", telepon)
                st.write("Pembayaran:", metode)
                st.write("Total:", rupiah(subtotal + ongkir))

                if metode == "COD":
                    st.info("Status: Menunggu Konfirmasi")
                else:
                    st.info("Status: Menunggu Pembayaran (Simulasi)")

                st.session_state.cart = {}
