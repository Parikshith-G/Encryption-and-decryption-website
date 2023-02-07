import random
import datetime
cur_t=datetime.datetime.now()

def algo4_encrypt(text1):
    text=[]
    for i in text1:
        text.append(chr(i))
    aa,bb,cc,dd,ee,ff=chr(random.randint(10000,20000   )),chr(random.randint(10000,20000   )),chr(random.randint(10000,20000   )),chr(random.randint(10000,20000   )),chr(random.randint(10000,20000   )),chr(random.randint(10000,20000   ))
    # ####print(ord(aa))
    digsig=aa+bb+cc+dd+ee+ff
    ##print(digsig)
    curMicSec,curSec,curMin,curHour,curDay,curMonth,curYear=cur_t.microsecond,cur_t.second,cur_t.minute,cur_t.hour,cur_t.day,cur_t.month,cur_t.year
    #####print(curMicSec,curSec,curMin,curHour,curDay,curMonth,curYear)
    key=digsig+chr(curMicSec+curSec+curMin+curHour+curDay+curMonth+curYear)
    check= curMicSec+curSec+curMin+curHour+curDay+curMonth+curYear
    # #####print(curSec)
    flag1=curSec+curMin+curHour+curDay+curMonth+curYear
    flag2=curMin+curHour+curDay+curMonth+curYear
    flag3=curHour+curDay+curMonth+curYear
    flag4=curDay+curMonth+curYear
    flag5=curMonth+curYear
    flag6=curYear
    # #####print(flag1,curMicSec)
    # #####print("micro",check-flag1)
    # key=chr
    superkey=digsig+chr(check)
    

    # for i in digsig:
        ####print("above ",ord(i))
    # #####print(superkey)
    ####print("\n")
    # #####print(key)
    # #####print(superkey)
    #######print(superkey)
    f1,f2,f3,f4,f5,f6=chr(flag1),chr(flag2),chr(flag3),chr(flag4),chr(flag5),chr(flag6)
    secret=digsig+f1+f2+f3+f4+f5+f6
    #######print(secret)
    
    
    # for i in superkey:
    microsec=[]
    sec=[]
    min=[]
    hour=[]
    day=[]
    month=[]
    year=[]
    
    
    p=0
    i=0
    i=0
    
    
    
    
    # ms,ss,mm,hh,dd,mmm,yy=[],[],[],[],[],[],[]
    # while i<len(text):
    #     # #######print(p)
    #     if p==0:
    #         ms.append(text[i])
    #         # microsec.append(chr(ord(text[i])+curMicSec))
    #         # #######print(p)
    #         p+=1
    #         # #######print(p)
    #         i+=1
    #     elif p==1:
    #         # #######print("hit")
    #         ss.append(text[i])
    #         # sec.append(chr(ord(text[i])+curSec))
    #         p+=1
    #         i+=1
    #     elif p==2:
    #         mm.append(text[i])
    #         p+=1
    #         i+=1
    #     elif p==3:
    #         # hour.append(chr(ord(text[i])+curHour))
    #         hh.append(text[i])
    #         p+=1
    #         i+=1
    #     elif p==4:
    #         # day.append(chr(ord(text[i])+curDay))
    #         dd.append(text[i])
    #         p+=1
    #         i+=1
    #     elif p==5:
    #         # month.append(chr(ord(text[i])+curMonth))
    #         mmm.append(text[i])
    #         p+=1
    #         i+=1
    #     elif p==6:
    #         # year.append(chr/(ord(text[i])+curYear))
    #         yy.append(text[i])
        #     p+=1
        #     i+=1
        # # i+=1
    #     else:
    #         # #######print("hit")
    #         p=0
    # #####print(ms,ss,mm,hh,dd,mmm,yy)
            
    p=0
    i=0
    i=0
    while i<len(text):
        # #######print(p)
        if p==0:
            microsec.append(chr(ord(text[i])+curMicSec))
            # #######print(p)
            p+=1
            # #######print(p)
            i+=1
        elif p==1:
            # #######print("hit")
            sec.append(chr(ord(text[i])+curSec))
            p+=1
            i+=1
        elif p==2:
            min.append(chr(ord(text[i])+curMin))
            p+=1
            i+=1
        elif p==3:
            hour.append(chr(ord(text[i])+curHour))
            p+=1
            i+=1
        elif p==4:
            day.append(chr(ord(text[i])+curDay))
            p+=1
            i+=1
        elif p==5:
            month.append(chr(ord(text[i])+curMonth))
            p+=1
            i+=1
        elif p==6:
            year.append(chr(ord(text[i])+curYear))
            p+=1
            i+=1
        # i+=1
        else:
            # #######print("hit")
            p=0
        # i=0
        enctext=""
        a,b,c,d,e,f=random.randint(0,10000),random.randint(0,10000),random.randint(0,10000),random.randint(0,10000),random.randint(0,10000),random.randint(0,10000)
        enctext=chr(a)+chr(b)+chr(c)+chr(d)+chr(e)+chr(f)
        for j in microsec:
            enctext+=j
        enctext+=chr(a)+aa
        for j in sec:
            enctext+=j
        enctext+=chr(b)+bb
        for j in min:
            enctext+=j
        enctext+=chr(c)+cc
        for j in hour:
            enctext+=j
        enctext+=chr(d)+dd
        for j in day:
            enctext+=j
        enctext+=chr(e)+ee
        for j in month:
            enctext+=j
        enctext+=chr(f)+ff
        for j in year:
            enctext+=j
    # #######print(microsec,sec,min,hour,day,month,year)
    # #######print("part1 ",enctext," part 2")
    # #######print("trdt",len(enctext))
    a=[]
    a.append(enctext)
    a.append(key)
    a.append(superkey)
    a.append(secret)
    a.append(digsig)
    # #####print(curMicSec)
    return a
    

