import urllib
import re

print "we will try to open this url, in order to get IP Address"

url = "http://checkip.dyndns.org"

print url

request = urllib.urlopen(url).read()
print request

theIP = re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', request)

print "your IP Address is: ",  theIP
