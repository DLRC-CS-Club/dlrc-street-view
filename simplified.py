import pandas, pyqrcode
DF = pandas.read_csv("images.csv")
[pyqrcode.create(tag).png(f"qrcodes\\{tag}.png") for tag in DF["tag"]]