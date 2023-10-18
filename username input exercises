import random
import getpass
#enter first and last name then print
f, l=input('First name '),input('Last name ')
print(f'Hello {l} !Your first name has {len(f)} letters and {len(l)} letters in last name')

#enter username and email and print
while True:   
    f, l=input('First name '), input('Last name ')
    if (len(f[0])+len(l)) <= 6:
        break
    print(f'{f[0]}{l}@connect.polyu.hk')

#provide options in input
f, l=input('First name '), input('Last name ')
while True:   
    x=input('which name do you want to be adressed?(options:1[first name],2[last name])')
    if int(x)==1 or int(x)==2:
        break
if int(x)==1:
    print(f'Hello {f}!Your first name has {len(f)} letters and {len(l)} characters in second name')
if int(x)==2:
    print(f'Hello {l}!Your first name has {len(f)} letters and {len(l)} characters in second name')

#one input instead of the previous two input
name=input('(first name<space>last name)')
while True:   
    x=input('which name do you want to be adressed?(options:1[first name],2[last name])')
    if int(x)==1 or int(x)==2:
        break
new=name.split(' ')
if int(x)==1:
    print(f'Hello {new[0]}!Your first name has {len(new[0])} letters and {len(new[1])} characters in second name')
if int(x)==2:
    print(f'Hello {new[1]}!Your first name has {len(new[0])} letters and {len(new[1])} characters in second name')

#middle name is optional
name=input('(first name<space>last name[middle name is optional])')
new=name.split(' ')
while True:  
    if  len(new)==2:
        x=input('which name do you want to be adressed?(options:1[first name],2[last name])')
        if int(x)==1 or int(x)==2:
            break
    if  len(new)==3:
        x=input('which name do you want to be adressed?(options:1[first name],2[middle name],3[last name])')
        if int(x)==1 or int(x)==2 or int(x)==3:
            break
    
if int(x)==1 and len(new)==2:
        print(f'Hello {new[0]}!Your first name has {len(new[0])} letters and {len(new[1])} characters in second name')
if int(x)==1 and len(new)==3:
        print(f'Hello {new[0]}!Your first name has {len(new[0])} letters and {len(new[2])} characters in second name and middle name had {len(new[1])} number of letters.')
if int(x)==2 and len(new)==2:
        print(f'Hello {new[1]}!Your first name has {len(new[0])} letters and {len(new[1])} characters in second name')
if int(x)==2 and len(new)==3:
        print(f'Hello {new[1]}!Your first name has {len(new[0])} letters and {len(new[2])} characters in second name and middle name had {len(new[1])} number of letters.')
if int(x)==3 and len(new)==3:
        print(f'Hello {new[2]}!Your first name has {len(new[0])} letters and {len(new[2])} characters in second name and middle name had {len(new[1])} number of letters.')















    
