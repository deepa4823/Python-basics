def power(n,m):
n=int(input("Enter number"))
m=int(input("Enter the power"))
def power(n,m):
    if m==0:
        return 1;
    else:
        return n*power(n,m-1);