SPECIAL FIBONACCI
#f(N)=f(n-1)*f(n-1)+(n-2)*(n-2)mod 47
#where f(0)=1,f(1)=1
#find and return an integer value representing the nth number in this special series.


'''
def sfib(n):
    if n==0:
        return 1
    if n==1:
        return 1
    
    return(sfib(n-1)*sfib(n-1)+(n-2)*(n-2))%47

num=int(input())
res=sfib(num)
print(res)


output:
6
34