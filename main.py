import pyqrcode
import pandas as pd
import pdfkit

codes = []

DF = pd.read_csv("images.csv")

for _, row in DF.iterrows():
    qr = pyqrcode.create(row["link"], error='M')
    codes.append({'location': row["location"],
                  'lesson': row["lesson"],
                  'data': qr.png_as_base64_str()})

html = ""
with open("./template.html", 'r') as f:
    html = f.read()
    

for code in codes:
    html_formatted = html.format(location = code['location'], lesson = code['lesson'], data = code['data'])
    pdfkit.from_string(html_formatted, f"./qrcodes/{code['location']}-{code['lesson']}.pdf")

