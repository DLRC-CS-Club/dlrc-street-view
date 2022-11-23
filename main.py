#!/usr/bin/env python3

import pandas as pd
import pyqrcode

DF = pd.read_csv("images.csv")

def save_qr():
    """Generate and save a QR code encoded with a tag"""

    for tag in DF["tag"]:
        qr = pyqrcode.create(tag)
        qr.png(f"qrcodes\\{tag}.png")

if __name__ == "__main__":
    save_qr()