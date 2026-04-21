import streamlit as st
import pandas as pd
from datetime import datetime
import os

# ファイル設定
log_file = 'gym_log.csv'

# --- 1. サーバー側の記録処理 ---
# 隠しテキスト入力を使って、JavaScriptからデータを受け取ります
if 'record_trigger' not in st.session_state:
    st.session_state.record_trigger = ""

# JavaScriptからこの入力欄に「出筋」または「退筋」が書き込まれたら発動
record_val = st.chat_input("hidden_trigger", key="hidden_input") 
# ※chat_inputは画面下に固定されますが、CSSで消します。

# 判定ロジック
input_data = st.query_params.get("action")
if input_data:
    label = "出筋" if input_data == "in" else "退筋"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_data = pd.DataFrame([[now, label]], columns=["日時", "種別"])
    new_data.to_csv(log_file, mode='a', header=not os.path.exists(log_file), index=False)
    
    st.query_params.clear() # パラメータを消去
    st.toast(f"{label}を記録しました！")
    st.rerun()

# --- 2. 見た目と判定の完全一体化（HTML） ---
st.markdown("""
    <style>
        .main-title { font-size: 26px; font-weight: bold; margin-bottom: 15px; }
        .btn-group { display: flex; gap: 10px; }
        .gym-btn {
            width: 180px; height: 180px; 
            border-radius: 30px; 
            border: none;
            color: white; font-size: 40px; font-weight: bold;
            cursor: pointer;
            display: flex; align-items: center; justify-content: center;
            text-decoration: none;
        }
        .btn-in { background-color: #007bff; }
        .btn-out { background-color: #ff8c00; }
        .gym-btn:active { transform: scale(0.95); opacity: 0.8; }
        
        /* 不要なStreamlit要素を徹底的に隠す */
        [data-testid="stChatInput"] { display: none; }
    </style>

    <h1 class="main-title">ジム打刻アプリ</h1>
    <div class="btn-group">
        <a href="./?action=in" target="_self" class="gym-btn btn-in">出筋</a>
        <a href="./?action=out" target="_self" class="gym-btn btn-out">退筋</a>
    </div>
    <br>
    """, unsafe_allow_html=True)

# --- 3. 履歴表示 ---
if os.path.exists(log_file):
    st.write("### 最近の記録")
    df = pd.read_csv(log_file)
    st.table(df.tail(3).iloc[::-1])