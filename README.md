# my_python_scripts

I'm learning Python and I'm having so much fun creating scripts of various kinds.

### music.py 
It's a simple script which want a "path" as a parameter.
It will take all the names of .mp3,.wma,.flac files and save them into a dictionary where the key is the artist and the value is the name of the song.
It recognize file names with this form <artist> - <name of the song> .mp3/.wma/.flac. 
If they are not in that form you'll probably will have a strange dictionary as result :D for example if a file is ComputerLove.mp3 the dictionary will save it as {ComputerLove : ComputerLove}.
After creating the dictionary it will save it in a json file in the same dir of the path you passed as argument.
I updated this script, so it will run even if the script will be not given as a parameter. It will just take the actual path where the script is saved.
  
### IFTTT_Scraping
Easy script which works with IFTTT website. I looked at robot.txt and I saw that I could do this.
Service_Parser: Will help you get all the SERVICES in a dictionary { Name_Of_Service : /page_of_the_service }  
Rules_Parser: Will help you getting all the RULES from all the SERVICES pages, you can choose the interval of time to wait between a request or another, default set to 60-120. 
Main: get the SERVICES and the RULES then it will save Services and Rules in JSON files. A JSON file for each RULES page.
Example: My_Toy_Service page will have rules about My_Toy_Service, so you will get a JSON file with all the rules in that page.

### MergeFiles.py
It takes the files in a directory and merge their content into a unique file, I needed this for some JSON...


### thesis_project_scripts
These scripts were created and used by me, for my thesis work. I had a dataset with a lot of rules and smartobject and I extracted them for my needs. 
There are also two script which creates SQL queries for populating a DB that I used.
