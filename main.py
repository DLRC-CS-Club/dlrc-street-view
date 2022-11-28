import pyqrcode
import pandas as pd

DF = pd.read_csv("images.csv")

for i in range(len(DF)):
    link = DF["link"][i]
    area = DF["class"][i]
    location = DF["location"][i]
    qr = pyqrcode.create(link)
    qr.png(f".\\qrcodes\\{location}-{area}.png")