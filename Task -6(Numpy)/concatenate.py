import numpy
nmp = map(int,input().split())
n = numpy.array([input().split() for i in range(nmp[0])],int)
m = numpy.array([input().split() for i in range(nmp[1])],int)

print(numpy.concatenate(n,m),axis = 0)
