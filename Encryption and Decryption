#Encrpt
secret_message=input('enter your secret:  ')
Encrypt=[]
for i in range(len(secret_message)):
    key=65
    key2=97
    if ord(secret_message[i]) != 88 and ord(secret_message[i]) != 89 and ord(secret_message[i]) != 90 and ord(secret_message[i]) != 120 and ord(secret_message[i]) != 121 and ord(secret_message[i]) != 122:
        Encrypt.append(chr(ord(secret_message[i])+3))
    for j in range(88,91):
        if ord(secret_message[i])==j:
            Encrypt.append(chr(key))
        key+=1
        
    for k in range(120,123):
        if ord(secret_message[i])==k:
            Encrypt.append(chr(key2))
        key2+=1
        
print(f'your secret is:  {"".join(Encrypt)}')   

#Decrpt
Encrypted_message=input('enter your Encrypted password:  ')
Decrypt=[]
for i in range(len(Encrypted_message)):
    key=90
    key2=122
    if ord(Encrypted_message[i]) != 65 and ord(Encrypted_message[i]) != 66 and ord(Encrypted_message[i]) != 67 and ord(Encrypted_message[i]) != 97 and ord(Encrypted_message[i]) != 98 and ord(Encrypted_message[i]) != 99:
        Decrypt.append(chr(ord(Encrypted_message[i])-3))
    for j in range(65,68):
        if ord(Encrypted_message[i])==j:
            Decrypt.append(chr(key))
        key-=1
        
    for k in range(97,100):
        if ord(Encrypted_message[i])==k:
            Decrypt.append(chr(key2))
        key2-=1
        
print(f'your secret is:  {"".join(Decrypt)}')  
