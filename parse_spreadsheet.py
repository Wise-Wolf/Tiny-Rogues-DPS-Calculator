from __future__ import print_function

import os.path
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SPREADSHEET_ID = '1QyCWcp8wB7kwCERdsyhKvFfqab2mn8ZgGUmUJq407Yw'
WEAPONS = 'Weapon Stats!A1:M'
ITEMS = 'Item Stats!A1:D'
TRAITS = 'Trait Stats!A1:D'
MODIFIERS = 'Modifiers!A1:D'
CLASSES = 'Classes!A1:J'


# Parse Weapon Data
def parse_weapons():
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=WEAPONS, majorDimension='ROWS').execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
        return

    for row in values[1:]:
        try:
            statsdict = json.loads(row[12])
        except IndexError:
            statsdict = {}

        tempdict = {}

        tempdict['name'] = row[0]
        tempdict['uptier'] = float(row[1])
        tempdict['strsc'] = float(row[2])
        tempdict['dexsc'] = float(row[3])
        tempdict['intsc'] = float(row[4])
        tempdict['mindmg'] = float(row[5])
        tempdict['maxdmg'] = float(row[6])
        tempdict['aps'] = float(row[7])
        tempdict['shots'] = float(row[8])
        tempdict['capacity'] = int(row[9])
        tempdict['relspd'] = float(row[10])
        tempdict['types'] = row[11].split(", ")
        tempdict['stats'] = statsdict
    
        weaponlist.append(tempdict)


# Parse Item Data
def parse_items():
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=ITEMS, majorDimension='ROWS').execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
        return

    for row in values[1:]:
        try:
            statsdict = json.loads(row[2])
        except json.JSONDecodeError:
            statsdict = {}

        tempdict = {}

        tempdict['name'] = row[0]
        tempdict['slot'] = row[3]
        tempdict['conditions'] = row[1].split(", ")
        tempdict['stats'] = statsdict

        itemlist.append(tempdict)


# Parse Trait Data
def parse_traits():
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=TRAITS, majorDimension='ROWS').execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
        return

    for row in values[1:]:
        try:
            statsdict = json.loads(row[2])
        except json.JSONDecodeError:
            statsdict = {}

        tempdict = {}

        tempdict['name'] = row[0]
        tempdict['slot'] = row[3]
        tempdict['conditions'] = row[1].split(", ")
        tempdict['stats'] = statsdict

        itemlist.append(tempdict)


# Parse Modifier Data
def parse_modifiers():
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=MODIFIERS, majorDimension='ROWS').execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
        return

    for row in values[1:]:
        try:
            statsdict = json.loads(row[2])
        except json.JSONDecodeError:
            statsdict = {}

        tempdict = {}

        tempdict['name'] = row[0]
        tempdict['slot'] = row[3]
        tempdict['conditions'] = row[1].split(", ")
        tempdict['stats'] = statsdict

        itemlist.append(tempdict)


# Parse Starter Gear for Classes
def parse_classes():
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=CLASSES, majorDimension='ROWS').execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
        return

    for row in values[1:]:

        tempdict = {}

        tempdict['name'] = row[0]
        tempdict['strength'] = int(row[1])
        tempdict['dexterity'] = int(row[2])
        tempdict['intelligence'] = int(row[3])
        tempdict['weapon'] = row[4]
        tempdict['helmet'] = row[5]
        tempdict['body'] = row[6]
        tempdict['boots'] = row[7]
        tempdict['offhand'] = row[8]
        tempdict['accessory'] = row[9]

        classeslist.append(tempdict)


# Create JSON files for use with the program
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

    global weaponlist
    weaponlist = []
    global itemlist
    itemlist = []
    global classeslist
    classeslist = []

    parse_weapons()
    weapondict = {'Weapons': weaponlist}
    parse_items()
    parse_traits()
    parse_modifiers()
    itemdict = {'Items': itemlist}
    parse_classes()
    classesdict = {'Classes': classeslist}

    with open('weapons.json', 'w') as outfile:
        outfile.write(json.dumps(weapondict, indent=4))
    with open('items.json', 'w') as outfile:
        outfile.write(json.dumps(itemdict, indent=4))
    with open('classes.json', 'w') as outfile:
        outfile.write(json.dumps(classesdict, indent=4))


if __name__ == '__main__':
    parse_data()