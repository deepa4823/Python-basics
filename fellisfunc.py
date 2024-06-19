FELLIS FUNCTION
'''
f(0)=1
f(1)=1
f(n)=f(n-1)+7*f(n-2)+(n/4)modulo 10^9+7
'''


# using recursion
'''

def fel(n):
    if n==0:
        return 1
    if n==1:
        return 1
    
    return(fel(n-1)+7*fel(n-2)+n//4)%(10**9+7)

num=int(input())
res=fel(num)
print(res)
