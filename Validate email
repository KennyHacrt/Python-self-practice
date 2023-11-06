def valid_username(username):
    a=0
    key=0
    list_valid=['.','-','_','1','2','3','4','5','6','7','8','9','0']
    #user name first letter
    for i in range(65,91):
        if username[0]==chr(i):
            a+=1
            break
    for i in range(97,123):
        if username[0]==chr(i):
            a+=1
            break
    if a==0:
        return False
    #username body part
    for i in range(len(username)):
           
        for k in range(65,91):
            if username[i]==chr(k):
                key+=1
                
            
        for l in range(97,123):
            if username[i]==chr(l):
                key+=1
                
        for h in range(len(list_valid)):
            if username[i]==list_valid[h]:
                key+=1

        if username[i]==' ':
            return False
    if key<len(username):
            return False
    else:
        return True
    
def valid_domain(domain):
    if domain!='connect.polyu' and domain!='gmail' and domain!='yahoo' and domain!='outlook' :
        return False
    return True

def valid_domain_suffix(domain_suffix):
    if domain_suffix !='com' and domain_suffix!='org' and domain_suffix!='edu' and domain_suffix!='hk':
        return False
    return True

def User_name_corr(email_adress):
        list1=email_adress.split('@')
        list2=list1[1].split('.')
        if len(list2)>3:
            return False
        else:
            if len(list2)==2:
                username=list1[0]
                domain=list2[0]
                domain_suffix=list2[1]
                if valid_username(username)==False:
                    return False
                if valid_domain(domain)==False:
                    return False
                if valid_domain_suffix(domain_suffix)==False:
                    return False
                return True
            else:
                username=list1[0]
                domain=f'{list2[0]}.{list2[1]}'
                domain_suffix=list2[2]
                if valid_username(username)==False:
                    return False
                if valid_domain(domain)==False:
                    return False
                if valid_domain_suffix(domain_suffix)==False:
                    return False
                return True

print(User_name_corr(input('Please enter your email address : ')))
