import sys, gzip

a = gzip.open(sys.argv[1])
b = a.read()
c = [z[2]*z[1]/1000. for z in [[eval(y) for y in x.split(',')] for x in b.splitlines()[1::]] if sum(z[1::]) > 0]
print sum(c)/80e3
