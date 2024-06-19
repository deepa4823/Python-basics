PEAK ELEMENT FINDER(use 0- indexing)


a=list(map(int,input().split()))
mp=-999
for i in range(1,len(a)-1):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        p=a[i]
        if p>mp:
            mp=p
print(mp)            
    




output:
1 3 2 20 4 6 5 1
20