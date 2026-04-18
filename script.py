import streamlit as st
import pandas as pd
from datetime import datetime
import os

# データの保存先設定
DB_FILE = 'gym_log.csv'

st.title("💪 Gym Check-in")

# ボタンを横並びにする
col1, col2 = st.columns(2)

with col1:
    if st.button('🏁 出勤 (入館)', use_container_width=True):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_data = pd.DataFrame([[now, '入館']], columns=['日時', '区分'])
        new_data.to_csv(DB_FILE, mode='a', header=not os.path.exists(DB_FILE), index=False)
        st.success(f"入館記録完了！\n{now}")

with col2:
    if st.button('🏠 退勤 (退館)', use_container_width=True):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_data = pd.DataFrame([[now, '退館']], columns=['日時', '区分'])
        new_data.to_csv(DB_FILE, mode='a', header=not os.path.exists(DB_FILE), index=False)
        st.info(f"退館記録完了！\n{now}")

# 履歴の表示
st.subheader("📊 最近の記録")
if os.path.exists(DB_FILE):
    df = pd.read_csv(DB_FILE)
    st.dataframe(df.tail(10), use_container_width=True)