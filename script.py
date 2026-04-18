import streamlit as st
import pandas as pd
from datetime import datetime
import os

# 記録用ファイルの準備
log_file = 'gym_log.csv'

# タイトル
st.markdown('<h1 class="main-title">ジム打刻アプリ</h1>', unsafe_allow_html=True)

# --- ボタンエリア ---
# カラムの幅をボタンサイズ（140px）にピッタリ合わせます
col1, col2, _ = st.columns([140, 140, 50]) 

with col1:
    # 見た目のボタン
    st.markdown('<div class="btn-box blue">出筋</div>', unsafe_allow_html=True)
    # 透明な判定ボタン
    if st.button("IN", key="btn_in_final_fixed", use_container_width=True):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[now, "出筋"]], columns=["日時", "種別"])
        if os.path.exists(log_file):
            new_data.to_csv(log_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(log_file, index=False)
        st.toast("ジムに来れてすごい！", icon="🔥")

with col2:
    st.markdown('<div class="btn-box orange">退筋</div>', unsafe_allow_html=True)
    if st.button("OUT", key="btn_out_final_fixed", use_container_width=True):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[now, "退筋"]], columns=["日時", "種別"])
        if os.path.exists(log_file):
            new_data.to_csv(log_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(log_file, index=False)
        st.toast("おつかれさま！", icon="✨")

# --- CSS: 限界まで密着させる設定 ---
st.markdown("""
    <style>
    /* 1. タイトル */
    .main-title { font-size: 24px !important; margin-bottom: 5px !important; }

    /* 2. カラム同士の隙間を1pxまで縮小 */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 1px !important; /* 5pxから1pxに短縮 */
        justify-content: flex-start !important;
    }
    
    /* 3. 各カラムの幅を固定 */
    [data-testid="column"] {
        flex: 0 0 140px !important;
        min-width: 140px !important;
        max-width: 140px !important;
    }

    /* 4. 見た目のボタン（土台） */
    .btn-box {
        width: 140px;
        height: 140px;
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

    /* 5. 透明ボタン（判定役） */
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

    /* 6. 履歴の位置 */
    div[data-testid="stVerticalBlock"] > div:nth-child(4) {
        margin-top: 15px !important;
    }
    
    .main .block-container {
        padding: 1rem 0.5rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 履歴表示
if os.path.exists(log_file):
    st.write("### 最近の記録")
    df = pd.read_csv(log_file)
    st.table(df.tail(3).iloc[::-1])