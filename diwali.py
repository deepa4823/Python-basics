DIWALI PROBLEM
#input:6
#      180
#output:4
#explanation:
#amount of time to solve problem is 4*60-180=60 mins
#1 probelm:5 min,time left=60-5=55min
#2:10 min,left=55-10=45min
##4:20min,left=30-20=10min
#5:25 min
#so he can solve only 4 problems,as he is not left with 25 min to complete 5Th problem



np=int(input())
t=int(input())

total=240-t
count=0
t=0
for i in range(1,np+1):
    t=t+5*i
    if t>total:
        break;
    count+=1
print(count)     