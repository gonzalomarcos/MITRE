import csv
import yaml
import datetime
from datetime import date

from functools import reduce

tech = []
in_file = open('REE.csv', "r")
out_file = open('REE.yaml', "w")
items = {}
itemsT = []
itemsTv= []
item = {}
itemv ={}
items2 = {}
itemsG = []
itemsPrueba ={}


def proper_round(num, dec=0): #detection
    num = num*5
    num = str(num)[:str(num).index('.')+dec+2]
    if num[-1]>='5':
        return float(num[:-2-(not dec)]+str(int(num[-2-(not dec)])+1))
    return float(num[:-1])

def proper_roundv(num, dec=0): #visibility
    num = num*4
    num = str(num)[:str(num).index('.')+dec+2]
    if num[-1]>='5':
        return float(num[:-2-(not dec)]+str(int(num[-2-(not dec)])+1))
    return float(num[:-1])

def conver_to_yaml3(line, counter):
    print("yaml3")
    print(itemsT)
    item3 = {
        'file_type': 'technique-administration',
        'name': 'example',
        'platform': ['all'],
        'version': 1.2,
        'techniques': itemsG
    }

    #itemsT.append(item3)
    #print(itemsT)
    return item3

def convert_to_yaml2(line, counter):
    item2 ={
        'technique_id': line[1],
        'technique_name': line[0],
        'detection': itemsT,
        'visibility': itemsTv }
    print("yaml2")
    #print(item2)
    item={}
    #itemsT.append(item2)
    return item2

def convert_to_yaml(line, counter):
    item = {
                                'applicable_to': ['all'],
                                'comment': '',
                                'location': [''],
                                'score_logbook': [{
                                    'date': datetime.date(date.today().year, date.today().month, date.today().day),
                                    'comment': line[2],
                                    'score': int(proper_round(float(line[3])))}]


    }
    print("item arriba")
    #print(item)
    return item

def convert_to_yamlvisibility(line, counter):
    itemv = {
                                'applicable_to': ['all'] ,
                                'comment': '',
                                'score_logbook': [{
                                    'date': datetime.date(date.today().year, date.today().month, date.today().day),
                                    'comment': 'MITRE Engenuity',
                                    'score': int(proper_roundv(float(line[3])))}]


    }
    print("item arriba v")
    #print(item)
    
    
    
    return itemv


try:
    reader = csv.reader(in_file)
    next(reader, None)  # skip headers

    for counter, line in enumerate(reader):
        print("----------------")
        print(counter)
        print("Lugar"+line[3])
        #print(itemsT)
        if line[1] not in tech:

            if line[3] != "x" and line[3] != '0':
                print("no x")

                #print(line[3])
                #print(counter)
                item2 = convert_to_yaml(line, counter)
                item2v = convert_to_yamlvisibility(line, counter)
                #itemsT = []
                ##itemsT.append(item2)

                itemsT.append(item2)
                #itemsT = {**itemsT, **item2}
                itemsTv.append(item2v)
                #itemsTv = {**itemsTv, **item2v}
                if itemsT != []:
                    itemsT = convert_to_yaml2(line, counter)
                    itemsG.append(itemsT)
                    itemsT = []
                    itemsTv = []
                    item2v = []
                    item2 = []
                    print("itemsG")
                else:
                    print("noitemsG")
                    # print(itemsG)
                    itemsT = []
                    itemsTv = []
                    item2v = []
                    item2 = []






            else:
                print("else")


    #print("fin")
    itemsF=conver_to_yaml3(line, counter)
    print("itemsF")
    print(itemsF)
    out_file.write(yaml.safe_dump(itemsF, default_flow_style=False, sort_keys=False))

finally:
    in_file.close()
    out_file.close()
