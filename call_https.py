import urllib.request

url = "220.181.38.148"
# try:
myURL1 = urllib.request.urlopen("https://" + url, timeout=3)
print(myURL1.getcode())
