import sys
N,M=map(int,sys.stdin.readline().rstrip().split())

basket = [0]*N
for i in range(N):
    basket[i]= i+1

for i in range(M):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    a1 = basket[a-1]
    b1 = basket[b-1]
    basket[a-1] = b1
    basket[b-1] = a1
print(' '.join(map(str, basket)))