def algo3_decrypt(enctext,mainkey):
    offset=ord(mainkey[0])
    hourKey=ord(mainkey[1])-offset
    dayKey=ord(mainkey[2])-offset
    monthKey=ord(mainkey[3])-offset
    yearKey=ord(mainkey[4])-offset
    a=enctext[0]
    b=enctext[1]
    c=enctext[2]
    i=3
    hour,day,month,year=[],[],[],[]
    while enctext[i]!=a:
        hour.append(chr(ord(enctext[i])-hourKey))
        i+=1
    while enctext[i]!=b:
        day.append(chr(ord(enctext[i])-dayKey))
        
        i+=1
        
    while enctext[i]!=c:
        month.append(chr(ord(enctext[i])-monthKey))
        i+=1
    while i<len(enctext):
        year.append(chr(ord(enctext[i])-yearKey))
        i+=1
    # day.pop(0)
    month.pop(0)
    year.pop(0)
    day.pop(0)
    text=""
    # for i in hour:
    #     text+=i

    # for i in day:
    #     text+=i
    # for i in month:
    #     text+=i
    # for i in year:
    #     text+=i
    # # ##print(text)
    ##print(hour,day,month,year)
    # for i in enctext:
    i=0
    while i<len(year):
        text+=hour[i]+day[i]+month[i]+year[i]
        ##print(text)
        i+=1
    if i!=len(hour):
        text+=hour[len(hour)-1]
    if i!=len(day):
        text+=day[len(day)-1]
    if i!=len(month):
        text+=month[len(month)-1]
    ##print(text)
    return text