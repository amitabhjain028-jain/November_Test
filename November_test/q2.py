str1="silent"
str2="listen"

d1={}
d2={}

for ch in str1:
    if ch in d1:
        d1[ch]+=1
    else:
        d1[ch]=1

for ch in str2:
    if ch in d2:
        d2[ch]+=1
    else:
        d2[ch]=1

if d1 == d2:
    print("Is anagram")
else:
    print("Is not Anagram")