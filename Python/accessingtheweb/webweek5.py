import urllib
import xml.etree.ElementTree as ET

url = ' http://python-data.dr-chuck.net/comments_172750.xml  '

uh = urllib.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
countlst = []
for data in counts:
    count = data.text
    count = int(count)
    countlst.append(count)
print ('sum :',(sum(countlst)))


    