#!/usr/bin/env python3
# pylint: skip-file

import flet as ft
from flet.buttons import RoundedRectangleBorder
import pyqrcode
import pandas as pd

def main(page: ft.Page):
    """flet app"""
    page.title = "QR Generator"
    appbar = ft.AppBar(title=ft.Text("QR Generator", style="headlineMedium"), center_title=True)
    page.window_width, page.window_height = 360, 640
    PATH = None

    def pick_files_result(e: ft.FilePickerResultEvent):
        global PATH
        if e.files: PATH = ", ".join(map(lambda f: f.path, e.files))
        print(f"path:{PATH}")

    def generate(e):
        # code goes here
        ...
        DF = pd.read_csv("images.csv")

        for i in range(len(DF)):
            link = DF["link"][i]
            area = DF["class"][i]
            location = DF["location"][i]
            qr = pyqrcode.create(link)
            qr.png(f".\\qrcodes\\{location}-{area}.png")

    btn_style = ft.ButtonStyle(
        padding=(page.window_width/3.45), shape=RoundedRectangleBorder(radius=16)
    )

    generate_qr = ft.ElevatedButton("Generate QR", icon=ft.icons.FILE_DOWNLOAD, style=btn_style, on_click=generate)
    pick_files = ft.ElevatedButton("Pick csv files", icon=ft.icons.UPLOAD_FILE, style=btn_style, on_click=lambda _: pick_files_dialog.pick_files())
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    page.overlay.append(pick_files_dialog)

    page.add(
        appbar,
        ft.Divider(),
        ft.Column([pick_files, generate_qr])
    )

ft.app(target=main)