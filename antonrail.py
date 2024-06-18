#ANT ON RAIL
#solution:
#sample input:5
            # 1 -1 1 -1 1 
#output: 2

'''
n=int(input())
vals=list(map(int,input().split()))
start=0
ans=0
for i in vals:
    start=start+i
    if start==0:
        ans=ans+1
print(ans)