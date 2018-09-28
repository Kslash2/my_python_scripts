import csv


with open("coreresults.tsv", encoding='utf-8') as core:
    with open("coreresultstodb.sql", 'w+', encoding='utf-8') as db:
        for row in core:
            values = str(row).replace('\'','').replace('\t','\',\'').replace('\n','')
            db.write('INSERT INTO `behavior` VALUES (\'' + values + '\')'+';'+'\n')


