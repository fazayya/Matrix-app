import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------
st.set_page_config(page_title="Matrix App", layout="wide")

# ------------------------------------------------------------
# BACKGROUND (Math Blur Image)
# ------------------------------------------------------------
st.markdown("""
<style>
    body { margin: 0; padding: 0; }

    /* Background image with blur + dark overlay */
    .main-bg {
        background-image: url('https://i.imgur.com/5VxD3s8.jpeg');
        background-size: cover;
        background-position: center;
        filter: blur(3px);
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        z-index: -1;
    }

    .content-wrapper {
        backdrop-filter: blur(10px);
        padding: 25px;
        border-radius: 15px;
    }

    h1, h2, h3, p, label {
        color: #ffffff !important;
        font-family: 'Poppins', sans-serif;
    }

    /* Smaller font for language + upload */
    .small-text {
        font-size: 14px !important;
    }
</style>
<div class='main-bg'></div>
""", unsafe_allow_html=True)


# ------------------------------------------------------------
# LANGUAGE
# ------------------------------------------------------------
st.markdown("### <span class='small-text'>Language:</span>", unsafe_allow_html=True)

lang = st.selectbox(
    "",
    ["🇮🇩 Indonesia (ID)", "🇬🇧 English (EN)", "🇨🇳 中文 (ZH)"]
)

T = {
    "WELCOME": {
        "🇮🇩 Indonesia (ID)": "SELAMAT DATANG!",
        "🇬🇧 English (EN)": "WELCOME!",
        "🇨🇳 中文 (ZH)": "欢迎！"
    },
    "SUB": {
        "🇮🇩 Indonesia (ID)": "di aplikasi matriks.",
        "🇬🇧 English (EN)": "in matrix application.",
        "🇨🇳 中文 (ZH)": "矩阵应用程序中。"
    },
    "UPLOAD": {
        "🇮🇩 Indonesia (ID)": "Unggah file Excel survei Anda:",
        "🇬🇧 English (EN)": "Upload your survey Excel file in here:",
        "🇨🇳 中文 (ZH)": "上传您的 Excel 调查文件："
    },
    "FEATURES": {
        "🇮🇩 Indonesia (ID)": "Fitur Kami:",
        "🇬🇧 English (EN)": "The Features:",
        "🇨🇳 中文 (ZH)": "功能："
    },
    "THANKS": {
        "🇮🇩 Indonesia (ID)": "TERIMA KASIH! sampai jumpa lagi :)",
        "🇬🇧 English (EN)": "THANK YOU! see you next time :)",
        "🇨🇳 中文 (ZH)": "谢谢你！下次见 :)"
    }
}


# ------------------------------------------------------------
# CONTENT WRAPPER
# ------------------------------------------------------------
st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)

# TITLE
st.markdown(
    f"<h1 style='text-align:center;'>{T['WELCOME'][lang]}</h1>",
    unsafe_allow_html=True
)
st.markdown(
    f"<p style='text-align:center; font-size:18px;'>{T['SUB'][lang]}</p>",
    unsafe_allow_html=True
)


# UPLOAD (smaller font)
st.markdown(f"<p class='small-text'>{T['UPLOAD'][lang]}</p>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["xlsx", "xls"])

df = None
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.success("File uploaded successfully!")
    st.dataframe(df)


# ------------------------------------------------------------
# FEATURES SLIDER — FIXED + DRAGGABLE
# ------------------------------------------------------------
st.markdown(
    f"<h3 style='text-align:center; margin-top:30px;'>{T['FEATURES'][lang]}</h3>",
    unsafe_allow_html=True
)

swiper_html = """
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />

<style>
.feature-card {
    background: rgba(255,255,255,0.14);
    border-radius: 18px;
    height: 140px;
    padding-top: 50px;
    cursor: pointer;
    text-align: center;
    transition: 0.25s;
    color: white;
    border: 1px solid rgba(255,255,255,0.25);
}
.feature-card:hover {
    background: rgba(255,255,255,0.24);
    transform: scale(1.06);
}
</style>

<div class="swiper" style="width:100%; height:220px;">
    <div class="swiper-wrapper">

        <div class="swiper-slide">
            <div class="feature-card" onclick="window.location.href='?page=desc'">
                <h3>📊 Descriptive Analysis</h3>
            </div>
        </div>

        <div class="swiper-slide">
            <div class="feature-card" onclick="window.location.href='?page=charts'">
                <h3>📈 Virtual Charts</h3>
            </div>
        </div>

        <div class="swiper-slide">
            <div class="feature-card" onclick="window.location.href='?page=corr'">
                <h3>🔗 Correlation Analysis</h3>
            </div>
        </div>

    </div>

    <div class="swiper-pagination"></div>
</div>

<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>

<script>
  const swiper = new Swiper('.swiper', {
    slidesPerView: 3,
    spaceBetween: 22,
    centeredSlides: true,
    loop: true,
    grabCursor: true,
    allowTouchMove: true,
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
  });
</script>
"""

components.html(swiper_html, height=260, scrolling=False)


# FOOTER
st.markdown(
    f"<p style='text-align:center; margin-top:40px; font-size:17px;'>{T['THANKS'][lang]}</p>",
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)