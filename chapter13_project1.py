import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')

parms = dict()
parms['address'] = address
url = address
print('Retrieving:', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
tree = ET.fromstring(data)

results = tree.findall("comments/comment")
count = 0
sum = 0
for item in results:
    count = count + 1
    num = int(item.find("count").text)
    sum = sum + num
print("Count:", count)
print("Sum:", sum)
