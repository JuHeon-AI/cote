import sys
n = int(input())
ans = []
c =[]
d =[]
for i in range(n):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    c.append(a)
    d.append(b)
    ans.append(a+b)
for i in range(n):
    print(f"Case #{i+1}: {c[i]} + {d[i]} = {ans[i]}")