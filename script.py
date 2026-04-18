import streamlit as st
import pandas as pd
from datetime import datetime
import os

# 記録用ファイルの準備
log_file = 'gym_log.csv'

# --- 2つのボタンを密着させて表示するHTML ---
# ボタン同士の隙間は「margin: 0 5px 0 0」の部分で調整しています
st.markdown("""
    <div style="display: flex; justify-content: flex-start; align-items: flex-start;">
        <div style="background-color: #007bff; width: 140px; height: 120px; line-height: 120px; border-radius: 20px; text-align: center; margin-right: 5px;">
            <span style="color: white; font-size: 30px; font-weight: bold; font-family: sans-serif;">出筋</span>
        </div>
        <div style="background-color: #ff8c00; width: 140px; height: 120px; line-height: 120px; border-radius: 20px; text-align: center;">
            <span style="color: white; font-size: 30px; font-weight: bold; font-family: sans-serif;">退筋</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 透明な本物のボタンを上に並べる ---
col1, col2, _ = st.columns([1, 1, 2], gap="small")

with col1:
    if st.button("PUSH IN", key="in_btn", use_container_width=True):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[now, "出筋"]], columns=["日時", "種別"])
        if os.path.exists(log_file):
            new_data.to_csv(log_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(log_file, index=False)
        st.toast("ジムに来れてすごい！", icon="🔥")

with col2:
    if st.button("PUSH OUT", key="out_btn", use_container_width=True):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[now, "退筋"]], columns=["日時", "種別"])
        if os.path.exists(log_file):
            new_data.to_csv(log_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(log_file, index=False)
        st.toast("おつかれさま！", icon="✨")

# --- レイアウトの強制調整CSS ---
st.markdown("""
    <style>
    /* 1. 透明ボタンをHTMLで作った色の塊の上にピッタリ重ねる */
    .stButton button {
        position: relative;
        top: -130px; /* ボタンの高さ分だけ上に持ち上げる */
        height: 120px !important;
        background-color: transparent !important;
        border: none !important;
        color: transparent !important;
        z-index: 10;
    }

    /* 2. 透明ボタン同士も隙間を詰める */
    [data-testid="stHorizontalBlock"] {
        gap: 0px !important;
        margin-left: 0px !important;
    }
    [data-testid="column"] {
        flex: 0 0 145px !important;
        min-width: 145px !important;
    }

    /* 3. 履歴の位置を調整 */
    div[data-testid="stVerticalBlock"] > div:nth-child(3) {
        margin-top: -120px !important;
    }

    .main .block-container {
        padding-top: 1.5rem !important;
        padding-left: 1rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 履歴表示
if os.path.exists(log_file):
    st.write("### 最近の記録")
    df = pd.read_csv(log_file)
    st.table(df.tail(3).iloc[::-1])