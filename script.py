import streamlit as st
import pandas as pd
from datetime import datetime
import os

# 記録用ファイルの準備
log_file = 'gym_log.csv'

# タイトル
st.write("### 🏋️‍♂️ ジム打刻アプリ")

# 2つのカラムを作成
col1, col2 = st.columns(2)

with col1:
    # 出筋：青い四角の絵文字を付けて、視覚的に青と分からせる
    if st.button("🟦 出筋", use_container_width=True):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[now, "出筋"]], columns=["日時", "種別"])
        if os.path.exists(log_file):
            new_data.to_csv(log_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(log_file, index=False)
        st.toast("ジムに来れてすごい！", icon="🔥")

with col2:
    # 退筋：オレンジの四角（または火）の絵文字を付けて色を分からせる
    if st.button("🟧 退筋", use_container_width=True):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[now, "退筋"]], columns=["日時", "種別"])
        if os.path.exists(log_file):
            new_data.to_csv(log_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(log_file, index=False)
        st.toast("おつかれさま！", icon="✨")

# 履歴表示
if os.path.exists(log_file):
    st.write("---")
    st.write("### 最近の記録")
    df = pd.read_csv(log_file)
    st.table(df.tail(5))