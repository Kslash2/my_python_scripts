import random

trigger_file = open("triggerchannel.txt", 'r')
action_file = open("actionchannel.txt",'r')
trigger_text = trigger_file.read()
action_text = action_file.read()
trigger_file.close()
action_file.close()

trigger_list = list()
action_list = list()



trigger_set = set()
action_set = set()

trigger_dict = dict()
action_dict =  dict()

def create_list(text):
    print("Creating List.....")
    word_list = []
    for word in text.split("\n"):
        word_list.append(str(word))
    return word_list


def create_set(word_list):
    print("Creating Set.....")
    word_set = set()
    for element in word_list:
        word_set.add(element)
    return word_set


def create_dict(word_set,int_list):
    my_dict = dict()
    print("list_size is: "+ str(len(int_list)))
    for el in word_set:
        my_dict[el] = int_list.pop()
    return my_dict

def create_tsv_from_dict(w_dict,filename):
    print("Creating files....")
    file = open(filename,"w")
    for key,value in w_dict.items():
        file.write("{}\t{}\n".format(key,value))
    print("Files created...")
    file.close()
    
trigger_list = create_list(trigger_text)
action_list = create_list(action_text)


trigger_set = create_set(trigger_list)
action_set = create_set(action_list)
print(len(trigger_set))
print(len(action_set))


id_list = list(random.sample(range(0,1000), len(trigger_set)+len(action_set)))
print(len(id_list))
trigger_dict = create_dict(trigger_set,id_list)
action_dict = create_dict(action_set,id_list)

create_tsv_from_dict(trigger_dict,"triggerchannel.tsv")
create_tsv_from_dict(action_dict,"actionchannel.tsv")

