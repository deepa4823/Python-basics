#u r given an integer array nums containing positive integers.
#we define a function encrypt such that encrypt(x)replaces every digit
#in x with the largest digit in x.
#ex:encrypt(523)=555 and encrypt(213)=333  return the sum of encrypted elements.



a=[321,645,984]
def process(n):
#max and count
    mx=-999
    c=0
    ans=0
    while n>0:
        digit=n%10
        if digit>mx:
            mx=digit
        c=c+1
        n=n//10

            #arrange
    while c>0:
        ans=ans*10+mx
        c=c-1
    return ans
n=list(map(int,input().split()))
f_ans=0
for i in n:
       ans=process(i)
       f_ans+=ans
print(f_ans)       
        