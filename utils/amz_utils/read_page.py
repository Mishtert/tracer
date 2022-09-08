import requests
from bs4 import BeautifulSoup
import pandas as pd

url ="https://www.amazon.com/Best-Sellers/zgbs/ref=zg_bs_unv_ac_0_ac_1"

HEADERS ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

response = requests.get(url, headers=HEADERS)

print(response)

with open("bestseller.html","w") as f:
    f.write(response.text)



