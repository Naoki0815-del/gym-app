import flet as ft
import pandas as pd
from datetime import datetime
import os

# 保存用ファイル名
LOG_FILE = "gym_log.csv"

def main(page: ft.Page):
    # --- ページ設定 ---
    page.title = "ジム打刻アプリ"
    page.window_width = 450
    page.window_height = 500
    page.padding = 40
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- 共通の保存・通知関数 ---
    def record(label, message, color):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # CSV保存
        df = pd.DataFrame([[now, label]], columns=["日時", "種別"])
        df.to_csv(LOG_FILE, mode='a', header=not os.path.exists(LOG_FILE), index=False)

        # 通知を表示
        page.snack_bar = ft.SnackBar(
            content=ft.Text(f"{label}完了：{message}"),
            bgcolor=color,
        )
        page.snack_bar.open = True
        page.update()

    # --- ボタンごとの処理 ---
    def handle_in(e):
        record("出筋", "ジムに来れてすごい！🔥", ft.Colors.BLUE) # colors -> Colors

    def handle_out(e):
        record("退筋", "お疲れさま！✨", ft.Colors.ORANGE) # colors -> Colors

    # --- UI構成 ---
    page.add(
        ft.Text("ジム打刻アプリ", size=32, weight="bold"),
        ft.Divider(height=40, color="transparent"),
        ft.Row(
            [
                # 出筋ボタン
                ft.Container(
                    content=ft.Text("出筋", size=40, weight="bold", color="white"),
                    width=170, height=170,
                    bgcolor=ft.Colors.BLUE, # colors -> Colors
                    border_radius=30,
                    alignment=ft.alignment.center,
                    on_click=handle_in,
                ),
                # 退筋ボタン
                ft.Container(
                    content=ft.Text("退筋", size=40, weight="bold", color="white"),
                    width=170, height=170,
                    bgcolor=ft.Colors.ORANGE, # colors -> Colors
                    border_radius=30,
                    alignment=ft.alignment.center,
                    on_click=handle_out,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        ),
    )

# WEBブラウザモードで起動
ft.app(target=main, view=ft.AppView.WEB_BROWSER)