num_list=['1','2','3','4','5','6','7','8','9','0']
username=input('please enter your username  :')
password=input('please enter your password  :')
asciia_symbol_list=[]

for i in range(33,48):
    asciia_symbol_list.append(chr(i))
for i in range(58,65):
    asciia_symbol_list.append(chr(i))
for i in range(91,97):
    asciia_symbol_list.append(chr(i))
for i in range(123,127):
    asciia_symbol_list.append(chr(i))
while True:
    corr=[]
    corr_pass=[]
    Capital_letter=0
    Lower_letter=0
    numbers=0
    symbol=0
    for i in range(len(username)):
        corr.append(username[i])
    
    for i in range (len(corr)):
        if corr[i] == corr[i].capitalize() or corr[i] == ' ' or len(username)<5:
            username_check=False
            break
        else:
           username_check=True
    
    
    for i in range (len(password)):
        corr_pass.append(password[i])

    for i in range(len(corr_pass)):
        if len(password)<5:
            password_check=False
            break
        if corr_pass[i]==corr_pass[i].capitalize():
            Capital_letter+=1
        if corr_pass[i]==corr_pass[i].lower():
            Lower_letter+=1
        for j in range(len(num_list)):
            if corr_pass[i]==num_list[j]:
                numbers+=1
                break
        for k in range(len(asciia_symbol_list)):
            if corr_pass[i]==asciia_symbol_list[k]:
                symbol+=1
                break
    



    if Capital_letter!=0 and Lower_letter!=0 and numbers!=0 and symbol!=0:
        password_check=True


    if username_check==True and password_check==True :
        break
    if username_check==False :
        username=input('please enter your username  :')
    if password_check==False :
        password=input('please enter your password  :')
print(f'your username is {username}')
print(f'your password is {password}')  
