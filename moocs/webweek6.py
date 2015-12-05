import json
import urllib

url = "http://python-data.dr-chuck.net/comments_172754.json"
uh = urllib.urlopen(url)
data = str(uh.read())


countslst = []
info = json.loads(data)

comments = info['comments']

for item in comments:
  countslst.append(item['count'])
total = sum(countslst)
print total


