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
            height: 200px;
            line-height: 200px;
            border-radius: 25px;
            text-align: center;
            margin: 10px 0;
        ">
            <span style="
                color: white;
                font-size: 60px;
                font-weight: bold;
                font-family: sans-serif;
            ">{label}</span>
        </div>
    """
    st.markdown(button_html, unsafe_allow_html=True)
    return st.button(f"PUSH {label}", key=key, use_container_width=True)

# 左右のカラム作成
col1, col2 = st.columns(2)

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

# --- 重なりを解消し、位置を整えるCSS ---
st.markdown("""
    <style>
    /* 1. 透明ボタンの設定 */
    .stButton button {
        position: relative;
        top: -220px;
        height: 200px !important;
        background-color: transparent !important;
        border: none !important;
        color: transparent !important;
    }

    /* 2. 「最近の記録」見出しだけを上に持ち上げる */
    div[data-testid="stVerticalBlock"] > div:nth-child(3) {
        margin-top: -210px !important; /* ボタンとの距離感 */
        margin-bottom: 10px !important; /* 下のテーブルとの隙間を確保 */
    }

    /* 3. テーブル（4番目の要素）は持ち上げすぎない */
    div[data-testid="stVerticalBlock"] > div:nth-child(4) {
        margin-top: 0px !important;
    }
    
    /* 見出し自体の余白をリセット */
    h3 {
        padding-bottom: 5px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 履歴表示
if os.path.exists(log_file):
    st.write("### 最近の記録")
    df = pd.read_csv(log_file)
    st.table(df.tail(5).iloc[::-1])