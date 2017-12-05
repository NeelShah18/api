import re
import sys
import urllib
from bs4 import BeautifulSoup

usage = "Run the script: ./geolocate.py IPAddress"

if len(sys.argv)!=2:
    print(usage)
    sys.exit(0)

if len(sys.argv) > 1:
    ipaddr = sys.argv[1]

geody = "http://www.geody.com/geoip.php?ip=" + ipaddr
html_page = urllib.request.urlopen(geody).read()
soup = BeautifulSoup(html_page,"lxml")

# Remove html tags using regex.
print(soup)