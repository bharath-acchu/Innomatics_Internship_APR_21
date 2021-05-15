import numpy as np
np.set_printoptions(sign=" ")

n, m = list(map(int, input().split()))
k = np.array([input().split() for _ in range(n)],dtype = int)
print(np.mean(k,axis=1), np.var(k,axis=0), sep='\n')
print(np.std(k).round(12))
