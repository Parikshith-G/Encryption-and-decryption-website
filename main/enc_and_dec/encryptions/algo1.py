import random


def algo1_encrypt(text):
    offset=random.randint(0,10000)
    # print(text)
    print(offset)
    s=[]
    for i in text:
        s.append(chr(i))
    i,j=0,len(s)-1
    # print(s)
    # a,b=0,0
    while i<=j:
        a=chr(ord(s[i])+offset)
        b=chr(ord(s[j])+offset)
        s[i]=b
        s[j]=a
        i+=1
        j-=1
    
    key=""
    
    dupoffset=random.randint(0,10000)    
    #print(dupoffset)
    key+=chr(dupoffset)
    key+=chr(offset+dupoffset)
    a=[]
    enctext=""
    for i in s:
        enctext+=i
    a.append(key)
    a.append(enctext)
    # print(a)
    return a