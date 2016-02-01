#Handling The Data
#The basic outline of this problem is to read the file,
#look for integers using the re.findall(),
#looking for a regular expression of '[0-9]+'
#and then converting the extracted strings to integers
#and summing up the integers.

import re
f = open('web_week2.txt', 'r')
h = f.read()
y = re.findall('[0-9]+', h)
total = 0
for x in y:
    total = total + int(x)
print(total)
