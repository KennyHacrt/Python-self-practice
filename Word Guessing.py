import random
vocab_list=['Computer','Python','Human','Keyboard','Mouse']
selected_vocab=vocab_list[random.randint(0,len(vocab_list)-1)]
modified_list=[]

#select alphabets from vocab
luck2=random.randint(0,len(selected_vocab)-1)
luck3=random.randint(0,len(selected_vocab)-1)
luck1=random.randint(0,len(selected_vocab)-1)
while True:
    if luck2==luck1 or luck2==luck3 or luck1==luck3:
        luck2=random.randint(0,len(selected_vocab)-1)
        luck3=random.randint(0,len(selected_vocab)-1)
        luck1=random.randint(0,len(selected_vocab)-1)
    else:
        break


#modify selected vocabulary
for i in range(len(selected_vocab)):

    if int(selected_vocab.index(selected_vocab[i]))==luck1 or int(selected_vocab.index(selected_vocab[i]))==luck2 or int(selected_vocab.index(selected_vocab[i]))==luck3:
        modified_list.append(selected_vocab[i])
    else:
        modified_list.append('_')
print(" ".join(modified_list))

#play

def is_win():
    chances=3
    for i in range(3):
        ans=input('please guess the word  :')
        if ans.lower()==selected_vocab.lower():
            print('You win')
            break
        chances-=1
        if chances==0:
            print('You lose')
            break


        print(f'try again you still have {chances} chances')



is_win()
    
