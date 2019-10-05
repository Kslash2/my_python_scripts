"""
This script get all csv files in the current directory and merge them
into a unique csv file.

"""


import os
import glob
import csv


writer = csv.writer(open('appended_output.csv', 'w', newline=''))
for csv_file_name in glob.glob(os.path.join('.', '*.csv')):
    if csv_file_name != 'appended_output.csv':
        print(csv_file_name)
        with open(csv_file_name) as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader, None)
            writer.writerows(reader)
