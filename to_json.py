import json
from zasoby import list2
from ruh import list1


def ruhjson():
 with open("ruh.json", 'w') as write_file:
    json.dump(list1, write_file)
def zasobyjson():
 with open("zasoby.json", 'w') as write_file:
    json.dump(list2, write_file)