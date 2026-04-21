import streamlit as st
import pandas as pd
from datetime import datetime
import os

# 記録用ファイルの準備
log_file = 'gym_log.csv'

# --- タイトル表示 ---
st.markdown('<h1 class="main-title">ジム打刻アプリ</h1>', unsafe_allow_html=True)

# --- 【背景】巨大ボタンを描画するHTML ---
st.markdown("""
    <div style="display: flex; justify-content: flex-start; align-items: flex-start;">
        <div style="background-color: #007bff; width: 185px; height: 180px; line-height: 180px; border-radius: 30px; text-align: center; margin-right: 4px;">
            <span style="color: white; font-size: 45px; font-weight: bold; font-family: sans-serif;">出筋</span>
        </div>
        <div style="background-color: #ff8c00; width: 185px; height: 180px; line-height: 180px; border-radius: 30px; text-align: center;">
            <span style="color: white; font-size: 45px; font-weight: bold; font-family: sans-serif;">退筋</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 【判定用】透明なボタン ---
col1, col2, _ = st.columns([1, 1, 0.1], gap="small")

with col1:
    if st.button("PUSH IN", key="in_btn", use_container_width=True):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[now, "出筋"]], columns=["日時", "種別"])
        if os.path.exists(log_file):
            new_data.to_csv(log_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(log_file, index=False)

with col2:
    if st.button("PUSH OUT", key="out_btn", use_container_width=True):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[now, "退筋"]], columns=["日時", "種別"])
        if os.path.exists(log_file):
            new_data.to_csv(log_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(log_file, index=False)

# --- レイアウト強制調整 & クリック反応強化CSS ---
st.markdown("""
    <style>
    /* 1. 基本レイアウト */
    .main-title { font-size: 28px !important; font-weight: bold !important; margin-bottom: 10px !important; color: #31333F; }
    
    /* 2. ボタンを透明化し、サイズを固定 */
    .stButton button {
        position: relative;
        top: -190px;
        height: 180px !important;
        background-color: transparent !important;
        border: none !important;
        color: transparent !important;
        z-index: 10;
        box-shadow: none !important;
    }

    /* 3. 【重要】クリックした瞬間の色（灰色）を強制 */
    /* active（クリック中）と focus（クリック直後）の両方に適用 */
    .stButton button:active, .stButton button:focus {
        background-color: rgba(0, 0, 0, 0.3) !important; /* 黒の透過（灰色に見える） */
        border-radius: 30px !important;
        transition: none !important;
    }

    /* 4. マウスが乗った時のStreamlit標準枠を消す */
    .stButton button:hover {
        border: none !important;
        color: transparent !important;
        background-color: rgba(255, 255, 255, 0.1) !important;
    }

    /* 5. カラム幅の維持 */
    [data-testid="stHorizontalBlock"] { gap: 0px !important; }
    [data-testid="column"] { flex: 0 0 188px !important; min-width: 188px !important; }

    /* 6. 履歴の位置調整 */
    div[data-testid="stVerticalBlock"] > div:nth-child(4) { margin-top: -180px !important; }

    /* 7. 全体の余白 */
    .main .block-container { padding-top: 1.5rem !important; padding-left: 0.5rem !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 履歴表示 ---
if os.path.exists(log_file):
    st.write("### 最近の記録")
    df = pd.read_csv(log_file)
    st.table(df.tail(3).iloc[::-1])