import streamlit as st
import pandas as pd
from datetime import datetime
import os

# 記録用ファイルの準備
log_file = 'gym_log.csv'

# タイトル
st.markdown('<h1 class="main-title">ジム打刻アプリ</h1>', unsafe_allow_html=True)

# --- ボタンエリア ---
# [1, 1, 2] の比率にすることで、左側にボタンを寄せ、右側を空けます
col1, col2, _ = st.columns([1, 1, 2], gap="small")

with col1:
    # 見た目と判定を一体化するためのコンテナ
    st.markdown('<div class="btn-container blue">出筋</div>', unsafe_allow_html=True)
    if st.button("IN", key="btn_in_v4", use_container_width=True):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[now, "出筋"]], columns=["日時", "種別"])
        if os.path.exists(log_file):
            new_data.to_csv(log_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(log_file, index=False)
        st.toast("ジムに来れてすごい！", icon="🔥")

with col2:
    st.markdown('<div class="btn-container orange">退筋</div>', unsafe_allow_html=True)
    if st.button("OUT", key="btn_out_v4", use_container_width=True):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[now, "退筋"]], columns=["日時", "種別"])
        if os.path.exists(log_file):
            new_data.to_csv(log_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(log_file, index=False)
        st.toast("おつかれさま！", icon="✨")

# --- レイアウトと判定の同期CSS ---
st.markdown("""
    <style>
    /* 1. タイトル */
    .main-title { font-size: 24px !important; margin-bottom: 10px !important; }

    /* 2. スマホでも横並びを死守 */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        justify-content: flex-start !important;
        gap: 5px !important;
    }
    /* ボタンの幅を画面の約25%（4分の1）程度に絞る */
    [data-testid="column"] {
        flex: 0 0 85px !important;
        min-width: 85px !important;
    }

    /* 3. 見た目のボタン（土台）*/
    .btn-container {
        height: 100px; /* 高さを抑えてコンパクトに */
        border-radius: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 22px; /* 小さくなった幅に合わせて文字も調整 */
        font-weight: bold;
        position: absolute;
        width: 85px;
        z-index: 1;
        pointer-events: none; /* クリックを透明ボタンに透過させる */
    }
    .blue { background-color: #007bff; }
    .orange { background-color: #ff8c00; }

    /* 4. 透明ボタン（判定役）：土台とサイズを完全に一致させる */
    .stButton button {
        height: 100px !important;
        width: 85px !important;
        background-color: transparent !important;
        border: none !important;
        color: transparent !important;
        position: relative;
        z-index: 2;
        margin: 0 !important;
        padding: 0 !important;
    }

    /* 5. 履歴の位置を調整 */
    div[data-testid="stVerticalBlock"] > div:nth-child(4) {
        margin-top: 20px !important;
    }
    
    .main .block-container {
        padding: 1.5rem 0.5rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 履歴表示
if os.path.exists(log_file):
    st.write("### 最近の記録")
    df = pd.read_csv(log_file)
    st.table(df.tail(3).iloc[::-1])