#FIND REPEATED AND MISSING VALUES

r=3
c=3
a=[]
count=0
for i in range(0,3):
    sub=[]
    print("enter values for row",i)
    for j in range(0,3):
        ele=int(input())
        sub.append(ele)
        print(sub)
    a.append(sub)    
    print(a)

#repeated
d={}
ans=[]
for i in range(0,r):
    for j in range(0,c):
        if a[i][j] not in d:
            d[a[i][j]]=1
        else:
            d[a[i][j]]+=1
            if d[a[i][j]]==2:
                ans.append(a[i][j])
print(d)
#missing
for i in range(1,r**2+1):
    if i not in d:
        ans.append(i)
        
print(d)
print(ans)





output:
enter values for row 0
1
[1]
2
[1, 2]
3
[1, 2, 3]
[[1, 2, 3]]
enter values for row 1
4
[4]
6
[4, 6]
7
[4, 6, 7]
[[1, 2, 3], [4, 6, 7]]
enter values for row 2
8
[8]
9
[8, 9]
2
[8, 9, 2]
[[1, 2, 3], [4, 6, 7], [8, 9, 2]]
{1: 1, 2: 2, 3: 1, 4: 1, 6: 1, 7: 1, 8: 1, 9: 1}
{1: 1, 2: 2, 3: 1, 4: 1, 6: 1, 7: 1, 8: 1, 9: 1}
[2, 5]    