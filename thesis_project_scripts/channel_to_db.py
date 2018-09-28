
def create_dictionary(csv_file):
    d={}
    with open(csv_file) as f:
        for line in f:
            (key, value)=line.split("\t")
            d[key]=value.rstrip()
    return d


def create_queries(ch_dict,filename):
    file = open(filename,"w+")
    for key,value in ch_dict.items():
        file.write("INSERT INTO `my_codeflow`.`action_channel` (`id_action_channel`, `name`) VALUES ('{}', '{}');\n".format(value,key))
    file.close()

action_dict = create_dictionary("actionchannel.tsv")

trigger_dict = create_dictionary("triggerchannel.tsv")


#uno alla volta e ricorda di cambiare la query in create_queries
#oppure fare un refactoring
#create_queries(action_dict,"action_queries.txt")
create_queries(trigger_dict,"trigger_queries.txt")
