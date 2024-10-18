n= int(input())
a = list(map(int,input().split()))
num=0

for i in range(n):
    count=0
    for j in range(1,a[i],1):
        if a[i] % (j)==0:
            count+=1
    if count==1:
        num+=1
print(num)