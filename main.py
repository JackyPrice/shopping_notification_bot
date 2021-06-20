import time

import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

useragent = UserAgent()

# attempt to prevent the website from thinking this is a bot
opts = Options()
opts.add_argument("user-agent="+useragent.random)
driver = webdriver.Chrome(options=opts)

# gets specific filter on store for new egg for 1200W+ corsair psus
# driver.get("https://www.newegg.com/global/uk-en/p/pl?N=101582752%20600479300%2050001459%20600479299&cm_sp=Cat_Power-Supplies_3-_-VisNav-_-titanium-1200W-above-_3")

# test on gpu in stock
while True:
    driver.get("https://www.newegg.com/global/uk-en/p/pl?N=101582767%20601331379%20601296707")

    # wait for website to load
    time.sleep(5)

    html = driver.page_source
    soup = bs4.BeautifulSoup(html, "html.parser")
    items_in_store = soup.find_all("div", {"class":"item-container"})

    in_stock = []
    stock_count = 0
    for item in items_in_store:
        if("OUT OF STOCK" not in item.text):
            in_stock.append(item)
            stock_count = stock_count + 1

    print("after filter")
    print("there are " + str(stock_count) + " unique items in stock")
    for url in in_stock:
        print(url)

    time.sleep(600)