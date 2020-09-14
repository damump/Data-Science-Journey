from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import unicodedata

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
count = 0
total = 0
sum = list()
for tag in tags:
    # Look at the parts of a tag
    count = count + 1
    number = tag.contents[0]
    sum.append(number)
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
for item in sum:
    item = int(item)
    total = total + item
print(total)
print(count)
