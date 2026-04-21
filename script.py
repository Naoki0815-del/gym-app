import flet as ft
import pandas as pd
from datetime import datetime
import os

# 保存用ファイル名
LOG_FILE = "gym_log.csv"

def main(page: ft.Page):
    # --- ページ設定 ---
    page.title = "ジム打刻アプリ (Flet版)"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 450
    page.window_height = 600
    page.padding = 30
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- 保存・通知処理 ---
    def record_data(label, color):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # CSVへの保存処理
        new_data = pd.DataFrame([[now, label]], columns=["日時", "種別"])
        if os.path.exists(LOG_FILE):
            new_data.to_csv(LOG_FILE, mode='a', header=False, index=False)
        else:
            new_data.to_csv(LOG_FILE, index=False)

        # ポップアップ通知 (SnackBar)
        msg = "ジムに来れてすごい！🔥" if label == "出筋" else "お疲れさま！✨"
        page.snack_bar = ft.SnackBar(
            content=ft.Text(f"{label}完了: {msg}"),
            bgcolor=color,
            duration=2000,
        )
        page.snack_bar.open = True
        page.update()

    # --- UI要素 ---
    title = ft.Text("ジム打刻アプリ", size=32, weight="bold", color=ft.colors.BLUE_GREY_900)

    # 出筋ボタン
    btn_in = ft.Container(
        content=ft.Text("出筋", size=40, weight="bold", color="white"),
        width=180,
        height=180,
        bgcolor=ft.colors.BLUE,
        border_radius=30,
        alignment=ft.alignment.center,
        on_click=lambda _: record_data("出筋", ft.colors.BLUE),
    )

    # 退筋ボタン
    btn_out = ft.Container(
        content=ft.Text("退筋", size=40, weight="bold", color="white"),
        width=180,
        height=180,
        bgcolor=ft.colors.ORANGE,
        border_radius=30,
        alignment=ft.alignment.center,
        on_click=lambda _: record_data("退筋", ft.colors.ORANGE),
    )

    # レイアウト配置
    page.add(
        title,
        ft.Divider(height=40, color="transparent"),
        ft.Row(
            [btn_in, btn_out],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        ),
        ft.Divider(height=40, color="transparent"),
        ft.Text("ボタンを押すと自動で gym_log.csv に保存されます", color="grey")
    )

# アプリ起動
ft.app(target=main)