#!/usr/bin/env python3
# pylint: skip-file

import pandas as pd
import pdfkit
import pyqrcode

with open("./template.html", 'r') as f:
    HTML_DATA = f.read()

DF = pd.read_csv("./images.csv")

for i, row in DF.iterrows():
    QR = pyqrcode.create(row["link"], error="M")
    pdf_data = HTML_DATA.format(QR.png_as_base64_str(), row["location"],
                                row["lesson"])
    pdfkit.from_string(pdf_data,
                       f"./qrcodes/{row['location']} -{row['lesson']}.pdf")
