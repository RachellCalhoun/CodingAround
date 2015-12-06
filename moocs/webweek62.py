import urllib
import json

serviceurl = "http://python-data.dr-chuck.net/geojson?"
place = "Oregon Institute of Technology"
url = serviceurl + urllib.urlencode({'sensor':'false', 'address': place})


uh = urllib.urlopen(url)
data = uh.read()
js = json.loads(str(data))

#print js to check data
#print json.dump(js, indent=4) to check data
# prints something like : {status: 'ok', 'results':[{...,'place_id':..., }]}
#so js["results"]--- gets into the dictionary value for results and returns a list.
# the [0] first in the list is a dictionary. 
#["place_id"] looks for the value with the key 'place_id'
place_id = js["results"][0]["place_id"] 
print place_id


