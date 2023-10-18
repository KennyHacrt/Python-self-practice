

military_form=int(input('please enter military time  :'))
key=False
if military_form>1200:
    military_form=military_form-1200
    key=True
new_time=str(military_form)

fuc=0
if new_time=='0':
    fuc=1
    new_time='1200'
    
mil=[]
for i in range(len(new_time)) :
    mil.append(new_time[i])
if len(new_time)==4:
    mil.insert(2,':')
else:
    mil.insert(1,':')

for i in range(len(mil)):
    print(mil[i],end='')

if key or len(mil)==5 and fuc!=1 :
    print('p.m.')
else:
    print('a.m.')
