
def algo1_decrypt(enctext,key):
    dupoffset=key[0]
    offset=abs(ord(key[1])-ord(dupoffset))
    #print(offset)
    # offset=ord(lock)-ord(dupoffset)
    text=[]
    for i in enctext:
        text.append(i)
    i,j=0,len(text)-1
    while i<=j:
        a=chr(ord(text[i])-offset)
        b=chr(ord(text[j])-offset)
        text[i]=b
        text[j]=a
        i+=1
        j-=1
        
    dectext=""
    for i in text:
        dectext+=i
    return dectext