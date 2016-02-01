
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)



counts = dict()
for line in handle:
    wds = line.split()
    if len(wds) < 2 : continue
    if wds[0] != "From" : continue
    names = wds[1]
    counts[names] = counts.get(names,0) + 1
    
bignum = None
bigname = None

for name, count in counts.items():
	if bigname is None or count > bignum:
		bigname = name
		bignum = count

print bigname, bignum



