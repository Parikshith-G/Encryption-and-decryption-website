from .encryptions.algo1 import algo1_encrypt
from .encryptions.algo2 import algo2_encrypt
# from .encryptions.algo1 import encrypt
from .encryptions.algo3 import algo3_encrypt
from .encryptions.algo4 import algo4_encrypt
def main_logic_encryption(file):
    
    # print(file,len(file))
    k=len(file)
    part1,part2,part3,part4=file[0:k//4],file[k//4:k//2],file[k//2:3*k//4],file[3*k//4:k]
    # print(part1,part2,part3,part4)
    a=algo1_encrypt(part1)
    b=algo2_encrypt(part2)
    c=algo3_encrypt(part3)
    d=algo4_encrypt(part4)
    # print(d)
    # print(b)
    algo1_key=a[0]
    algo1_enctext=a[1]
    
    algo2_enctext=b[0]
    algo2_keyforthesuperkey=b[1]
    algo2_superkey=b[2]
    
    algo3_mainkey=c[0]
    algo3_enctext=c[1]
    
    algo4_enctext=d[0]
    algo4_key=d[1]
    algo4_superkey=d[2]
    algo4_secret=d[3]
    algo4_digsig=d[4]
    
   
    a=[]
    a.append(algo1_key)
    a.append(algo1_enctext)
    
    a.append( algo2_enctext)
    a.append(algo2_keyforthesuperkey)
    a.append(algo2_superkey)
    
    a.append(algo3_mainkey)
    a.append(algo3_enctext)
    
    a.append(algo4_enctext)
    a.append(algo4_key)
    a.append(algo4_superkey)
    a.append(algo4_secret)
    a.append(algo4_digsig)
    
    return a
    
