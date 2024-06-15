Q2: MATHTEST
#Alice has a mathematics test for which she is underprepared.
#the question is to find the smallest prime number which is larger than integer N
#find and return an integer representing the smallesr prime number larger than N.
#(prime number :if it is divisible by 1 or itself)




def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
num=int(input())
k=num+1

while True:
    if isprime(k):
        print(k)
        break
    k=k+1