import pyqrcode
import pandas as pd

DF = pd.read_csv("images.csv")

for i in range(len(DF)):
    link = DF["link"][i]
    space = DF["class"][i]
    loca = DF["location"][i]
    qr = pyqrcode.create(link)
    qr.png(f"{space}_{loca}.png")