import line_operations, colors

class Player:
    gold = 0
    hitpoints = 2
    stamina = 2
    armor = 0
    movespeed = 7.5
    movespeedinc = 0.0
    attspd = 1.01
    relspd = 1.0
    refire = 0.0
    critchance = 0.05
    critdmg = 2.0
    incdmg = 0.0
    adddmg = 0
    bonusdmg = 0
    dotrateup = 0.0
    dotup = 0.0
    burnrateup = 0.0
    burnup = 0.0
    bleedrateup = 0.0
    bleedup = 0.0
    poisonrateup = 0.0
    poisonup = 0.0
    frostrateup = 0.0
    frostup = 0.0
    strprof = 0.0
    dexprof = 0.0
    intprof = 0.0
    perks = {1 : '', 2 : '', 3 : '', 4 : '', 5 : '', 6 : ''}

    # Inherit values from the chosen class
    def __init__(self, klass):
        self.klass = klass.name
        self.strength = klass.strength
        self.dexterity = klass.dexterity
        self.intelligence = klass.intelligence
        self.weapon = klass.weapon
        self.offhand = klass.offhand
        self.helmet = klass.helmet
        self.body = klass.body
        self.boots = klass.boots
        self.accessory = klass.accessory

class Klass:
    def __init__(self, name, itemempty, strength, dexterity, intelligence, weapon, helmet = None, body = None, boots = None, offhand = None, accessory = None):
        self.name = name
        
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence

        # If a class doesn't start with a certain item, it is assigned an empty one
        if helmet is None:
            self.helmet = itemempty
        else:
            self.helmet = helmet
        
        if body is None:
            self.body = itemempty
        else:
            self.body = body

        if boots is None:
            self.boots = itemempty
        else:
            self.boots = boots

        if offhand is None:
            self.offhand = itemempty
        else:
            self.offhand = offhand

        if accessory is None:
            self.accessory = itemempty
        else:
            self.accessory = accessory

        self.weapon = weapon

class Weapon:
    def __init__(self, name, uptier, strsc, dexsc, intsc, mindmg, maxdmg, aps, shots, \
    types = {'One-handed': 0, 'Two-handed' : 0, 'Melee' : 0, 'Ranged' : 0, 'Physical' : 0, 'Magical' : 0, 'Bow' : 0, 'Gun' : 0, 'Dagger' : 0, 'Sword': 0, 'Axe' : 0, 'Mace' : 0, 'Scythe' : 0,  'Flail' : 0, 'Wand' : 0, '' : 1}, \
    capacity = 1, reload = 0.0, burndmg = 0.0, bleeddmg = 0.0, poisondmg = 0.0, frostdmg = 0.0, dottickrate = 0.0, \
    attspd = 0.0, refire = 0.0, relspd = 0.0, incdmg = 0.0, adddmg = 0, bonusdmg = 0, critchance = 0.0, critdmg = 0.0, mspd = 0.0, \
    dotup = 0.0, burnup = 0.0, bleedup = 0.0, poisonup = 0.0, frostup = 0.0, dotrateup = 0.0, burnrateup = 0.0, bleedrateup = 0.0, poisonrateup = 0.0, frostrateup = 0.0):
        self.name = name
        self.types = types
        self.upgradetier = uptier
        self.upgradelevel = 0
        self.strsc = strsc
        self.dexsc = dexsc
        self.intsc = intsc
        self.mindmg = mindmg
        self.maxdmg = maxdmg
        self.aps = aps
        self.shots = shots
        self.capacity = capacity
        self.reload = reload
        self.frostdmg = frostdmg
        self.burndmg = burndmg
        self.bleeddmg = bleeddmg
        self.poisondmg = poisondmg
        self.dottickrate = dottickrate
        self.dotrateup = dotrateup
        self.burnrateup = burnrateup
        self.bleedrateup = bleedrateup
        self.poisonrateup = poisonrateup
        self.frostrateup = frostrateup
        self.dotup = dotup
        self.burnup = burnup
        self.bleedup = bleedup
        self.poisonup = poisonup
        self.frostup = frostup
        self.attspd = attspd
        self.relspd = relspd
        self.refire = refire
        self.incdmg = incdmg
        self.adddmg = adddmg
        self.bonusdmg = bonusdmg
        self.critchance = critchance
        self.critdmg = critdmg
        self.mspd = mspd

class Item:
    def __init__(self, slot, name, condition = '', attspd = 0.0, refire = 0.0, relspd = 0.0, incdmg = 0.0, adddmg = 0, bonusdmg = 0, critchance = 0.0, critdmg = 0.0, mspd = 0.0, hp = 0, st = 0, ar = 0, \
    dotup = 0.0, burnup = 0.0, bleedup = 0.0, poisonup = 0.0, frostup = 0.0, dotrateup = 0.0, burnrateup = 0.0, bleedrateup = 0.0, poisonrateup = 0.0, frostrateup = 0.0):
        self.slot = slot
        self.name = name
        self.condition = condition
        self.dotrateup = dotrateup
        self.burnrateup = burnrateup
        self.bleedrateup = bleedrateup
        self.poisonrateup = poisonrateup
        self.frostrateup = frostrateup
        self.dotup = dotup
        self.burnup = burnup
        self.bleedup = bleedup
        self.poisonup = poisonup
        self.frostup = frostup
        self.attspd = attspd
        self.relspd = relspd
        self.refire = refire
        self.incdmg = incdmg
        self.adddmg = adddmg
        self.bonusdmg = bonusdmg
        self.critchance = critchance
        self.critdmg = critdmg
        self.mspd = mspd
        self.hp = hp
        self.st = st
        self.ar = ar

# Create classes
def initialize_classes():
    # Create all the classes, and give them their starting stats + starting gear
    deprived = Klass('Deprived', allitems['empty'], 1, 1, 1, allitems['motail'])
    thehero = Klass('The Hero', allitems['empty'], 1, 1, 1, allitems['motail'])
    warrior = Klass('Warrior', allitems['empty'], 3, 1, 0, allitems['motail'])
    ranger = Klass('Ranger', allitems['empty'], 1, 3, 0, allitems['shtbow'], allitems['hutcap'], allitems['racloak'])
    sorcerer = Klass('Sorcerer', allitems['empty'], 0, 0, 4, allitems['motail'])
    wanderer = Klass('Wanderer', allitems['empty'], 1, 2, 1, allitems['motail'])
    knight = Klass('Knight', allitems['empty'], 2, 1, 1, allitems['motail'])
    thief = Klass('Thief', allitems['empty'], 0, 3, 1, allitems['motail'])
    pyromancer = Klass('Pyromancer', allitems['empty'], 1, 0, 3, allitems['motail'])
    cleric = Klass('Cleric', allitems['empty'], 2, 0, 2, allitems['motail'])
    bandit = Klass('Bandit', allitems['empty'], 2, 2, 0, allitems['motail'])
    gunslinger = Klass('Gunslinger', allitems['empty'], 0, 2, 2, allitems['motail'])
    doppelganger = Klass('Doppelganger', allitems['empty'], 2, 2, 2, allitems['motail'])

    choice = 0
    # Let the user choose their starting class
    while True:
        print('Please choose your class')
        print('1. Deprived')
        print('2. The Hero')
        print('3. Warrior')
        print('4. Ranger')
        print('5. Sorcerer')
        print('6. Wanderer')
        print('7. Knight')
        print('8. Thief')
        print('9. Pyromancer')
        print('10. Cleric')
        print('11. Bandit')
        print('12. Gunslinger')
        print('99. Doppelganger')
        choice = int(input('>'))   
        match choice:
            case 1:
                klass = deprived
                break
            case 2:
                klass = thehero
                break
            case 3:
                klass = warrior
                break
            case 4:
                klass = ranger
                break
            case 5:
                klass = sorcerer
                break
            case 6:
                klass = wanderer
                break
            case 7:
                klass = knight
                break
            case 8:
                klass = thief
                break
            case 9:
                klass = pyromancer
                break
            case 10:
                klass = cleric
                break
            case 11:
                klass = bandit
                break
            case 12:
                klass = gunslinger
                break
            case 99:
                klass = doppelganger
                break
            case _:
                line_operations.cls()
                print(colors.bcolors.FAIL + 'Please input a correct number corresponding to the class you\'re playing!' + colors.bcolors.ENDC)

    global player
    player = Player(klass)

# Perform the initial setup. A goal here would be to load in items from a file into a dictionary from which they'd be easily accessible.
def initial_setup():
    # Create an empty placeholder item
    itemempty = Item('Empty', 'Empty')
    # Create Magic Quiver
    item1 = Item('Offhand', 'Magic Quiver', 'Bow', 0, 0.2)
    # Create Molotov Cocktail
    molotovtypes = {'One-handed': 1, 'Two-handed' : 0, 'Melee' : 0, 'Ranged' : 1, 'Physical' : 1, 'Magical' : 0, 'Bow' : 0, 'Gun' : 0, 'Dagger' : 0, 'Sword': 0, 'Axe' : 0, 'Mace' : 0, 'Scythe' : 0,  'Flail' : 0, 'Wand' : 0, '' : 1}
    weapon1 = Weapon('Molotov Cocktail', 0.07, 0.00, 0.03, 0.01, 175, 200, 2, 1, molotovtypes, 1, 0, 0.6, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.75)
    # Initialize Ranger's starting equipment manually
    shortbowtypes = {'One-handed': 0, 'Two-handed' : 1, 'Melee' : 0, 'Ranged' : 1, 'Physical' : 1, 'Magical' : 0, 'Bow' : 1, 'Gun' : 0, 'Dagger' : 0, 'Sword': 0, 'Axe' : 0, 'Mace' : 0, 'Scythe' : 0,  'Flail' : 0, 'Wand' : 0, '' : 1}
    rangerweapon = Weapon('Shortbow', 0.13, 0.01, 0.03, 0.00, 150, 175, 2.75, 1, shortbowtypes)
    rangerhelmet = Item('Helmet', 'Hunter Cap', 'Ranged', 0.1)
    rangerbody = Item('Body', 'Ranger Cloak')
    # Create a dictionary of all the items manually
    global allitems
    allitems = {'empty' : itemempty, 'motail' : weapon1, 'shtbow' : rangerweapon, 'hutcap' : rangerhelmet, 'racloak' : rangerbody, 'maiver': item1}
    initialize_classes()

# Let the user change a piece of their equipment
def change_equip():
    choice = 0
    name = ''
    line_operations.cls()

    while True:
        print('Which part of your equipment do you want to change?')
        print('1. Weapon')
        print('2. Offhand')
        print('3. Helmet')
        print('4. Body')
        print('5. Boots')
        print('6. Accessory')
        choice = int(input('>'))
        
        match choice:
            case 1:
                name = input('Input the name of the new item >').lower()
                player.weapon = allitems[name]
                choice = int(input('Input the weapon\'s current upgrade level >'))
                player.weapon.upgradelevel = choice
                name = input('Input the weapon\'s modifier >').lower()
                return
            case 2:
                name = input('Input the name of the new item >').lower()
                player.offhand = allitems[name]
                return
            case 3:
                name = input('Input the name of the new item >').lower()
                player.helmet = allitems[name]
                return
            case 4:
                name = input('Input the name of the new item >').lower()
                player.body = allitems[name]
                return
            case 5:
                name = input('Input the name of the new item >').lower()
                player.boots = allitems[name]
                return
            case 6:
                name = input('Input the name of the new item >').lower()
                player.accessory = allitems[name]
                return
            case _:
                line_operations.cls()
                print(colors.bcolors.FAIL + 'Please input a correct option!' + colors.bcolors.ENDC)

# Let the user add or change a perk
def change_perk():
    choice = 0
    name = ''
    line_operations.cls()

    while True:
        print('Which perk slot do you want to modify?')
        choice = int(input('1-6 >'))

        match choice:
            case 1 | 2 | 3 | 4 | 5 | 6:
                name = input('Input the perk\'s name >')
                player.perks[choice] = name
                return
            case _:
                line_operations.cls()
                print(colors.bcolors.FAIL + 'Please input a correct option!' + colors.bcolors.ENDC)
                
# Let the user change one of their stats
def change_stats():
    choice = 0
    line_operations.cls()

    while True:
        print('Which stat do you want to change?')
        print('1. STR')
        print('2. DEX')
        print('3. INT')
        choice = int(input('>'))

        match choice:
            case 1:
                player.strength = int(input('Input new STR value >'))
                return
            case 2:
                player.dexterity = int(input('Input new DEX value >'))
                return
            case 3:
                player.intelligence = int(input('Input new INT value >'))
                return
            case _:
                line_operations.cls()
                print(colors.bcolors.FAIL + 'Please input a correct option!' + colors.bcolors.ENDC)

# Let the user change one of their stat proficiencies
def change_proficiency():
    choice = 0
    line_operations.cls()

    while True:
        print('Which stat proficiency do you want to change?')
        print('1. STR')
        print('2. DEX')
        print('3. INT')
        choice = int(input('>'))

        match choice:
            case 1:
                player.strprof = float(input('Input new STR proficiency value >'))
                return
            case 2:
                player.dexprof = float(input('Input new DEX proficiency value >'))
                return
            case 3:
                player.intprof = float(input('Input new INT proficiency value >'))
                return
            case _:
                line_operations.cls()
                print(colors.bcolors.FAIL + 'Please input a correct option!' + colors.bcolors.ENDC)

# Calculate player's stats based on their gear and perks
def calculate_stats():
    # Initialize stats
    player.hitpoints = 2
    player.stamina = 2
    player.armor = 0
    player.movespeedinc = 0
    player.movespeed = 7.5
    player.attspd = 1.01
    player.relspd = 1
    player.refire = 0
    player.critchance = 0.05
    player.critdmg = 2
    player.incdmg = 0
    player.adddmg = 0
    player.bonusdmg = 0
    player.dotrateup = 0
    player.burnrateup = 0
    player.bleedrateup = 0
    player.poisonrateup = 0
    player.frostrateup = 0
    player.dotup = 0
    player.burnup = 0
    player.bleedup = 0
    player.poisonup = 0
    player.frostup = 0

    # Calculate stat bonuses
    player.hitpoints += player.strength // 10
    player.stamina += player.dexterity // 10
    # player.mana += player.intelligence // 10

    # Calculate item modifiers
    # ------------------------
    # Add Weapon Stats
    player.movespeedinc += player.weapon.mspd
    player.attspd += player.weapon.attspd
    player.relspd += player.weapon.relspd
    player.refire += player.weapon.refire
    player.critchance += player.weapon.critchance
    player.critdmg += player.weapon.critdmg
    player.incdmg += player.weapon.incdmg
    player.adddmg += player.weapon.adddmg
    player.bonusdmg += player.weapon.bonusdmg
    player.dotrateup += player.weapon.dotrateup
    player.burnrateup += player.weapon.burnrateup
    player.bleedrateup += player.weapon.bleedrateup
    player.poisonrateup += player.weapon.poisonrateup
    player.frostrateup += player.weapon.frostrateup
    player.dotup += player.weapon.dotup
    player.burnup += player.weapon.burnup
    player.bleedup += player.weapon.bleedup
    player.poisonup += player.weapon.poisonup
    player.frostup += player.weapon.frostup

    # Add Offhand Stats
    if player.offhand.name != 'Empty':
        if player.weapon.types['Two-handed'] == 0 or player.offhand.condition == 'Bow':
            if player.weapon.types[player.offhand.condition] == 1:
                player.hitpoints += player.offhand.hp
                player.stamina += player.offhand.st
                player.armor += player.offhand.ar
                player.movespeedinc += player.offhand.mspd
                player.attspd += player.offhand.attspd
                player.relspd += player.offhand.relspd
                player.refire += player.offhand.refire
                player.critchance += player.offhand.critchance
                player.critdmg += player.offhand.critdmg
                player.incdmg += player.offhand.incdmg
                player.adddmg += player.offhand.adddmg
                player.bonusdmg += player.offhand.bonusdmg
                player.dotrateup += player.offhand.dotrateup
                player.burnrateup += player.offhand.burnrateup
                player.bleedrateup += player.offhand.bleedrateup
                player.poisonrateup += player.offhand.poisonrateup
                player.frostrateup += player.weapon.frostrateup
                player.dotup += player.offhand.dotup
                player.burnup += player.offhand.burnup
                player.bleedup += player.offhand.bleedup
                player.poisonup += player.offhand.poisonup
                player.frostup += player.weapon.frostup
    
    # Add Helmet Stats
    if player.helmet.name != 'Empty':
        if player.weapon.types[player.helmet.condition] == 1:
            player.hitpoints += player.helmet.hp
            player.stamina += player.helmet.st
            player.armor += player.helmet.ar
            player.movespeedinc += player.helmet.mspd
            player.attspd += player.helmet.attspd
            player.relspd += player.helmet.relspd
            player.refire += player.helmet.refire
            player.critchance += player.helmet.critchance
            player.critdmg += player.helmet.critdmg
            player.incdmg += player.helmet.incdmg
            player.adddmg += player.helmet.adddmg
            player.bonusdmg += player.helmet.bonusdmg
            player.dotrateup += player.helmet.dotrateup
            player.burnrateup += player.helmet.burnrateup
            player.bleedrateup += player.helmet.bleedrateup
            player.poisonrateup += player.helmet.poisonrateup
            player.frostrateup += player.weapon.frostrateup
            player.dotup += player.helmet.dotup
            player.burnup += player.helmet.burnup
            player.bleedup += player.helmet.bleedup
            player.poisonup += player.helmet.poisonup
            player.frostup += player.weapon.frostup

    # Add Body Stats
    if player.body.name != 'Empty':
        if player.weapon.types[player.body.condition] == 1:
            player.hitpoints += player.body.hp
            player.stamina += player.body.st
            player.armor += player.body.ar
            player.movespeedinc += player.body.mspd
            player.attspd += player.body.attspd
            player.relspd += player.body.relspd
            player.refire += player.body.refire
            player.critchance += player.body.critchance
            player.critdmg += player.body.critdmg
            player.incdmg += player.body.incdmg
            player.adddmg += player.body.adddmg
            player.bonusdmg += player.body.bonusdmg
            player.dotrateup += player.body.dotrateup
            player.burnrateup += player.body.burnrateup
            player.bleedrateup += player.body.bleedrateup
            player.poisonrateup += player.body.poisonrateup
            player.frostrateup += player.weapon.frostrateup
            player.dotup += player.body.dotup
            player.burnup += player.body.burnup
            player.bleedup += player.body.bleedup
            player.poisonup += player.body.poisonup
            player.frostup += player.weapon.frostup

    # Add Boots Stats
    if player.boots.name != 'Empty':
        if player.weapon.types[player.boots.condition] == 1:
            player.hitpoints += player.boots.hp
            player.stamina += player.boots.st
            player.armor += player.boots.ar
            player.movespeedinc += player.boots.mspd
            player.attspd += player.boots.attspd
            player.relspd += player.boots.relspd
            player.refire += player.boots.refire
            player.critchance += player.boots.critchance
            player.critdmg += player.boots.critdmg
            player.incdmg += player.boots.incdmg
            player.adddmg += player.boots.adddmg
            player.bonusdmg += player.boots.bonusdmg
            player.dotrateup += player.boots.dotrateup
            player.burnrateup += player.boots.burnrateup
            player.bleedrateup += player.boots.bleedrateup
            player.poisonrateup += player.boots.poisonrateup
            player.frostrateup += player.weapon.frostrateup
            player.dotup += player.boots.dotup
            player.burnup += player.boots.burnup
            player.bleedup += player.boots.bleedup
            player.poisonup += player.boots.poisonup
            player.frostup += player.weapon.frostup

    # Add Accessory Stats
    if player.accessory.name != 'Empty':
        if player.weapon.types[player.accessory.condition] == 1:
            player.hitpoints += player.accessory.hp
            player.stamina += player.accessory.st
            player.armor += player.accessory.ar
            player.movespeedinc += player.accessory.mspd
            player.attspd += player.accessory.attspd
            player.relspd += player.accessory.relspd
            player.refire += player.accessory.refire
            player.critchance += player.accessory.critchance
            player.critdmg += player.accessory.critdmg
            player.incdmg += player.accessory.incdmg
            player.adddmg += player.accessory.adddmg
            player.bonusdmg += player.accessory.bonusdmg
            player.dotrateup += player.accessory.dotrateup
            player.burnrateup += player.accessory.burnrateup
            player.bleedrateup += player.accessory.bleedrateup
            player.poisonrateup += player.accessory.poisonrateup
            player.frostrateup += player.weapon.frostrateup
            player.dotup += player.accessory.dotup
            player.burnup += player.accessory.burnup
            player.bleedup += player.accessory.bleedup
            player.poisonup += player.accessory.poisonup
            player.frostup += player.weapon.frostup

    # Multiply Move Speed by Move Speed Inc%
    player.movespeed *= 1 + player.movespeedinc
    calculate_nonstandardmods()
    calculate_perks()
    calculate_passives()

# Calculate passives
def calculate_passives():
    if player.klass == 'Deprived':
        if player.helmet.name == 'Empty' and player.body.name == 'Empty' and player.boots.name == 'Empty':
            player.strprof += 0.01
            player.dexprof += 0.01
            player.intprof += 0.01

    if player.klass == 'Warrior':
        player.attspd += 0.06 * player.hitpoints

    if player.klass == 'Knight':
        player.incdmg += 0.08 * player.armor

    '''if player.klass == 'Pyromancer':
        if player.weapon.types['Fire'] == 1:
            player.burnup += 1'''

# Calculate non-standard modifiers
def calculate_nonstandardmods():
    if player.boots.name == 'Peg Leg':
        player.movespeedinc += player.gold * 0.005
        player.movespeed = 7.5 * (1 + player.movespeedinc)
        
# Calculate perks
def calculate_perks():
    for perk in player.perks:
        if player.perks[perk] == 'Alacrity':
            player.attspd += 0.3
    for perk in player.perks:
        if player.perks[perk] == 'Agility':
            player.movespeedinc += 0.1
            player.movespeed = 7.5 * (1 + player.movespeedinc)
            player.attspd += player.movespeedinc
    for perk in player.perks:
        if player.perks[perk] == 'Lethality':
            player.critdmg += 1.5
    for perk in player.perks:
        if player.perks[perk] == 'Swagger':
            player.critchance = (player.critchance * 0.8) + 0.2

# Calculate player's DPS
def calculate_dps():
    global maindps
    maindps = 0
    global dotdps
    dotdps = 0
    global totaldps
    totaldps = 0

    # Main DPS calculation
    avgdmg = (player.weapon.mindmg + player.weapon.maxdmg) / 2 # Get average damage
    hitdmg = avgdmg + player.adddmg # Add Base Damage Bonuses
    hitdmg *= (1 + (player.weapon.upgradetier * player.weapon.upgradelevel)) # Add Upgrade Damage Bonuses
    hitdmg *= (1 + (player.strength * (player.weapon.strsc + player.strprof)) + (player.dexterity * (player.weapon.dexsc + player.dexprof)) + (player.intelligence * (player.weapon.intsc + player.intprof))) # Add Scaling Damage Bonuses
    hitdmg *= (1 + player.incdmg) # Add Increased Damage %
    hitdmg += player.bonusdmg # Add Bonus Damage
    critbonus = 1 - player.critchance + player.critchance * player.critdmg # Calculate Crit Bonus
    critdmg = hitdmg * critbonus # Calculate Average Hit taking into account Criticals
    generalaps = player.weapon.aps * player.attspd # Calculate the amount of shots fired per second
    firingtime = player.weapon.capacity / generalaps # Calculate the amount of time it takes to empty the magazine
    reloadingtime = player.weapon.relspd * player.relspd # Calculate the amount of time it takes to reload
    uptime = firingtime / (firingtime + reloadingtime) # Calculate the uptime
    maindps = generalaps * (1 + player.refire) * player.weapon.shots * critdmg * uptime # Calculate the basic hit DPS

    # DOT DPS calculation
    burndmg = critdmg * player.weapon.burndmg * (1 + player.dotup + player.burnup)
    bleeddmg = critdmg * player.weapon.bleeddmg * (1 + player.dotup + player.bleedup)
    poisondmg = critdmg * player.weapon.poisondmg * (1 + player.dotup + player.poisonup)
    frostdmg = critdmg * player.weapon.frostdmg * (1 + player.dotup + player.frostup)
    burntickrate = player.weapon.dottickrate * (1 + player.dotrateup + player.burnrateup)
    bleedtickrate = player.weapon.dottickrate * (1 + player.dotrateup + player.bleedrateup)
    poisontickrate = player.weapon.dottickrate * (1 + player.dotrateup + player.poisonrateup)
    frosttickrate = player.weapon.dottickrate * (1 + player.dotrateup + player.frostrateup)
    dotdps = (burndmg * burntickrate) + (bleeddmg * bleedtickrate) + (poisondmg * poisontickrate) + (frostdmg * frosttickrate)

    # Total DPS calculation
    totaldps = maindps + dotdps

# Display all the information
def main_loop():
    line_operations.cls()
    choice = 0
    
    calculate_stats()
    calculate_dps()

    mspd = format(player.movespeedinc, '.0%')
    aspd = format(player.attspd, '.0%')
    refc = format(player.refire, '.0%')
    critc = format(player.critchance, '.0%')
    critd = format(player.critdmg, '.0%')

    while True:
        print(f'{"CURRENT GEAR":40s}\t{"STATS":70s}\t{"PERKS":35s}\tDPS')
        print(f'Weapon: {f"{player.weapon.name} + {player.weapon.upgradelevel}":35s}\t{f"STR: {player.strength} | DEX: {player.dexterity} | INT: {player.intelligence}":70s}\t{f"Perk 1: {player.perks[1]}":35s}\t{colors.bcolors.OKBLUE}DPS (Main hits){colors.bcolors.ENDC}')
        print(f'Offhand: {player.offhand.name:35s}\t{f"HP: {player.hitpoints} | ARMOR: {player.armor} | STAMINA: {player.stamina}":70s}\t{f"Perk 2: {player.perks[2]}":35s}\t{colors.bcolors.OKBLUE}{format(maindps, ".2f")}{colors.bcolors.ENDC}')
        print(f'Helmet: {player.helmet.name:35s}\t{f"Movement Speed: {player.movespeed} (+{mspd})":70s}\t{f"Perk 3: {player.perks[3]}":35s}\t{colors.bcolors.OKGREEN}DPS (DOT){colors.bcolors.ENDC}')
        print(f'Body: {player.body.name:35s}\t{f"Attack Speed: {aspd} | Refire Chance: {refc}":70s}\t{f"Perk 4: {player.perks[4]}":35s}\t{colors.bcolors.OKGREEN}{format(dotdps, ".2f")}{colors.bcolors.ENDC}')
        print(f'Boots: {player.boots.name:35s}\t{f"Critical Chance: {critc}":70s}\t{f"Perk 5: {player.perks[5]}":35s}\t{colors.bcolors.WARNING}DPS (Total){colors.bcolors.ENDC}')
        print(f'Accessory: {player.accessory.name:35s}\t{f"Critical Multiplier: {critd}":70s}\t{f"Perk 6: {player.perks[6]}":35s}\t{colors.bcolors.WARNING}{format(totaldps, ".2f")}{colors.bcolors.ENDC}\n')

        print('OPTIONS')
        print('1. Change Equipment')
        print('2. Change Stats')
        print('3. Add or Change a Perk')
        print('4. Change Stat Proficiency')
        choice = int(input('>'))

        match choice:
            case 1:
                change_equip()
                break
            case 2:
                change_stats()
                break
            case 3:
                change_perk()
                break
            case 4:
                change_proficiency()
                break
            case _:
                line_operations.cls()
                print(colors.bcolors.FAIL + 'Please input a correct option!' + colors.bcolors.ENDC)

# Main program
def Main():
    initial_setup()
    while True:
        main_loop()

# Run the main program
Main()