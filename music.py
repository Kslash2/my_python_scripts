import glob
import os
import sys
import json


def get_path():
    #get path from parameters
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            path = str(sys.argv[1])
        else:
            path = 0
    #get path of the script if path is not given as parameter
    else:
        path = os.path.dirname(os.path.abspath(__file__))

    return path


def find_mp3_music(path):
    mp3_list = glob.glob(path + "\*.mp3")
    print("found: " + str(len(mp3_list)) + " mp3")
    wma_list = glob.glob(path + "\*.wma")
    print("found: " + str(len(wma_list)) + " wma")
    flac_list = glob.glob(path + "\*.flac")
    print("found: " + str(len(flac_list)) + " flac")
    music_list = mp3_list + wma_list + flac_list
    name_list = []
    for m in music_list:
        name_list.append(os.path.basename(m))

    return name_list


def get_artist_name_song_name(music):
    if music.find('-'):
        music_parsed = music.split("-")
        if len(music_parsed) > 1:
            key = music_parsed[0].strip()
            value = music_parsed[1].strip().replace(".mp3", "").replace(".wma", "").replace(".flac", "")
            return {key: value}
        else:
            musicp = music.strip().replace(".mp3", "").replace(".wma", "").replace(".flac", "")
            return {musicp: musicp}
    else:
        musicp = music.strip().replace(".mp3", "").replace(".wma", "").replace(".flac", "")
        return {musicp: musicp}


def create_dict(music_list):
    music_dictionary = {}
    for music in music_list:
        music_dictionary.update(get_artist_name_song_name(music))

    return music_dictionary


def save_json(path, music_dictionary):
    name = os.path.basename(os.path.normpath(path)) + ".json"
    print("Songs list saved in the file: " + name)
    with open(path + "\\" + name, 'w') as f:
        json.dump(music_dictionary, f)


def main():
    my_path = get_path()
    if my_path == -1:
        print("Sorry, insert a path!")
    else:
        if my_path == 0:
            print("Sorry, this path doesnt'exists!")
        else:
            music = find_mp3_music(my_path)
            music_dictionary = create_dict(music)
            print("Result list: ")
            print(music_dictionary)
            save_json(my_path, music_dictionary)


main()
