#!/usr/bin/env python3
# pylint: skip-file

import pandas as pd
import pdfkit
import pyqrcode

df = pd.read_csv("images.csv")
data = []

for i, row in df.iterrows():
    qr = pyqrcode.create(row["link"], error="M")
    data.append({
        "location": row["location"],
        "lesson": row["lesson"],
        "data": qr.png_as_base64_str()})

with open(r".\\template.html") as f:
    template = f.read()

for code in data:
    location, lesson, data = code["location"], code["lesson"], code["data"]
    html = template.format(data, location, lesson)
    pdfkit.from_string(html, f".\\qrcodes\\{location}-{lesson}.pdf")