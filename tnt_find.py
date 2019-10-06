"""
    This script is useful to search for torrent in the dump file from tnt.village.org, now closed.
    Thank you Luigi Di Liberto and thank you all tnt community.
"""

import pandas as pd
from pathlib import Path
import sys

file_path = Path(__file__).parent.absolute()
dump = "dump_release_tntvillage_2019-08-30.csv"

# not used yet
categories =  [
    "Film TV e programmi",
    "Musica",
    "E Books",
    "Film",
    "Linux",
    "Anime",
    "Cartoni",
    "Macintosh",
    "Windows Software",
    "Pc Game",
    "Playstation",
    "Students Releases",
    "Documentari",
    "Video Musicali",
    "Sport",
    "Teatro",
    "Wrestling",
    "Varie",
    "Xbox",
    "Immagini sfondi",
    "Altri Giochi",
    "Serie TV",
    "Fumetteria",
    "Trash",
    "Nintendo",
    "A Book",
    "Podcast",
    "Edicola",
    "Mobile"
]


URL_release = "http://forum.tntvillage.scambioetico.org/index.php?showtopic="
URL_wayback_machine = "https://web.archive.org/web/http://forum.tntvillage.scambioetico.org/index.php?showtopic="
MAGNET = "magnet:?xt=urn:btih:"

def find_torrent(type_of_search,**kwargs):
    """ Find the torrent using his title (TITOLO), or its title and description (DESCRIZIONE)
        Args:
            type_of_search(int) = flag if it's 1 then search only by title, if it's 2 it search by description too
            searched_word(string) = word searched (TITOLO)
            searched_description(string) = description searched (DESCRIZIONE)
        
        returns:
            dump_table(pandas Dataframe) = resulting dataframe after querying it
    """
    
    searched_word = kwargs.get("searched_word", None)
    searched_description = kwargs.get("searched_description", None)
    
    dump_table = pd.read_csv(dump, delimiter=",")
    dump_table = dump_table.astype(str)
    dump_table = dump_table.rename(columns=lambda x: x.strip())
    if type_of_search == 1:
        dump_table = dump_table[dump_table["TITOLO"].str.contains(searched_word, case=False)]
    elif type_of_search == 2:
        dump_table = dump_table[dump_table["TITOLO"].str.contains(searched_word, case=False)]
        dump_table = dump_table[dump_table["DESCRIZIONE"].str.contains(searched_description, case=False)]
    dump_table["URL_RELEASE_TEMP"] = URL_release
    dump_table["URL_WAYBACK_RELEASE_TEMP"] = URL_wayback_machine
    dump_table["MAGNET_TEMP"] = MAGNET
    dump_table["URL_RELEASE"] =  dump_table["URL_RELEASE_TEMP"] + dump_table["TOPIC"]
    dump_table["URL_WAYBACK_RELEASE"] = dump_table["URL_WAYBACK_RELEASE_TEMP"] + dump_table["TOPIC"]
    dump_table["MAGNET"] = dump_table["MAGNET_TEMP"] + dump_table["HASH"]
    dump_table.drop(columns=["URL_RELEASE_TEMP", "URL_WAYBACK_RELEASE_TEMP", "MAGNET_TEMP"])
    dump_table = dump_table[["TITOLO", "DESCRIZIONE", "DIMENSIONE", "MAGNET", "URL_RELEASE", "URL_WAYBACK_RELEASE", ]]
    
    return dump_table


if __name__ == '__main__':
    if len(sys.argv) == 2:
        # searching by only title
        search_word = str(sys.argv[1]).replace('"', '')
        print("Looking for: " + search_word + "...")
        result = find_torrent(1, searched_word = search_word)
    elif len(sys.argv) == 3:
        # searching by both title and description
        search_word = str(sys.argv[1]).replace('"', '')
        description = str(sys.argv[2]).replace('"', '')
        print("Looking for: " + search_word + "..." + description)
        result = find_torrent(2, searched_word = search_word, searched_description = description)
    print(result)
    result.to_csv("result" + ".csv", sep=",")
print("Result saved to result.csv file.")
