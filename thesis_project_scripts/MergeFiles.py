import sys
import os


files = os.listdir()
merged_file_name = input("Please insert the name of the file to save:")
merged_file = open(merged_file_name, 'a')

for filename in files:
  if filename != merged_file_name:
      if filename != sys.argv[0]:
          f = open(filename, 'r')
          txt = f.read()
          merged_file.write(" ")
          merged_file.write(txt)
          f.close()
  
final_file.close()
print("complete")
