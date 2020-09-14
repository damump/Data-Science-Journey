import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input("Enter count:"))
position = int(input("Enter position:"))
print("Retrieving", url)
# Retrieve all of the anchor tagss
co = 0
pos = 0
while co != count:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")
    co = co + 1
    print("Retrieving", tags[17].get("href", None))
    url = tags[17].get("href", None)
    html = urllib.request.urlopen(url, context=ctx).read()
