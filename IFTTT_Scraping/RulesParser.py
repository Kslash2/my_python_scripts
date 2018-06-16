from ServicesParser import *


class Rule:
    def __init__(self, id, name, author, install_num):
        self.id = id
        self.name = name
        self.author = author
        self.install_num = install_num


def get_all_rules(url_list):
    list_of_parsed_rules = []
    for i, url in enumerate(url_list):
        if i > 235 :
            list_raw_rules = get_raw_rules(url)
            list_of_parsed_rules += parse_rules(list_raw_rules)
            print(i)
            print(list_of_parsed_rules)
            print("Writing on file.....")
            write_file(to_json(list_of_parsed_rules), "Rules_List" + str(i))

    return list_of_parsed_rules


def get_raw_rules(url):
    list_rules = []
    page = get_source(url)
    wait_random(60, 120)
    soup = BeautifulSoup(page, 'html.parser')
    list_rules += soup.findAll('li', class_="web-applet-card")

    return list_rules


def parse_rules(list_rules):
    list_of_parsed_rules = []
    for rule in list_rules:
        soup = BeautifulSoup(str(rule), 'html.parser')
        id = str(soup.li['data-id']).strip()
        name = str(soup.find("span", {"class": "title"})).replace("<span class=\"title\">", "").replace("</span>", "").strip()
        author = str(soup.b).replace("<b>", "").replace("</b>", "").strip()
        install_num_tag = str(soup.find("div", {"class": "installs"}))
        install_num = str(BeautifulSoup(install_num_tag, 'html.parser').span).replace("<span>", "").replace("</span>", "").strip()
        list_of_parsed_rules.append(Rule(id, name, author, install_num))

    return list_of_parsed_rules
