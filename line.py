n=int(input())
count = 0
for i in range(n):
    a = input()
    b = []
    for j in range(len(a)-1):
        b.append(a[j])
        if a[j]!=a[j+1] and b.count(a[j+1]) > 0:
            count +=1
            break
        print(b)
print(n-count)