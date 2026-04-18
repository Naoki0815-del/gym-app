import streamlit as st
import pandas as pd
from datetime import datetime
import os

# 記録用ファイルの準備
log_file = 'gym_log.csv'

# タイトル
st.title("ジム打刻アプリ")

# --- ボタンエリア（HTMLとStreamlitボタンの完全同期） ---
# st.columnsを使わず、CSSで横並びを制御します
col1, col2 = st.columns(2)

with col1:
    # 1. 見た目の青い箱
    st.markdown('<div class="custom-btn blue">出筋</div>', unsafe_allow_html=True)
    # 2. その上に透明ボタンを重ねる
    if st.button("IN", key="btn_in_final", use_container_width=True):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[now, "出筋"]], columns=["日時", "種別"])
        if os.path.exists(log_file):
            new_data.to_csv(log_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(log_file, index=False)
        st.toast("ジムに来れてすごい！", icon="🔥")

with col2:
    # 1. 見た目のオレンジの箱
    st.markdown('<div class="custom-btn orange">退筋</div>', unsafe_allow_html=True)
    # 2. その上に透明ボタンを重ねる
    if st.button("OUT", key="btn_out_final", use_container_width=True):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[now, "退筋"]], columns=["日時", "種別"])
        if os.path.exists(log_file):
            new_data.to_csv(log_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(log_file, index=False)
        st.toast("おつかれさま！", icon="✨")

# --- CSS: 判定のズレを物理的にゼロにする ---
st.markdown("""
    <style>
    /* 1. カラムの横並びを強制（スマホ対応） */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 8px !important;
    }
    [data-testid="column"] {
        flex: 1 !important;
        min-width: 0 !important;
    }

    /* 2. 見た目のボタン（土台） */
    .custom-btn {
        height: 160px;
        border-radius: 25px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 40px;
        font-weight: bold;
        position: absolute; /* カラム内で基準にする */
        width: calc(100% - 16px); /* カラム幅に合わせる */
        z-index: 1;
        pointer-events: none; /* 下の透明ボタンにクリックを通す */
    }
    .blue { background-color: #007bff; }
    .orange { background-color: #ff8c00; }

    /* 3. 透明な本物のボタン（判定役） */
    .stButton button {
        height: 160px !important;
        background-color: transparent !important;
        border: none !important;
        color: transparent !important;
        position: relative;
        z-index: 2; /* 土台より上に配置 */
        margin: 0 !important;
    }

    /* 4. 最近の記録の位置調整 */
    div[data-testid="stVerticalBlock"] > div:nth-child(4) {
        margin-top: 10px !important;
    }
    
    /* 5. 全体の余白 */
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