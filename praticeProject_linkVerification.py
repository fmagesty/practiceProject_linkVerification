# Program that, user inputs an URL and the program attempts to download every linked page on that url.
# The program should flag any pages that have a 404 'Not Found' status code and print them out as broken links.

import requests, re
from bs4 import BeautifulSoup

url = 'https://' + input('Enter the url of the page.\n')

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')
urlreg = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', res.text)
for link in soup.find_all('a'):
    link = urlreg
    print(link)