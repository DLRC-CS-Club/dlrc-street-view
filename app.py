#!/usr/bin/env python3
# pylint: skip-file

import flet as ft
from flet.buttons import RoundedRectangleBorder
import pyqrcode
import pandas as pd
import pdfkit

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
        with open("./template.html", 'r') as f:
            HTML_DATA = f.read()

        DF = pd.read_csv(PATH)

        for i, row in DF.iterrows():
            QR = pyqrcode.create(row["link"], error="M")
            pdf_data = HTML_DATA.format(QR.png_as_base64_str(), row["location"], row["lesson"])
            pdfkit.from_string(pdf_data, f"./qrcodes/{row['location']}{row['lesson']}.pdf")
    
       

    btn_style = ft.ButtonStyle(
        padding=(page.window_width/3.45), shape=RoundedRectangleBorder(radius=16)
    )

    generate_qr = ft.ElevatedButton("Generate QR PDF", icon=ft.icons.FILE_DOWNLOAD, style=btn_style, on_click=generate)
    pick_files = ft.ElevatedButton("Pick csv file", icon=ft.icons.UPLOAD_FILE, style=btn_style, on_click=lambda _: pick_files_dialog.pick_files())
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    page.overlay.append(pick_files_dialog)

    page.add(
        appbar,
        ft.Divider(),
        ft.Column([pick_files, generate_qr])
    )

ft.app(target=main)