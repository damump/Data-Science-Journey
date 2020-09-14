import urllib.request, urllib.parse, urllib.error
import json


url = input("Enter Location:")
print("Retrieving: ", url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
sum = 0
count = 0

js = json.loads(data)

for item in js["comments"]:
    count = count + 1
    number = int(item["count"])
    sum = sum + number
print("Count:", count)
print("Sum:", sum)
