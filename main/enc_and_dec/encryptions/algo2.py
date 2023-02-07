import random
def algo2_encrypt(text):
    def foolsTextEncryptor(ss:str ):
        key=""
        # maker=""
        enctext=""
        s=[]
        for i in ss:
            s.append(chr(i))
        for i in range(len(s)):
            offset=random.randint(0,10000)
            while offset==39:
                offset=random.randint(0,10000)
            # maker+=str()
            key+=str(chr (offset))
            enctext+=chr(ord(s[i])+offset)
        # #print(key)
        a=[]
        # key+="'"
        a.append(key)
        a.append(enctext)
        
        return a
    arr=foolsTextEncryptor(text)
    
    # #print(arr[0])
    # #print(arr[1])
    key=arr[0]
    enctext=arr[1]
    # #print(key)
    # #print(key)
    #taking key and encrypting it to make a superkey
    def foolsKeyEncryptor(key):
        arr=[]
        for i in key:
            arr.append(i)
        # #print(arr)
        
        superkey=""
        keyforthesuperkey=""
        
        # for i in range(len(arr)):
        #     arr[i]=int(arr[i])
        # #print(arr)
        
        
        
        for i in range(len(arr)):
            p=random.randint(0,10000)
            while p==39:
                p=random.randint(0,10000)
            keyforthesuperkey+=str(chr(p))
            superkey+=chr(ord(arr[i])+p)
        a=[]
        a.append(keyforthesuperkey)
        a.append(superkey)
        return a
    a=(foolsKeyEncryptor(key))
    keyforthesuperkey=a[0]
    superkey=a[1]        
    foolsKeyEncryptor(key)
    
    
    #returning the key superkey and encrypted text
    
    ret=[]
    ret.append(enctext)
    ret.append(keyforthesuperkey)
    ret.append(superkey)
    # #print(key)
    return ret