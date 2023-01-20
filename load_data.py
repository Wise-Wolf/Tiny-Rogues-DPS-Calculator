from __future__ import print_function

import json


class Klass:
    def __init__(self, name, itemempty, strength, dexterity, intelligence, 
                weapon, helmet, body, boots, offhand, accessory):

        self.name = name
        
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence

        self.helmet = helmet
        self.body = body
        self.boots = boots
        self.offhand = offhand
        self.accessory = accessory

        self.empty = itemempty

        self.weapon = weapon


class Weapon:
    slot = 'Weapon'

    def __init__(self, modifier, name, uptier, uplevel, strsc, dexsc, intsc, mindmg, maxdmg, aps, shots, 
                capacity, relspd, types = ['Unconditional'], stats = {}):

        self.modifier = modifier
        self.name = name
        self.uptier = uptier
        self.uplevel = uplevel
        self.strsc = strsc
        self.dexsc = dexsc
        self.intsc = intsc
        self.mindmg = mindmg
        self.maxdmg = maxdmg
        self.aps = aps
        self.shots = shots
        self.capacity = capacity
        self.relspd = relspd
        self.types = types
        self.stats = stats


class Item:
    def __init__(self, slot, name, conditions = ['Unconditional'], stats = {}):
        self.slot = slot
        self.name = name
        self.conditions = conditions
        self.stats = stats


def load_weapons():
    
    klass = globals()['Weapon']

    f = open('weapons.json')
    data = json.load(f)

    for weapon in data['Weapons']:
        instance = klass(allitems['empty'], weapon['name'], weapon['uptier'], 0, weapon['strsc'], weapon['dexsc'], weapon['intsc'], 
                        weapon['mindmg'], weapon['maxdmg'], weapon['aps'], weapon['shots'], weapon['capacity'], weapon['relspd'], 
                        weapon['types'], weapon['stats'])
        
        allitems[instance.name.lower()] = instance


def load_items():
    
    klass = globals()['Item']

    f = open('items.json')
    data = json.load(f)

    for item in data['Items']:
        instance = klass(item['slot'], item['name'], item['conditions'], item['stats'])
            
        allitems[instance.name.lower()] = instance


def load_classes():
    
    klass = globals()['Klass']

    f = open('classes.json')
    data = json.load(f)

    for klasss in data['Classes']:
        instance = klass(klasss['name'], allitems['empty'], klasss['strength'], klasss['dexterity'], klasss['intelligence'], 
                        allitems[klasss['weapon'].lower()], allitems[klasss['helmet'].lower()], allitems[klasss['body'].lower()], 
                        allitems[klasss['boots'].lower()], allitems[klasss['offhand'].lower()], allitems[klasss['accessory'].lower()])

        allitems[instance.name.lower()] = instance


def load_data():
    global allitems
    allitems = {}
    itemempty = Item('Any', 'Empty')
    allitems[itemempty.name.lower()] = itemempty
    load_weapons()
    load_items()
    load_classes()

    return allitems


if __name__ == '__main__':
    load_data()