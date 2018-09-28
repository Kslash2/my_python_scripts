
file_to_read = open("action.txt", 'r')
text = file_to_read.read()
file_to_read.close()
my_list = []
my_set = set()

print("Creating List.....")
for word in text.split("\n"):
    my_list.append(str(word))

print("Creating Set.....") 
for element in my_list:
    my_set.add(element)

print("Creating file....")
final_file = open("actions.csv", "w")

for el in my_set:
    final_file.write("\"%s\",\"%s\"\n" %(str(el).title(),str(el).lower()))
final_file.close()
