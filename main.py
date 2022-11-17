import pyqrcode
import png
from pyqrcode import QRCode
import csv

url = "https://www.apple.com/"
qr = pyqrcode.create(url)

qr.png("myqr.png")