import sys
n = int(input())
a = list(map(int,sys.stdin.readline().rstrip().split()))
v = int(input())
print(a.count(v))