s="aaabbccccdaa"
li=[]
len=1
start=s[0]
for ch in s[1:]:
    if ch == start:
        len+=1
    else:
        li.append(f"{start}{len}")
        len=1
        start=ch
li.append(f"{start}{len}")

result="".join(li)

print(result)

 