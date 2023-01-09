from __future__ import print_function

import os.path, json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class Klass:
    def __init__(self, name, itemempty, strength, dexterity, intelligence, weapon, helmet, body, boots, offhand, accessory):
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

    def __init__(self, name, uptier, uplevel, strsc, dexsc, intsc, mindmg, maxdmg, aps, shots, capacity, relspd, burndmg, bleeddmg, poisondmg, frostdmg, specialdotdmg, dottickrate, types = ['Unconditional'], stats = {}):
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
        self.burndmg = burndmg
        self.bleeddmg = bleeddmg
        self.poisondmg = poisondmg
        self.frostdmg = frostdmg
        self.specialdotdmg = specialdotdmg
        self.dottickrate = dottickrate
        self.types = types
        self.stats = stats

class Item:
    def __init__(self, slot, name, conditions = ['Unconditional'], stats = {}):
        self.slot = slot
        self.name = name
        self.conditions = conditions
        self.stats = stats

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SPREADSHEET_ID = '1QyCWcp8wB7kwCERdsyhKvFfqab2mn8ZgGUmUJq407Yw'
WEAPONS = 'Weapon Stats!A1:S'
ITEMS = 'Item Stats!A1:D'
TRAITS = 'Trait Stats!A1:D'
MODIFIERS = 'Modifiers!A1:D'
CLASSES = 'Classes!A1:J'

# Parse Weapon Data
def parse_weapons():
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=WEAPONS, majorDimension='ROWS').execute()
    values = result.get('values', [])

    klass = globals()['Weapon']

    if not values:
        print('No data found.')
        return

    for row in values[1:]:
        try:
            newdict = json.loads(row[18])
        except:
            newdict = {}
        # 0:name, 1:uptier, 2:strsc, 3:dexsc, 4:intsc, 5:mindmg, 6:maxdmg, 7:aps, 8:shots, 9:capacity, 10:relspd
        # 11:burndmg, 12:bleeddmg, 13:poisondmg, 14:frostdmg, 15:specialdotdmg, 16:dottickrate, 17:types, 18:stats
        instance = klass(row[0], float(row[1]), 0, float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]), int(row[9]), float(row[10]), \
        float(row[11]), float(row[12]), float(row[13]), float(row[14]), float(row[15]), float(row[16]), row[17].split(', '), newdict)
        allitems[instance.name.lower()] = instance

# Parse Item Data
def parse_items():
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=ITEMS, majorDimension='ROWS').execute()
    values = result.get('values', [])

    klass = globals()['Item']

    if not values:
        print('No data found.')
        return

    for row in values[1:]:
        try:
            newdict = json.loads(row[2])
        except:
            newdict = {}
        instance = klass(row[3], row[0], row[1].split(', '), newdict)
        allitems[instance.name.lower()] = instance
    
    itemempty = Item('Any', 'Empty')
    allitems[itemempty.name.lower()] = itemempty

# Parse Trait Data
def parse_traits():
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=TRAITS, majorDimension='ROWS').execute()
    values = result.get('values', [])

    klass = globals()['Item']

    if not values:
        print('No data found.')
        return

    for row in values[1:]:
        try:
            newdict = json.loads(row[2])
        except:
            newdict = {}
        instance = klass(row[3], row[0], row[1].split(', '), newdict)
        allitems[instance.name.lower()] = instance

# Parse Modifier Data
def parse_modifiers():
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=MODIFIERS, majorDimension='ROWS').execute()
    values = result.get('values', [])

    klass = globals()['Item']

    if not values:
        print('No data found.')
        return

    for row in values[1:]:
        try:
            newdict = json.loads(row[2])
        except:
            newdict = {}
        instance = klass(row[3], row[0], row[1].split(', '), newdict)
        allitems[instance.name.lower()] = instance

# Parse Starter Gear for Classes
def parse_classes():
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=CLASSES, majorDimension='ROWS').execute()
    values = result.get('values', [])

    klass = globals()['Klass']

    if not values:
        print('No data found.')
        return

    for row in values[1:]:
        # name, itemempty, strength, dexterity, intelligence, weapon, helmet = None, body = None, boots = None, offhand = None, accessory = None
        instance = klass(row[0], allitems['empty'], int(row[1]), int(row[2]), int(row[3]), allitems[row[4].lower()], allitems[row[5].lower()], allitems[row[6].lower()], allitems[row[7].lower()], allitems[row[8].lower()], allitems[row[9].lower()])
        allitems[instance.name.lower()] = instance

def parse_data():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds, static_discovery=False)
        global sheet
        sheet = service.spreadsheets()
    except HttpError as err:
        print(err)

    global allitems
    allitems = {}

    parse_weapons()
    parse_items()
    parse_traits()
    parse_modifiers()
    parse_classes()

    return allitems

if __name__ == '__main__':
    parse_data()