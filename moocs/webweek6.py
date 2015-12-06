import json
import urllib

url = "http://python-data.dr-chuck.net/comments_172754.json"
uh = urllib.urlopen(url)
data = str(uh.read())


countslst = []
info = json.loads(data)

comments = info['comments']
count = 0
for item in comments:
  countslst.append(item['count'])
  count += 1
total = sum(countslst)
print "total is: ", total
print "count is: "  count


