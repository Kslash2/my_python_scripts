import sys
import os


files = os.listdir()
merged_file_name = input("Please insert the name of the file to save:")
merged_file = open(merged_file_name, 'a')

for filename in files:
  if filename != merged_file_name:
      if filename != os.path.basename(sys.argv[0]):
          f = open(filename, 'r')
          txt = f.read()
          merged_file.write("\n")
          merged_file.write(txt)
          f.close()
  
merged_file.close()
print("files merged")
