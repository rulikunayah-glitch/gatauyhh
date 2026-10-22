
st.markdown("""
<style>
/* BACKGROUND */
.stApp {
    background: linear-gradient(145deg, #eaf4ff 0%, #f7faff 55%, #e4f0ff 100%);
    color: #1b3150;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #163b70, #10294e);
}

[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label {
    padding: 8px 10px;
    border-radius: 10px;
}

/* MAIN HEADINGS */
h1, h2, h3 {
    color: #17365e !important;
    letter-spacing: -0.5px;
}

h1 {
    font-weight: 800 !important;
}

p, label {
    color: #304b6b;
}

/* HERO BANNER */
.hero {
    background: linear-gradient(120deg, #153765, #2779d6);
    padding: 40px;
    border-radius: 26px;
    color: white;
    margin-bottom: 30px;
    box-shadow: 0 12px 30px rgba(35, 101, 180, 0.18);
}

.hero h1 {
    color: white !important;
    font-size: 48px;
    font-weight: 850;
    margin-bottom: 5px;
}

.hero p {
    color: #e3efff;
    font-size: 16px;
}

/* PRODUCT CONTAINERS */
[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,0.96);
    border: 1px solid #dbe9f8 !important;
    border-radius: 22px !important;
    box-shadow: 0 5px 18px rgba(35, 80, 130, 0.07);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

[data-testid="stVerticalBlockBorderWrapper"]:hover {
    box-shadow: 0 10px 26px rgba(35, 80, 130, 0.13);
}

/* PRODUCT NAME & PRICE */
.product-name {
    font-size: 21px;
    font-weight: 800;
    color: #193b67;
    margin-top: 8px;
}

.price {
    color: #176ed0;
    font-size: 27px;
    font-weight: 850;
    margin: 10px 0;
}

.tag {
    display: inline-block;
    background: #e8f2ff;
    color: #2364a5;
    padding: 6px 13px;
    border-radius: 50px;
    font-size: 12px;
    font-weight: 650;
}

/* ALL BUTTONS */
div.stButton > button {
    background: linear-gradient(110deg, #287ce0, #1760bf);
    color: white !important;
    border: 1px solid transparent;
    border-radius: 14px;
    min-height: 46px;
    font-weight: 700;
    letter-spacing: 0.1px;
    box-shadow: 0 5px 12px rgba(31, 104, 198, 0.17);
    transition: all 0.2s ease;
}

div.stButton > button:hover {
    background: linear-gradient(110deg, #155ab3, #103f85);
    color: white !important;
    transform: translateY(-2px);
    box-shadow: 0 8px 18px rgba(31, 104, 198, 0.25);
    border: 1px solid transparent;
}

div.stButton > button:active {
    transform: scale(0.98);
}

/* INPUTS */
div[data-baseweb="input"] > div,
div[data-baseweb="textarea"] > div,
div[data-baseweb="select"] > div {
    background: white;
    border: 1px solid #d4e4f5;
    border-radius: 12px;
}

div[data-baseweb="input"] > div:focus-within,
div[data-baseweb="textarea"] > div:focus-within {
    border-color: #287ce0;
    box-shadow: 0 0 0 2px #287ce022;
}

/* CHECKOUT SUMMARY */
.checkout-box {
    background: white;
    border: 1px solid #dbe9f8;
    padding: 24px;
    border-radius: 22px;
    box-shadow: 0 8px 24px #1b4e8510;
}

.checkout-total {
    color: #176ed0;
    font-size: 30px;
    font-weight: 850;
}

/* METRICS */
[data-testid="stMetric"] {
    background: white;
    border: 1px solid #dbe9f8;
    padding: 20px;
    border-radius: 18px;
}

/* DIVIDER */
hr {
    border-color: #d6e6f7;
}

/* MOBILE */
@media (max-width: 768px) {
    .hero {
        padding: 24px;
    }

    .hero h1 {
        font-size: 36px;
    }

    .block-container {
        padding: 1rem;
    }
}
</style>
""", unsafe_allow_html=True)
