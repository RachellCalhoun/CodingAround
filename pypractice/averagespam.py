# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
pos = 0
total = 0 

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    if line.startswith("X-DSPAM-Confidence:"):
        count=count+1
        
        
        pos = line.find(' ')
        val = line[pos:]

        total = total + float(val) 

	avg = total/count 
print "Average spam confidence:", avg
