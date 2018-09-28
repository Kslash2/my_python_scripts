#This script replaces words from the file coreresults
#with respective int value from other files
import csv

def create_dictionary(csv_file):
    d={}
    with open(csv_file) as f:
        for line in f:
            (key, value)=line.split("\t")
            d[key]=value.rstrip()
    return d

action_dict = create_dictionary("actionchannel.tsv")
print("action dictionary:" + str(action_dict))

trigger_dict = create_dictionary("triggerchannel.tsv")
print("trigger dictionary:" + str(trigger_dict))

key_list = []
id_list = []
print("Getting keys...")
with open("coreresults.tsv", encoding='utf-8') as coretxt:
    reader = csv.DictReader(coretxt, dialect='excel-tab')
    for row in reader:
        key = str(row['triggerchannel'])
        if(key != ''):
            key_list.append(key)
        else:
            key_list.append(key)
            id_list.append(str(row['id']))
             
print("creating list....")       
with open("trigger_keys.tsv", "w+", encoding='utf-8') as final:
    for key in key_list:
        if(key != ''):                 
            val = trigger_dict[key]
            final.write(val+"\n")
        else:
            val = 'xxx'
            key = 'xxx'
            final.write(val+"\n")

with open("error_key.txt", "w+") as er:
    er.write(str(id_list))
print("work completed")

