SPACE COUNTER(find and return an integer value representing the count of the number of spaces in given string s)
#input:hello world hey
#output:2


string=(input())
count=0
for i in string:
    if i==' ':
        count+=1
print(count) 