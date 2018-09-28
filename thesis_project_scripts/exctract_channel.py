import csv

file = "coreresults.tsv"
filew = "action_list.txt"

with open(file, encoding= 'utf-8') as  core:
    reader = csv.DictReader(core, delimiter='\t')
    for row in reader:
        with open(filew,"a+",encoding= 'utf-8') as result:
            result.write("{}\n".format(row['actionchannel']))
        
        
