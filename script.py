import streamlit as st
import pandas as pd
from datetime import datetime
import os

# --- 強制的・絶対的に色を固定する魔法のコード (CSS) ---
st.markdown("""
    <style>
    /* ボタン全体の枠組みを強制固定 */
    div.stButton > button {
        height: 180px !important;
        border-radius: 25px !important;
        border: none !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    
    /* ボタンの中の文字を、どんな状態でも「白・極大」に固定 */
    div.stButton > button div, 
    div.stButton > button p,
    div.stButton > button span {
        font-size: 60px !important;
        font-weight: bold !important;
        color: #FFFFFF !important; /* 絶対に白 */
        opacity: 1 !important;     /* 透明度をゼロに */
    }
    
    /* 出筋（左）：絶対に青 */
    div[data-testid="column"]:nth-of-type(1) button {
        background-color: #007bff !important;
    }
    
    /* 退筋（右）：絶対にオレンジ */
    div[data-testid="column"]:nth-of-type(2) button {
        background-color: #ff8c00 !important;
    }

    /* カーソルを合わせても、クリックしても色を変えない設定 */
    div.stButton > button:hover, 
    div.stButton > button:active, 
    div.stButton > button:focus {
        color: #FFFFFF !important;
        border: none !important;
        outline: none !important;
    }
    </style>
    """, unsafe_allow_html=True)
# ------------------------------------------

log_file = 'gym_log.csv'

col1, col2 = st.columns(2)

with col1:
    if st.button("出筋", use_container_width=True):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[now, "出筋"]], columns=["日時", "種別"])
        if os.path.exists(log_file):
            new_data.to_csv(log_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(log_file, index=False)
        st.toast("ジムに来れてすごい！", icon="🔥")

with col2:
    if st.button("退筋", use_container_width=True):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[now, "退筋"]], columns=["日時", "種別"])
        if os.path.exists(log_file):
            new_data.to_csv(log_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(log_file, index=False)
        st.toast("おつかれさま！", icon="✨")

if os.path.exists(log_file):
    st.write("### 最近の記録")
    df = pd.read_csv(log_file)
    st.table(df.tail(5))