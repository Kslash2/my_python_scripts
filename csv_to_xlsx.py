"""
This script converts csv files in xlsx and after that,
deletes csv files.

"""


import os
import csv
import datetime
from xlsxwriter import Workbook
import glob


for csvfile in glob.glob(os.path.join('.', '*.csv')):
    workbook = Workbook(csvfile[:-4] + '-' + str(datetime.date.today()) + '.xlsx')
    worksheet = workbook.add_worksheet()
    with open(csvfile, 'rt', encoding='utf8') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
    workbook.close()
    os.remove(csvfile)
