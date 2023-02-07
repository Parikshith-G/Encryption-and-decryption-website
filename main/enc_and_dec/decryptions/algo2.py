def algo2_decrypt(enctext,superkey,keyforthesuperkey):
    def foolsKeyDecryptor(superkey,keyforthesuperkey):
        gen=[]
        gen1=[]
        for i in keyforthesuperkey:
            gen.append(ord(i))
        
        for i in superkey:
            gen1.append(ord(i))
        totgen=[]
        i=0 
        while i<len(gen):
            totgen.append(chr(gen1[i]-gen[i]))
            i+=1
        # ##print(totgen)
        retgen=""
        for i in totgen:
            retgen+=i
            
        return(retgen)
        
        # ##print(gen1,gen)
    key=foolsKeyDecryptor(superkey,keyforthesuperkey)
    ##print(key)
    
    
    def foolsTextDecryptor(enctext,key):
        gen=[]
        gen1=[]
        for i in enctext:
            gen.append(ord(i))
        
        for i in key:
            gen1.append(ord(i))
        totgen=[]
        i=0 
        # ##print("asdf",gen1,gen)
        while i<len(gen):
            totgen.append(chr(gen[i]-gen1[i]))
            i+=1
        # ##print(totgen)
        retgen=""
        for i in totgen:
            retgen+=i
            
        return(retgen)
    text=(foolsTextDecryptor(enctext,key))
    a=[]
    #print("enctext        "+enctext)
    #print("key    "+key)
    #print("dectext               " +text)
    a.append(enctext)
    a.append(key)
    a.append(text)
    return text