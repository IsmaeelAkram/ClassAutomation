# LINKS.TXT IS GIT-IGNORED FOR PRIVACY

import webbrowser
import time
import os

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
browser = webbrowser.get(chrome_path)

links = []

for link in open('links.txt').readlines():
    url = link.split('|')[0]
    open_time = link.split('|')[1]
    links.append((url, open_time, False))

while True:
    timestamp = time.strftime("%H:%M")
    for link in links:
        if(timestamp == link[1] and link[2] == False):
            browser.open_new_tab(link[0])
            links[links.index(link)] = (link[0], link[1], True)
            os.system("say New link has been opened.")