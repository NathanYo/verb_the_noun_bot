from sys import argv
import random
script, vdict, ndict, checkfile = argv
v = open(vdict)
vlines = v.readlines()
n = open(ndict)
nlines = n.readlines()
v1 = random.randrange(0,3)
n1 = random.randrange(0,3)
v2 = vlines[v1].rstrip('\n')
n2 = nlines[n1].rstrip('\n')
c = open(checkfile, 'a+')
c.write("%s The %s" % (v2, n2))
c.write('\n')
print "%s The %s" % (v2 , n2)
clines = n.readlines()