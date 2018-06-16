from bs4 import BeautifulSoup
import urllib.request
import jsonpickle
import time
import random


def wait_random(min_sec,max_sec):
    rand = random.randint(min_sec, max_sec)
    time.sleep(rand)


def get_source(url):
    response = urllib.request.urlopen(url)
    return response.read()


def get_raw_services(pag, param, attribute):
    soup = BeautifulSoup(pag, 'html.parser')
    return soup.findAll(param, class_=attribute)


def get_parsed_services(tag_list):
    services_dict = {}

    for elem in tag_list:
        soup = BeautifulSoup(str(elem), 'html.parser')
        services_dict[str(soup.find('span')).replace("<span>", "").replace("</span>", "")] = soup.a['href']

    return services_dict


def get_services_url_list(parsed_services_dictionary):
    services_url_list = []
    for key, value in parsed_services_dictionary.items():
        services_url_list.append(str(value).replace('/', 'https://ifttt.com/'))

    return services_url_list


def create_url_list(my_url):
    page = get_source(my_url)
    list_li = get_raw_services(page, "li", "service-tile")
    serv_dict = get_parsed_services(list_li)
    json_serv_dict = to_json(serv_dict)
    write_file(json_serv_dict, "Services_dict")
    del serv_dict['500px']
    url_list = get_services_url_list(serv_dict)

    return url_list


def to_json(obj):
    return jsonpickle.encode(obj)


def from_json(obj):
    return jsonpickle.decode(obj)


def write_file(string_to_save, name):
    text_file = open(name + ".json", "w")
    text_file.write(string_to_save)
    text_file.close()


