import pandas as pd

# From: https://github.com/search?p=2&q=repose+ccc9c0&type=Code
# https://raw.githubusercontent.com/trevrus/color/a1864946e1819a317258d018baf006724e7207f3/SherwinWilliams/SW-ColorSnap-Color-Swatches-for-SW-Site-locator-031319.csv'
# https://raw.githubusercontent.com/glamp/sherwin-williams/main/data/colors.txt
# https://raw.githubusercontent.com/jpederson/colornerd/gh-pages/csv/sherwin-williams.csv

# TODO:
#  - https://github.com/trevrus/color/blob/main/SherwinWilliams/Emerald%20Designer%20Edition%20Digital%20Data.csv
#  - https://images.sherwin-williams.com/content_images/sw-pdf-sherwin-williams-color.pdf

url = "https://raw.githubusercontent.com/trevrus/color/a1864946e1819a317258d018baf006724e7207f3/SherwinWilliams/SW-ColorSnap-Color-Swatches-for-SW-Site-locator-031319.csv"
sw = pd.read_csv(url, skiprows=[0], usecols=["COLOR #", "COLOR NAME", "LOCATOR #", "RED", "GREEN", "BLUE", "HEX"])
