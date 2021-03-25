# LINKS.TXT IS GIT-IGNORED FOR PRIVACY

import webbrowser

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
browser = webbrowser.get(chrome_path)

for link in open('links.txt').readlines():
    url = link.split('|')[0]
    time = link.split('|')[1]