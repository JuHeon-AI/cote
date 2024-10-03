import sys
n = int(input())
ans = []
for i in range(n):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    ans.append(a+b)
for i in range(n):
    print(f"Case #{i+1}: {ans[i]}")