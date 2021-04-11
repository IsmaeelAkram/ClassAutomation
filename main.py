import webbrowser
import time
import os
from selenium import webdriver
import sys

chrome_path = "open -a /Applications/Google\ Chrome.app %s"
browser = webbrowser.get(chrome_path)

links = []

for link in open("links.txt").readlines():
    url = link.split("|")[0]
    open_time = link.split("|")[1]
    links.append((url, open_time, False))

print("Found links: " + str(links))
time.sleep(3)

while True:
    timestamp = time.strftime("%H:%M")
    sys.stdout.flush()
    for link in links:
        if str(timestamp) == link[1] or link[1] == "test":
            if link[2] == False:
                if "meet.google.com" in link[0]:
                    browser = webdriver.Chrome()
                    browser.get(link[0])

                    join_btn = browser.find_element_by_xpath(
                        '//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]'
                    )
                    join_btn.click()
                    links[links.index(link)] = (link[0], link[1], True)
                    os.system("say New link has been opened.")
                else:
                    browser.open_new_tab(link[0])
                    links[links.index(link)] = (link[0], link[1], True)
                    os.system("say New link has been opened.")
