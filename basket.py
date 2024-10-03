import sys
N,M=map(int,sys.stdin.readline().rstrip().split())

basket = [0]*N
for i in range(M):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    for j in range(a-1,b):
        basket[j]=c

print(' '.join(map(str, basket)))