def algo4_decrypt(enctext,superkey,secret,digsig):
        # #####print(digsig)
    # for i in digsig:
        #####print(ord(i))]
    cc=len(superkey)
    dd=len(secret)
    ee=len(digsig)
    # #print(c,d,e)
    digcheck1=superkey[0:6]
    
    superkey=ord(superkey[len(superkey)-1])
    ####print(superkey)
    # ######print(superkey)
    digcheck2=secret[0]+secret[1]+secret[2]+secret[3]+secret[4]+secret[5]
    f1,f2,f3,f4,f5,f6=ord(secret[6]),ord(secret[7]),ord(secret[8]),ord(secret[9]),ord(secret[10]),ord(secret[11])
    # ######print(f1)
    microSec=superkey-f1
    # ######print("micrt",microSec)
    superkey-=microSec
    # ######print("sec",superkey-f2)
    sec=superkey-f2
    superkey-=sec
    min=superkey-f3
    superkey-=min
    hour=superkey-f4
    superkey-=hour
    day=superkey-f5
    superkey-=day
    month=superkey-f6
    superkey-=month
    year=superkey
    ######print(microSec,sec,min,hour,day,month,year)
    aMicrosec=[]
    aSec=[]
    aMin=[]
    aHour=[]
    aDay=[]
    aMonth=[]
    aYear=[]
    # ######print(ord(key))
    # ######print(f1)
    i=0
    
    a=enctext[0]
    b=enctext[1]
    c=enctext[2]
    d=enctext[3]
    e=enctext[4]
    f=enctext[5]
    i=6
    try:
        while enctext[i]!=a:
            aMicrosec.append(chr(ord(enctext[i])-microSec))
            i+=1
        # dig5=aMicrosec.pop(0)
        ######print(aMicrosec)
        while enctext[i]!=b:
            aSec.append(chr(ord(enctext[i])-sec))
            i+=1
        aSec.pop(0)
        # #####print(ord(aSec[0]))
        dig1=chr(ord(aSec.pop(0))+sec)
        ######print(aSec)
        while enctext[i]!=c:
            aMin.append(chr(ord(enctext[i])-min))
            i+=1
        aMin.pop(0)
        dig2=chr(ord(aMin.pop(0))+min)
        ######print(aMin)
        while enctext[i]!=d:
            aHour.append(chr(ord(enctext[i])-hour))
            i+=1
        aHour.pop(0)
        dig3=chr(ord(aHour.pop(0))+hour)
        ######print(aHour)
        while enctext[i]!=e:
            aDay.append(chr(ord(enctext[i])-day))
            i+=1
        aDay.pop(0)
        dig4=chr(ord(aDay.pop(0))+day)
        ######print(aDay)
        while enctext[i]!=f:
            aMonth.append(chr(ord(enctext[i])-month))
            i+=1
        aMonth.pop(0)
        dig5=chr(ord(aMonth.pop(0))+month)
        ######print(aMonth)
        while i<len(enctext):
            aYear.append(chr(ord(enctext[i])-year))
            i+=1
        aYear.pop(0)
        dig6=chr(ord(aYear.pop(0))+year)
        ######print(aYear)
        dectext=""
        i=0
        while i<len(aYear):
            dectext+=aMicrosec[i]+aSec[i]+aMin[i]+aHour[i]+aDay[i]+aMonth[i]+aYear[i]
            i+=1
        # #####print(dectext)
        if i!=len(aMicrosec):
            dectext+=aMicrosec[len(aMicrosec)-1]
        if i!=len(aSec):
            dectext+=aSec[len(aSec)-1]
        if i!=len(aMin):
            dectext+=aMin[len(aMin)-1]    
        if i!=len(aHour):
            dectext+=aHour[len(aHour)-1]
        if i!=len(aDay):
            dectext+=aDay[len(aDay)-1]
        if i!=len(aMonth):
            dectext+=aMonth[len(aMonth)-1]
        # #####print(dectext)
        
        check=dig1+dig2+dig3+dig4+dig5+dig6
        ###print(digcheck1,"\t",check,"\t",digcheck2)
        # #####print(check,digsig)
        # # # #####print(dectext)
        # #print(digsig,check,digcheck2,digcheck2)
        
        # for i in digsig:
        #     #print(ord(i))
        # #print("\n")
        # for i in check:
        #     #print(ord(i))
        # #print("\n")
        # for i in digcheck1:
            
        #     #print(ord(i))
        # #print("\n")
        # for i in digcheck2:
        #     #print(ord(i))
        # #print(c,c==7)
        
            # #print
        if check!=digsig or digcheck1!=digsig or digcheck2!=digsig or cc!=7 or dd!=12 or ee!=6:
            raise Exception("Digital signatures dont match")
        return(dectext)
    except Exception as e:
        return("Digital Signatures dont match")
        