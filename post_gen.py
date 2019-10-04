import os
import re
from datetime import datetime, date
import sys

filepath = os.path.abspath(__file__)
dirpath = os.path.dirname(filepath)

files = os.listdir(dirpath)
txt_files = [f for f in files if ".txt" in f]

for txt in txt_files:
    category = sys.argv[1]
    today = date.today().strftime("%y-%m-%d")
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    if not re.match(r"(\d{4})-(1[0-2]|0[1-9])-(3[0-1]|2[0-9]|1[0-9]|0[1-9])-(.*).md", txt):
            title = txt.replace(".txt", "")
            f = open(txt)
            old_content = f.read()
            new_content = f"---\nlayout: post\ntitle:  \"{title}\"\ndate:   {timestamp}\ncategories: {category}\n---\n\n" + old_content
            new_title = today+"-"+title+".md"
            new_f = open(new_title, "w+")
new_f.write(new_content)
