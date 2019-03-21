from selenium import webdriver
import urllib.request
import requests
import time

driver = webdriver.Firefox()

url = "https://www.baltimorecitibuy.org/bso/external/publicBids.sdo"

driver.get(url)

base_link = "https://www.baltimorecitibuy.org/bso/external/bidAck.sdo?bidId="

org = driver.find_elements_by_class_name('link-01')

bid_link_list = []

for i in range(1, 6):
    
    time.sleep(10)
    val = org[i].get_attribute('href')
    print("link from selenium")
    print(val)
    if len(val) > 130:
        new_val = val[115:]
    elif len(val) < 130:
        new_val = val[119:]
        new_val = new_val + "&parentUrl=activeBids"

    print("This is new val")
    print(new_val)

    bid_link = base_link + new_val
    print("this is bid link")
    print(bid_link)
    print('\n')
    
    bid_link_list.append(bid_link)

print(bid_link_list)

final_bid_link_list = list(dict.fromkeys(bid_link_list))
print(final_bid_link_list)
