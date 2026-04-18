import streamlit as st
import pandas as pd
from datetime import datetime
import os

# 記録用ファイルの準備
log_file = 'gym_log.csv'

# --- コンパクトな自作ボタンを生成する関数 ---
def big_button(label, color, key):
    button_html = f"""
        <div style="
            background-color: {color};
            height: 120px;
            line-height: 120px;
            border-radius: 20px;
            text-align: center;
            margin: 5px 0;
            width: 140px; /* ボタンの横幅を固定してコンパクトに */
        ">
            <span style="
                color: white;
                font-size: 30px;
                font-weight: bold;
                font-family: sans-serif;
            ">{label}</span>
        </div>
    """
    st.markdown(button_html, unsafe_allow_html=True)
    return st.button(f"PUSH {label}", key=key)

# カラムを作成（左側に寄せるため、右側に大きな空きスペースを作る）
# [2, 2, 5] の比率で、左側2つにボタンを配置します
col1, col2, _ = st.columns([1, 1, 2])

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

# --- 左寄せとレイアウトの微調整 ---
st.markdown("""
    <style>
    /* 1. スマホでも横並びを維持し、左に寄せる */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        justify-content: flex-start !important;
    }
    
    /* 各カラムの幅をボタンに合わせて固定 */
    [data-testid="column"] {
        width: 150px !important;
        flex: 0 0 150px !important;
        min-width: 150px !important;
    }

    /* 2. 透明ボタンの設定（幅140px、高さ120pxに合わせる） */
    .stButton button {
        position: relative;
        top: -130px;
        width: 140px !important;
        height: 120px !important;
        background-color: transparent !important;
        border: none !important;
        color: transparent !important;
    }

    /* 3. 履歴の位置を調整 */
    div[data-testid="stVerticalBlock"] > div:nth-child(3) {
        margin-top: -120px !important;
    }
    
    /* 4. 全体的な余白調整 */
    .main .block-container {
        padding-top: 1.5rem !important;
        margin-left: 0 !important;
        text-align: left !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 履歴表示
if os.path.exists(log_file):
    st.write("### 最近の記録")
    df = pd.read_csv(log_file)
    st.table(df.tail(3).iloc[::-1])