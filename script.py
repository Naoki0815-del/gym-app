import streamlit as st
import pandas as pd
from datetime import datetime
import os

# 記録用ファイルの準備
log_file = 'gym_log.csv'

# タイトル
st.markdown('<h1 class="main-title">ジム打刻アプリ</h1>', unsafe_allow_html=True)

# --- ボタンエリア ---
# st.columnsを使わず、一つの箱の中に2つのボタンを配置することで折り返しを絶対阻止します
st.markdown("""
    <div class="button-container">
        <div class="btn-wrapper">
            <div class="btn-box blue"><span>出筋</span></div>
            <div id="btn-in"></div>
        </div>
        <div class="btn-wrapper">
            <div class="btn-box orange"><span>退筋</span></div>
            <div id="btn-out"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 透明ボタンの設置（ここも横並びを強制）
col_btn1, col_btn2, _ = st.columns([1, 1, 0.01], gap="small")

with col_btn1:
    if st.button("IN", key="in_final_v3", use_container_width=True):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[now, "出筋"]], columns=["日時", "種別"])
        if os.path.exists(log_file):
            new_data.to_csv(log_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(log_file, index=False)
        st.toast("ジムに来れてすごい！", icon="🔥")

with col_btn2:
    if st.button("OUT", key="out_final_v3", use_container_width=True):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[now, "退筋"]], columns=["日時", "種別"])
        if os.path.exists(log_file):
            new_data.to_csv(log_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(log_file, index=False)
        st.toast("おつかれさま！", icon="✨")

# --- レイアウト強制固定CSS ---
st.markdown("""
    <style>
    /* 1. タイトル */
    .main-title { font-size: 24px !important; margin-bottom: 0px !important; }

    /* 2. ボタンコンテナ：絶対に横並び、はみ出しは縮小 */
    .button-container {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        justify-content: flex-start;
        width: 100%;
        margin-bottom: 0px;
    }
    .btn-wrapper {
        position: relative;
        flex: 0 0 48%; /* 画面幅の約半分に固定 */
        max-width: 180px;
        height: 160px;
        margin-right: 4px;
    }

    /* 3. 見た目のデザイン */
    .btn-box {
        width: 100%;
        height: 100%;
        border-radius: 25px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .blue { background-color: #007bff; }
    .orange { background-color: #ff8c00; }
    .btn-box span { color: white; font-size: 38px; font-weight: bold; }

    /* 4. 透明ボタンの重ね合わせ（ここが重要） */
    [data-testid="stHorizontalBlock"] {
        position: relative;
        top: -160px; /* ボタンの高さ分だけ上に持ち上げる */
        margin-bottom: -160px; /* 後続要素への影響を消す */
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 4px !important;
    }
    
    .stButton button {
        height: 160px !important;
        background-color: transparent !important;
        border: none !important;
        color: transparent !important;
        z-index: 10;
    }

    /* 5. 履歴の位置 */
    div[data-testid="stVerticalBlock"] > div:nth-child(4) {
        margin-top: 10px !important;
    }

    /* 全体の余白 */
    .main .block-container {
        padding-top: 1rem !important;
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 履歴表示
if os.path.exists(log_file):
    st.write("### 最近の記録")
    df = pd.read_csv(log_file)
    st.table(df.tail(3).iloc[::-1])