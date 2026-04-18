import streamlit as st
import pandas as pd
from datetime import datetime
import os

# 記録用ファイルの準備
log_file = 'gym_log.csv'

# タイトル
st.markdown('<h1 class="main-title">ジム打刻アプリ</h1>', unsafe_allow_html=True)

# --- 左右のカラムを定義 ---
# ボタン同士を密着させるため gap="none" に近い設定をCSSで行います
col1, col2, _ = st.columns([1, 1, 0.1])

with col1:
    # 見た目のボタン（出筋）
    st.markdown("""
        <div class="btn-box blue">
            <span>出筋</span>
        </div>
        """, unsafe_allow_html=True)
    # 本物のボタン
    if st.button("IN", key="in_final", use_container_width=True):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[now, "出筋"]], columns=["日時", "種別"])
        if os.path.exists(log_file):
            new_data.to_csv(log_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(log_file, index=False)
        st.toast("ジムに来れてすごい！", icon="🔥")

with col2:
    # 見た目のボタン（退筋）
    st.markdown("""
        <div class="btn-box orange">
            <span>退筋</span>
        </div>
        """, unsafe_allow_html=True)
    # 本物のボタン
    if st.button("OUT", key="out_final", use_container_width=True):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[now, "退筋"]], columns=["日時", "種別"])
        if os.path.exists(log_file):
            new_data.to_csv(log_file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(log_file, index=False)
        st.toast("おつかれさま！", icon="✨")

# --- レイアウトをミリ単位で整えるCSS ---
st.markdown("""
    <style>
    /* 1. タイトル周りの調整 */
    .main-title { font-size: 28px !important; margin-bottom: 5px !important; }

    /* 2. 見た目ボタンの共通設定 */
    .btn-box {
        width: 175px;
        height: 180px;
        line-height: 180px;
        border-radius: 30px;
        text-align: center;
        position: absolute; /* カラム内で浮かせない */
    }
    .blue { background-color: #007bff; }
    .orange { background-color: #ff8c00; }
    .btn-box span { color: white; font-size: 45px; font-weight: bold; font-family: sans-serif; }

    /* 3. 透明ボタンをそれぞれの「btn-box」の上にピッタリ重ねる */
    .stButton button {
        position: relative;
        width: 175px !important;
        height: 180px !important;
        background-color: transparent !important;
        border: none !important;
        color: transparent !important;
        z-index: 100;
        margin: 0 !important;
    }

    /* 4. カラム同士を密着させる（隙間ゼロ） */
    [data-testid="stHorizontalBlock"] { gap: 0px !important; }
    [data-testid="column"] {
        flex: 0 0 175px !important;
        min-width: 175px !important;
        padding-right: 2px !important; /* わずかなボタン間の隙間 */
    }

    /* 5. 履歴（最近の記録）の位置調整 */
    div[data-testid="stVerticalBlock"] > div:nth-child(4) {
        margin-top: 10px !important; /* ボタンが絶対配置に近いので、ここは敢えて少し空ける */
    }

    /* 6. 全体の余白カット */
    .main .block-container {
        padding-top: 1.5rem !important;
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 履歴表示
if os.path.exists(log_file):
    st.write("### 最近の記録")
    df = pd.read_csv(log_file)
    st.table(df.tail(3).iloc[::-1])