import streamlit as st
import pandas as pd
from datetime import datetime
import os

# 記録用ファイルの準備
log_file = 'gym_log.csv'

# --- 巨大な自作ボタンを生成する関数 ---
def big_button(label, color, key):
    button_html = f"""
        <div style="
            background-color: {color};
            height: 180px;
            line-height: 180px;
            border-radius: 25px;
            text-align: center;
            margin: 5px 0;
        ">
            <span style="
                color: white;
                font-size: 45px;
                font-weight: bold;
                font-family: sans-serif;
            ">{label}</span>
        </div>
    """
    st.markdown(button_html, unsafe_allow_html=True)
    return st.button(f"PUSH {label}", key=key, use_container_width=True)

# --- 左右のカラム作成 ---
# gapを最小にして、スマホでも横に並びやすくします
col1, col2 = st.columns(2, gap="small")

with col1:
    if big_button("出筋", "#007bff", "in_btn"):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[now, "出筋"]], columns=["日時", "種別"])
        if os.path.exists(log_file):
            new_data.to_csv(log_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(log_file, index=False)
        st.toast("ジムに来れてすごい！", icon="🔥")

with col2:
    if big_button("退筋", "#ff8c00", "out_btn"):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[now, "退筋"]], columns=["日時", "種別"])
        if os.path.exists(log_file):
            new_data.to_csv(log_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(log_file, index=False)
        st.toast("おつかれさま！", icon="✨")

# --- スマホでも横並びを維持するCSS ---
st.markdown("""
    <style>
    /* 1. カラムの親要素を「折り返し禁止」にする */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        align-items: flex-start !important;
    }
    
    /* 2. 各カラムが50%ずつ幅をとるように固定 */
    [data-testid="column"] {
        width: 50% !important;
        flex: 1 1 50% !important;
        min-width: 50% !important;
    }

    /* 3. 透明ボタンの設定 */
    .stButton button {
        position: relative;
        top: -200px; /* ボタンの高さに合わせて少し調整 */
        height: 180px !important;
        background-color: transparent !important;
        border: none !important;
        color: transparent !important;
    }

    /* 4. 見出しの位置調整 */
    div[data-testid="stVerticalBlock"] > div:nth-child(3) {
        margin-top: -190px !important;
        margin-bottom: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 履歴表示
if os.path.exists(log_file):
    st.write("### 最近の記録")
    df = pd.read_csv(log_file)
    st.table(df.tail(5).iloc[::-1])