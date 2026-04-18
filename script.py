import streamlit as st
import pandas as pd
from datetime import datetime
import os

# 記録用ファイルの準備
log_file = 'gym_log.csv'

# --- 適切な幅の自作ボタンを生成する関数 ---
def big_button(label, color, key):
    button_html = f"""
        <div style="
            background-color: {color};
            height: 120px; /* 高さを少し抑えてコンパクトに */
            line-height: 120px;
            border-radius: 20px;
            text-align: center;
            margin: 5px auto; /* 中央寄せ */
            width: 80%; /* カラム内での幅を少し絞る */
        ">
            <span style="
                color: white;
                font-size: 30px; /* 幅に合わせて文字も調整 */
                font-weight: bold;
                font-family: sans-serif;
            ">{label}</span>
        </div>
    """
    st.markdown(button_html, unsafe_allow_html=True)
    return st.button(f"PUSH {label}", key=key, use_container_width=True)

# 左右のカラム作成（3列にして、真ん中を使うことで中央寄せにする）
# [1, 2, 1] の比率にすることで、中央の「2」の部分にボタンを配置します
_, col_main, _ = st.columns([0.5, 4, 0.5])

with col_main:
    inner_col1, inner_col2 = st.columns(2)
    with inner_col1:
        if big_button("出筋", "#007bff", "in_btn"):
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_data = pd.DataFrame([[now, "出筋"]], columns=["日時", "種別"])
            if os.path.exists(log_file):
                new_data.to_csv(log_file, mode='a', header=False, index=False)
            else:
                new_data.to_csv(log_file, index=False)
            st.toast("ジムに来れてすごい！", icon="🔥")

    with inner_col2:
        if big_button("退筋", "#ff8c00", "out_btn"):
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_data = pd.DataFrame([[now, "退筋"]], columns=["日時", "種別"])
            if os.path.exists(log_file):
                new_data.to_csv(log_file, mode='a', header=False, index=False)
            else:
                new_data.to_csv(log_file, index=False)
            st.toast("おつかれさま！", icon="✨")

# --- コンパクトに収めるためのCSS調整 ---
st.markdown("""
    <style>
    /* スマホでも横並びを維持 */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
    }

    /* 透明ボタンの設定（高さ120pxに合わせる） */
    .stButton button {
        position: relative;
        top: -130px;
        height: 120px !important;
        background-color: transparent !important;
        border: none !important;
        color: transparent !important;
    }

    /* 履歴の位置を調整 */
    div[data-testid="stVerticalBlock"] > div:nth-child(3) {
        margin-top: -120px !important;
    }
    
    /* 全体的に中央寄せ */
    .main .block-container {
        padding-top: 2rem !important;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 履歴表示
if os.path.exists(log_file):
    st.write("### 最近の記録")
    df = pd.read_csv(log_file)
    st.table(df.tail(3).iloc[::-1])