import datetime
import random
current_time=datetime.datetime.now()

def algo3_encrypt(text1):
    hour=[]
    day=[]
    month=[]
    year=[]
    p=0
    i=0
    text=[]
    for i in text1:
        text.append(chr(i))
    # #print(text)
    i=0
    while i<len(text):
        # if p==0:
        #     sec.append(ord(text[i]))
        #     p+=1
        #     i+=1
        # elif p==1:
        #     min.append(ord(text[i]))
        #     p+=1
        #     i+=1
        if p==0:
            hour.append(ord(text[i]))
            
            p+=1
            i+=1
        elif p==1:
            day.append(ord(text[i]))
            p+=1
            i+=1
        elif p==2:
            month.append(ord(text[i]))
            p+=1
            i+=1
        elif p==3:
            year.append(ord(text[i]))
            p+=1
            i+=1
        # elif p==0:
        #     microsec.append(ord(text[i]))
        #     p+=1
        #     i+=1
        else:
            p=0
        
    # ###print(sec)
    # ###print(a,b,c,current_time.second)
    #print(hour,month,day,year)
    key=[]
    offset=random.randint(0,10000)
    # while offset==39:
    #     offset=random.randint(0,100000)
    ct_hour= current_time.hour
    ct_day=current_time.day
    ct_month=current_time.month
    ct_year=current_time.year
    #print("aaaggg",offset)
    # # ###print(type(current_time.second))
    # key=str(current_time.second)+str(current_time.minute)+str(ct_hour)+str(ct_day)+str(ct_month)
    key.append(chr(ct_hour+offset))
    key.append(chr(ct_day+offset))
    key.append(chr(ct_month+offset))
    key.append(chr(ct_year+offset))
    #print("key",key)
    ###print(key)
    ###print(ct_hour)
    # for i in range(len(microsec)):
    #     microsec[i]+=current_time.microsecond
    # i=0
    # while i<1000000000000000000:
    #     i+=1
    # for i in range(len(sec)):
    #     sec[i]+=current_time.second
    # for i in range(len(min)):
    #     min[i]+=current_time.minute
    for i in range(len(hour)):
        hour[i]+=ct_hour
    for i in range(len(day)):
        day[i]+=ct_day
        
    for i in range(len(month)):
        month[i]+=ct_month
    for i in range(len(year)):
        year[i]+=ct_year
        
    for i in range(len(hour)):
        hour[i]=chr(hour[i])
    for i in range(len(day)):
        day[i]=chr(day[i])
    for i in range(len(month)):
        month[i]=chr(month[i])
    for i in range(len(year)):
        year[i]=chr(year[i])
    
    ###print(hour,month,day,year)
    a,b,c,d=random.randint(10000,20000),random.randint(10000,20000),random.randint(10000,20000),random.randint(10000,20000)
    enctext=chr(a)+chr(b)+chr(c)
    # while a==39:
    #     a=random.randint(0,100000)
    # while b==39:
    #     b=random.randint(0,100000)
    # while c==39:
    #     c=random.randint(0,100000)
    # while d==39:
    #     d=random.randint(0,100000)
    for i in hour:
        enctext+=i
    enctext+=chr(a)
    for i in day:
        enctext+=i
    enctext+=chr(b)
    for i in month:
        enctext+=i
    enctext+=chr(c)
    for i in year:
        enctext+=i
    ###print(len(enctext))
    ##print(offset)
    mainkey=""
    mainkey+=str(chr(offset))
    ##print(key)
    for i in key:
        mainkey+=str(i)
    a=[]
    # print(enctext)
    #print("main",mainkey)
    a.append(mainkey)
    a.append(enctext)
    # ##print(hour,day,month,year)
    # print(a)
    return (a)
    # pass