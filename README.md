# my_python_scripts

I'm learning Python and I'm having so much fun creating scripts of various kinds.

### music.py 
It's a simple script which want a "path" as a parameter.
It will take all the names of .mp3,.wma,.flac files and save them into a dictionary where the key is the artist and the value is the name of the song.
It recognize file names with this form <artist> - <name of the song> .mp3/.wma/.flac. 
If they are not in that form you'll probably will have a strange dictionary as result :D for example if a file is ComputerLove.mp3 the dictionary will save it as {ComputerLove : ComputerLove}.
After creating the dictionary it will save it in a json file in the same dir of the path you passed as argument.
  
  
