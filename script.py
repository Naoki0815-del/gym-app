import streamlit as st
import pandas as pd
from datetime import datetime
import os

# 記録用ファイルの準備
log_file = 'gym_log.csv'

# タイトル
st.markdown('<h1 class="main-title">ジム打刻アプリ</h1>', unsafe_allow_html=True)

# --- ボタンエリア ---
# カラムの比率を固定して、左側にボタンを密着させます
col1, col2, _ = st.columns([140, 140, 100]) # 140pxずつの幅を確保

with col1:
    # 見た目のボタン
    st.markdown('<div class="btn-box blue">出筋</div>', unsafe_allow_html=True)
    # 透明な判定ボタン
    if st.button("IN", key="btn_in_v5", use_container_width=True):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[now, "出筋"]], columns=["日時", "種別"])
        if os.path.exists(log_file):
            new_data.to_csv(log_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(log_file, index=False)
        st.toast("ジムに来れてすごい！", icon="🔥")

with col2:
    st.markdown('<div class="btn-box orange">退筋</div>', unsafe_allow_html=True)
    if st.button("OUT", key="btn_out_v5", use_container_width=True):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[now, "退筋"]], columns=["日時", "種別"])
        if os.path.exists(log_file):
            new_data.to_csv(log_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(log_file, index=False)
        st.toast("おつかれさま！", icon="✨")

# --- CSS: サイズ固定と密着の徹底 ---
st.markdown("""
    <style>
    /* 1. 全体の配置（横並び強制・隙間最小） */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 5px !important; /* ボタン同士の隙間を5pxに固定 */
        justify-content: flex-start !important;
    }
    
    /* 2. 各カラムの幅を140pxに固定 */
    [data-testid="column"] {
        flex: 0 0 140px !important;
        min-width: 140px !important;
        max-width: 140px !important;
    }

    /* 3. 見た目のボタン（土台） */
    .btn-box {
        width: 140px;
        height: 140px;
        background-color: #007bff;
        border-radius: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 32px;
        font-weight: bold;
        position: absolute;
        z-index: 1;
        pointer-events: none;
    }
    .blue { background-color: #007bff; }
    .orange { background-color: #ff8c00; }

    /* 4. 透明ボタン（判定役）：サイズを土台に完全一致させる */
    .stButton button {
        width: 140px !important;
        height: 140px !important;
        background-color: transparent !important;
        border: none !important;
        color: transparent !important;
        position: relative;
        z-index: 2;
        margin: 0 !important;
        padding: 0 !important;
    }

    /* 5. 履歴の位置とタイトル */
    .main-title { font-size: 24px !important; margin-bottom: 5px !important; }
    div[data-testid="stVerticalBlock"] > div:nth-child(4) {
        margin-top: 10px !important;
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