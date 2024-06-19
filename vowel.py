VOWEL REPETITION PROBLEM(print the most frequent vowel that is present in the string as a output)


s=input()
v="aeiou"
mx=-999
ans=0
d={}
for i in s:
    if  i in v:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
        if d[i]>mx:
            mx=d[i]
            ans=i
print(d)
print(ans)



output:
helloworld
{'e': 1, 'o': 2}
o