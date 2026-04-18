import streamlit as st
import pandas as pd
from datetime import datetime
import os

# 1画面に収めるための全体設定
st.set_page_config(layout="centered")

# 記録用ファイルの準備
log_file = 'gym_log.csv'

# --- 画面に収まるサイズ感の自作ボタン ---
def big_button(label, color, key):
    button_html = f"""
        <div style="
            background-color: {color};
            height: 140px; /* 高さを少し低く調整 */
            line-height: 140px;
            border-radius: 20px;
            text-align: center;
            margin: 5px 0;
        ">
            <span style="
                color: white;
                font-size: 40px; /* 文字サイズも微調整 */
                font-weight: bold;
                font-family: sans-serif;
            ">{label}</span>
        </div>
    """
    st.markdown(button_html, unsafe_allow_html=True)
    return st.button(f"PUSH {label}", key=key, use_container_width=True)

# 左右のカラム作成（スマホでも横並び強制）
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

# --- 1画面に収めるためのCSS調整 ---
st.markdown("""
    <style>
    /* 1. スマホでも横並びを維持 */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
    }
    [data-testid="column"] {
        width: 50% !important;
        flex: 1 1 50% !important;
        min-width: 50% !important;
    }

    /* 2. 透明ボタンの設定（高さ140pxに合わせる） */
    .stButton button {
        position: relative;
        top: -155px;
        height: 140px !important;
        background-color: transparent !important;
        border: none !important;
        color: transparent !important;
    }

    /* 3. 履歴の位置を限界まで上げる */
    div[data-testid="stVerticalBlock"] > div:nth-child(3) {
        margin-top: -150px !important;
    }
    
    /* 4. 履歴テーブル自体をコンパクトにする */
    div[data-testid="stTable"] {
        font-size: 12px !important;
    }
    h3 {
        font-size: 1.2rem !important;
        margin-bottom: 5px !important;
    }
    
    /* 上下の余計な余白を削る */
    .main .block-container {
        padding-top: 2rem !important;
        padding-bottom: 0rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 履歴表示（件数を3件に絞って高さを節約）
if os.path.exists(log_file):
    st.write("### 最近の記録")
    df = pd.read_csv(log_file)
    st.table(df.tail(3).iloc[::-1]) # 5件→3件に変更