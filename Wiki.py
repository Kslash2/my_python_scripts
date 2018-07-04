import urllib.request
import sys

def get_source(arg):
    url = "https://it.wikipedia.org/wiki/"
    response = urllib.request.urlopen(url + arg)
    return response.read()


def write_source(doc,name):
    text_file = open(name + ".html", "w")
    text_file.write(str(doc))
    text_file.close()


def main():
    arg = sys.argv[1]
    doc = get_source(arg)
    write_source(doc,arg)

main()
