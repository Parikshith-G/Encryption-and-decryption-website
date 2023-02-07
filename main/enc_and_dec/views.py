from django.shortcuts import render
from django.http import FileResponse
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import FileUpload,Document
from django.conf import settings
# Create your views here.
import os
from .encryption import main_logic_encryption
from .decryption import main_logic_decryption
def main(request):
  
    return render(request,'enc_and_dec/index.html')
def playground(request):
    return render(request,'enc_and_dec/playground.html')

def callme(request):
    return render(request,'enc_and_dec/callme.html')


def encryption(request):
    if request.method=="POST":
        
        form=FileUploadForm(request.POST,request.FILES)
        if form.is_valid():
            file=request.FILES['file']
            content=file.read()
            a=main_logic_encryption(content)
            
            algo1_key=a[0]
            algo1_enctext=a[1]
            
            algo2_enctext=a[2]
            algo2_keyforthesuperkey=a[3]
            algo2_superkey=a[4]
            
            algo3_mainkey=a[5]
            algo3_enctext=a[6]
            
            algo4_enctext=a[7]
            algo4_key=a[8]
            algo4_superkey=a[9]
            algo4_secret=a[10]
            algo4_digsig=a[11]
            
    
            file_name1=request.POST.get('file_name')
            file_name2=request.POST.get('file_name')
            file_name3=request.POST.get('file_name')
            file_name4=request.POST.get('file_name')
            file_name5=request.POST.get('file_name')
            file_name6=request.POST.get('file_name')
            file_name7=request.POST.get('file_name')
            file_name8=request.POST.get('file_name')
            file_name9=request.POST.get('file_name')
            file_name10=request.POST.get('file_name')
            file_name11=request.POST.get('file_name')
            file_name12=request.POST.get('file_name')
            
            
            if file_name1:                                  
                file_name1=file_name1+'.txt'
            else:
                file_name1='Encryption1_Key.txt'
                
            if file_name2:
                file_name2=file_name2+'.txt'
            else:
                file_name2='Encryption1_Text.txt'
                
            if file_name3:                                  
                file_name3=file_name3+'.txt'
            else:
                file_name3='Encryption2_Text.txt'
                
            if file_name4:
                file_name4=file_name4+'.txt'
            else:
                file_name4='Encryption2_SuperKey.txt'  
                
            if file_name5:                                  
                file_name5=file_name5+'.txt'
            else:
                file_name5='Encryption2_Key.txt'
                
            if file_name6:
                file_name6=file_name6+'.txt'
            else:
                file_name6='Encryption3_Key.txt'
                
            if file_name7:                                  
                file_name7=file_name7+'.txt'
            else:
                file_name7='Encryption3_Text.txt'
                
            if file_name8:
                file_name8=file_name8+'.txt'
            else:
                file_name8='Encryption4_Text.txt'
                
            if file_name9:                                  
                file_name9=file_name9+'.txt'
            else:
                file_name9='Encryption4_Key.txt'
                
            if file_name10:
                file_name10=file_name10+'.txt'
            else:
                file_name10='Encryption4_SuperKey.txt'
                
            if file_name11:                                  
                file_name11=file_name11+'.txt'
            else:
                file_name11='Encryption4_Secret.txt'
                
            if file_name12:
                file_name12=file_name12+'.txt'
            else:
                file_name12='Encryption4_DigitalSignature.txt'
                
                
                
            directory=settings.MEDIA_ROOT
     
            
            file_path1 = os.path.join(directory, file_name1)
            file_path2 = os.path.join(directory, file_name2)
            file_path3 = os.path.join(directory, file_name3)
            file_path4 = os.path.join(directory, file_name4)
            file_path5 = os.path.join(directory, file_name5)
            file_path6 = os.path.join(directory, file_name6)
            file_path7 = os.path.join(directory, file_name7)
            file_path8 = os.path.join(directory, file_name8)
            file_path9 = os.path.join(directory, file_name9)
            file_path10 = os.path.join(directory, file_name10)
            file_path11 = os.path.join(directory, file_name11)
            file_path12 = os.path.join(directory, file_name12)
            
            file1=open(file_path1,'w')
            file2=open(file_path2,'w')
            file3=open(file_path3,'w')
            file4=open(file_path4,'w')
            file5=open(file_path5,'w')
            file6=open(file_path6,'w')
            file7=open(file_path7,'w')
            file8=open(file_path8,'w')
            file9=open(file_path9,'w')
            file10=open(file_path10,'w')
            file11=open(file_path11,'w')
            file12=open(file_path12,'w')
            
            file1.write(algo1_key)
            file2.write(algo1_enctext)
            file3.write(algo2_enctext)
            file4.write(algo2_keyforthesuperkey)
            file5.write(algo2_superkey)
            file6.write(algo3_mainkey)
            file7.write(algo3_enctext)
            file8.write(algo4_enctext)
            file9.write(algo4_key)
            file10.write(algo4_superkey)
            file11.write(algo4_secret)
            file12.write(algo4_digsig)
            
            file1.close()
            file2.close()
            file3.close()
            file4.close()
            file5.close()
            file6.close()
            file7.close()
            file8.close()
            file9.close()
            file10.close()
            file11.close()
            file12.close()
            media_files = []
            media_root = settings.MEDIA_ROOT
            for filename in os.listdir(media_root):
                file_path = os.path.join(media_root, filename)
                if os.path.isfile(file_path):
                    media_files.append(filename)
            names=["Encryption1_Text","Encryption1_Key","Encryption2_Text","Encryption2_SuperKey","Encryption2_Key","Encryption3_Text","Encryption3_Key","Encryption4_DigitalSignature","Encryption4_Text","Encryption4_Key","Encryption4_Secret","Encryption4_SuperKey"]
            k=len(names)-1
            context = {
                "media_files": media_files,
                "media_url": settings.MEDIA_URL,
            
            }
            
           
    
            return render(request,'enc_and_dec/encryption_download.html',{"context":context,"names":names,"media_files":media_files})
    
    else:
        form=FileUploadForm()
    return render(request,'enc_and_dec/encryption.html',{'form':form})
    
    
    
    

def decryption(request):
    if request.method == "POST":
        file1 = request.FILES.get('file1')
        file2 = request.FILES.get('file2')
        file3 = request.FILES.get('file3')
        file4 = request.FILES.get('file4')
        file5 = request.FILES.get('file5')
        file6 = request.FILES.get('file6')
        file7 = request.FILES.get('file7')
        file8 = request.FILES.get('file8')
        file9 = request.FILES.get('file9')
        file10 = request.FILES.get('file10')
        file11 = request.FILES.get('file11')
        file12 = request.FILES.get('file12')
        
        encryption1_Text=file1.read().decode('utf-8')
        encryption1_Key=file2.read().decode('utf-8')
        encryption2_Key=file3.read().decode('utf-8')
        encryption2_SuperKey=file4.read().decode('utf-8')
        encryption2_Text=file5.read().decode('utf-8')
        encryption3_Key=file6.read().decode('utf-8')
        encryption3_Text=file7.read().decode('utf-8')
        encryption4_DigitalSignature=file8.read().decode('utf-8')
        encryption4_Key=file9.read().decode('utf-8')
        encryption4_Secret=file10.read().decode('utf-8')
        encryption4_SuperKey=file11.read().decode('utf-8')
        encryption4_Text=file12.read().decode('utf-8')
        # print(encryption1_Text,encryption1_Key).decode('utf-8')
        decodedText=main_logic_decryption(encryption1_Text,encryption1_Key,encryption2_Key,encryption2_SuperKey,encryption2_Text,encryption3_Key,encryption3_Text,encryption4_DigitalSignature,encryption4_Key,encryption4_Secret,encryption4_SuperKey,encryption4_Text)
        
        return render(request,'enc_and_dec/decryption_download.html',{'decodedText':decodedText})
    
    else:
        form=FileUploadForm()
    return render(request,'enc_and_dec/decryption.html',{'form':form})
    







