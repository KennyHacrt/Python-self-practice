import pickle
DATA_LIST=[1,'Kenny',123,24,35,'Donald','ASki',95,123,1231,'Heny']
def turn_list_to_binary():
    with open('binary task.txt','wb+') as Binary_data_file:
        binary_data=[]
        for i in range(len(DATA_LIST)):
            binary_data.append(pickle.dumps(DATA_LIST))
        Binary_data_file.writelines(binary_data)
    


    

def Open_binary_file():
    with open('binary task.txt','rb') as Binary_data_file:
        temp=Binary_data_file.readlines()
        for i in range(len(temp)):
            a=pickle.loads(temp[i])
            print(a)
