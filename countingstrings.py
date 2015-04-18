s = "ajlsdkjflsboblaksdj;flksjbob"
totalBobs = 0
for letter in range(1, len(s)-1):
    if s[letter-1:letter+2] == 'bob':
        totalBobs += 1
print 'Number of times bob occurs is:', totalBobs