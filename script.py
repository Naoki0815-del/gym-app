import streamlit as st
import pandas as pd
from datetime import datetime
import os

# --- 文字だけを確実に大きくする設定 ---
st.markdown("""
    <style>
    /* 全ボタンの文字を巨大にする */
    button p {
        font-size: 50px !important;
        font-weight: bold !important;
        color: white !important;
    }
    /* ボタンの高さを出す */
    div.stButton > button {
        height: 150px !important;
    }
    </style>
    """, unsafe_allow_html=True)

log_file = 'gym_log.csv'

col1, col2 = st.columns(2)

with col1:
    # type="primary" を指定すると、設定に応じた色が付きます
    if st.button("出筋", use_container_width=True, type="primary"):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[now, "出筋"]], columns=["日時", "種別"])
        if os.path.exists(log_file):
            new_data.to_csv(log_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(log_file, index=False)
        st.toast("ジムに来れてすごい！", icon="🔥")

with col2:
    # こちらは標準（白っぽい色）になります
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