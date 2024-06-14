n=int(input())
ans=n
org=n
count=0
n1=0
while n>0:
    count=count+1
    n=n//10
n=0
count=4
153
    while n1>0:        #153#15#1#0
        digit=n1%10    #3#5#1
        p=digit**count  #3**3#5**3#1**3
        ans=ans+p
        n1=n1//10

if ans==org:
    print("arm")
else:
    print("no")