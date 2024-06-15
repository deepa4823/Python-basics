ENCODE THE NUMBER
#input:167
#output=13649


'''
n=167
#to calculate no of digits
def sod(n):
    c=0
    while n>0:
        c=c+1
        n=n//10
    return c
print(sod(n))
#to calculate squareroot from end digit ie,49361
def rev(n):
    ans=0
    while n>0:
        digit=n%10
        sq=digit**2
        sod_sq=sod(sq)
        ans=ans*(10**sod_sq)+sq
        n=n//10
    return ans
print(rev(n))
ans=rev(n)
#to calculate rev of the squareroot ie,16394
def rev2(n):
    ans2=0
    while n>0:
        digit=n%10
        ans2=ans2*10+digit
        n=n//10
    return ans2
print(rev2(ans))    
    
    
#output:
       3
       49361
       16394