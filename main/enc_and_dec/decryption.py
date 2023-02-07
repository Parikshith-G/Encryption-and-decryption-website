from .decryptions.algo1 import algo1_decrypt
from .decryptions.algo2 import algo2_decrypt
from .decryptions.algo3 import algo3_decrypt
from .decryptions.algo4 import algo4_decrypt

def main_logic_decryption(encryption1_Text,encryption1_Key,encryption2_Key,encryption2_SuperKey,encryption2_Text,encryption3_Key,encryption3_Text,encryption4_DigitalSignature,encryption4_Key,encryption4_Secret,encryption4_SuperKey,encryption4_Text):
    text1=algo1_decrypt(encryption1_Text,encryption1_Key)
    text2=algo2_decrypt(encryption2_Text,encryption2_Key,encryption2_SuperKey)
    text3=algo3_decrypt(encryption3_Text,encryption3_Key)
    text4=algo4_decrypt(encryption4_Text,encryption4_SuperKey,encryption4_Secret,encryption4_DigitalSignature)
    
    # #print(text1)
    # #print("\n")
    # #print(text2)
    # #print("\n")
    # #print(text3)
    # #print("\n")
    # #print(text4)
    # #print(text1+text2+text3+text4)
    text=text1+text2+text3+text4
    return text
    
    #encryption1_Text,encryption1_Key,encryption2_Key,encryption2_SuperKey,encryption2_Text,encryption3_Key,encryption3_Text,encryption4_DigitalSignature,encryption4_Key,encryption4_Secret,encryption4_SupreKey,encryption4_Text