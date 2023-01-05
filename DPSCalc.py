import line_operations, colors

class Player:
    stats = {'gold':0, 'hitpoints':2, 'soulhearts':0, 'armor':0, 'stamina':2, 'mana':2, 'movespeed':7.5, 'movespeedinc':0.0, 'attspd':1.01, 'relspd':1.0, 'refire':0.0, \
    'critchance':0.05, 'critmulti':2.0, 'incdmg':0.0, 'adddmg':0, 'bonusdmg':0, 'strprof':0.0, 'dexprof':0.0, 'intprof':0.0, \
    'dotup':0.0, 'burnup':0.0, 'bleedup':0.0, 'poisonup':0.0, 'frostup':0.0, 'dotrateup':0.0, 'burnrateup':0.0, 'bleedrateup':0.0, 'poisonrateup':0.0, 'frostrateup':0.0}

    # Inherit values from the chosen class
    def __init__(self, klass, inittrait):
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
        self.trait1 = inittrait
        self.trait2 = inittrait
        self.trait3 = inittrait
        self.trait4 = inittrait
        self.trait5 = inittrait
        self.trait6 = inittrait

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
    def __init__(self, name, uptier, uplevel, strsc, dexsc, intsc, mindmg, maxdmg, aps, shots, capacity, relspd, burndmg, bleeddmg, poisondmg, frostdmg, dottickrate, types = ['Unconditional'], stats = {}):
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
        self.dottickrate = dottickrate
        self.types = types
        self.stats = stats

class Item:
    def __init__(self, slot, name, conditions = ['Unconditional'], stats = {}):
        self.slot = slot
        self.name = name
        self.conditions = conditions
        self.stats = stats

class Trait:
    def __init__(self, name, conditions = ['Unconditional'], stats = {}):
        self.name = name
        self.conditions = conditions
        self.stats = stats

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
    player = Player(klass, alltraits['empty'])

# Perform the initial setup. A goal here would be to load in items from a file into a dictionary from which they'd be easily accessible.
def initial_setup():
    # Create an empty placeholder item
    itemempty = Item('Any', 'Empty')
    # Create an empty placeholder trait
    traitempty = Trait('Empty')
    # Create Magic Quiver
    item1 = Item('Offhand', 'Magic Quiver', ['Bow', 'Crossbow'], {'refire':0.2})
    # Create Molotov Cocktail
    weapon1 = Weapon('Molotov Cocktail', 0.13, 0, 0.0, 0.03, 0.01, 175, 200, 2, 1, 1, 0, 0.6, 0, 0, 0, 1, ['One-handed', 'Ranged', 'Physical', 'Unconditional'], {'burnup':0.75})
    # Create Alacrity Trait
    trait1 = Trait('Alacrity', ['Unconditional'], {'attspd':0.3})
    # Create Agility Trait
    trait2 = Trait('Agility', ['Unconditional'], {'movespeedinc':0.1})
    # Create Lethality Trait
    trait3 = Trait('Lethality', ['Unconditional'], {'critmulti':1.5})
    # Initialize Ranger's starting equipment manually
    rangerweapon = Weapon('Shortbow', 0.16, 0, 0.01, 0.03, 0.00, 150, 175, 2.75, 1, 1, 0, 0, 0, 0, 0, 0, ['Two-handed', 'Ranged', 'Physical', 'Bow', 'Unconditional'])
    rangerhelmet = Item('Helmet', 'Hunter Cap', ['Ranged'], {'attspd':0.1})
    rangerbody = Item('Body', 'Ranger Cloak')
    # Create dictionaries of all items and all perks manually
    global allitems
    allitems = {'empty' : itemempty, 'motail' : weapon1, 'shtbow' : rangerweapon, 'hutcap' : rangerhelmet, 'racloak' : rangerbody, 'maiver': item1}
    global alltraits
    alltraits = {'empty' : traitempty, 'alacrity':trait1, 'agility':trait2, 'lethality':trait3}
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
                player.weapon.uplevel = choice
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

# Let the user add or change a Trait
def change_trait():
    choice = 0
    name = ''
    line_operations.cls()

    while True:
        print('Which trait slot do you want to modify?')
        choice = int(input('1-6 >'))

        match choice:
            case 1:
                name = input('Input the trait\'s name >').lower()
                player.trait1 = alltraits[name]
                return
            case 2:
                name = input('Input the trait\'s name >').lower()
                player.trait2 = alltraits[name]
                return
            case 3:
                name = input('Input the trait\'s name >').lower()
                player.trait3 = alltraits[name]
                return
            case 4:
                name = input('Input the trait\'s name >').lower()
                player.trait4 = alltraits[name]
                return
            case 5:
                name = input('Input the trait\'s name >').lower()
                player.trait5 = alltraits[name]
                return
            case 6:
                name = input('Input the trait\'s name >').lower()
                player.trait6 = alltraits[name]
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
                player.stats['strprof'] = float(input('Input new STR proficiency value >'))
                return
            case 2:
                player.stats['dexprof'] = float(input('Input new DEX proficiency value >'))
                return
            case 3:
                player.stats['intprof'] = float(input('Input new INT proficiency value >'))
                return
            case _:
                line_operations.cls()
                print(colors.bcolors.FAIL + 'Please input a correct option!' + colors.bcolors.ENDC)

# Calculate player's stats based on their gear and Traits
def calculate_stats():
    # Initialize stats
    player.stats = {'gold':0, 'hitpoints':2, 'soulhearts':0, 'armor':0, 'stamina':2, 'mana':2, 'movespeed':7.5, 'movespeedinc':0.0, 'attspd':1.01, 'relspd':1.0, 'refire':0.0, \
    'critchance':0.05, 'critmulti':2.0, 'incdmg':0.0, 'adddmg':0, 'bonusdmg':0, 'strprof':0.0, 'dexprof':0.0, 'intprof':0.0, \
    'dotup':0.0, 'burnup':0.0, 'bleedup':0.0, 'poisonup':0.0, 'frostup':0.0, 'dotrateup':0.0, 'burnrateup':0.0, 'bleedrateup':0.0, 'poisonrateup':0.0, 'frostrateup':0.0}

    # Calculate stat bonuses
    player.stats['hitpoints'] += player.strength // 10
    player.stats['stamina'] += player.dexterity // 10
    player.stats['mana'] += player.intelligence // 10

    # Calculate item modifiers
    # ------------------------
    # Add Weapon Stats
    for stat in player.weapon.stats:
        player.stats[stat] += player.weapon.stats[stat]

    # Add Offhand Stats
    if player.offhand.name != 'Empty':
        if 'Two-handed' not in player.weapon.types or 'Bow' in player.weapon.types:
            for condition in player.offhand.conditions:
                if condition in player.weapon.types:
                    for stat in player.offhand.stats:
                        player.stats[stat] += player.offhand.stats[stat]
                    break
    
    # Add Helmet Stats
    if player.helmet.name != 'Empty':
        for condition in player.helmet.conditions:
            if condition in player.weapon.types:
                for stat in player.helmet.stats:
                    player.stats[stat] += player.helmet.stats[stat]
                break

    # Add Body Stats
    if player.body.name != 'Empty':
        for condition in player.body.conditions:
            if condition in player.weapon.types:
                for stat in player.body.stats:
                    player.stats[stat] += player.body.stats[stat]
                break

    # Add Boots Stats
    if player.boots.name != 'Empty':
        for condition in player.boots.conditions:
            if condition in player.weapon.types:
                for stat in player.boots.stats:
                    player.stats[stat] += player.boots.stats[stat]
                break

    # Add Accessory Stats
    if player.accessory.name != 'Empty':
        for condition in player.accessory.conditions:
            if condition in player.weapon.types:
                for stat in player.accessory.stats:
                    player.stats[stat] += player.accessory.stats[stat]
                break

    # Add Trait 1 Stats
    if player.trait1.name != 'Empty':
        for condition in player.trait1.conditions:
            if condition in player.weapon.types:
                for stat in player.trait1.stats:
                    player.stats[stat] += player.trait1.stats[stat]
                break

    # Add Trait 2 Stats
    if player.trait2.name != 'Empty':
        for condition in player.trait2.conditions:
            if condition in player.weapon.types:
                for stat in player.trait2.stats:
                    player.stats[stat] += player.trait2.stats[stat]
                break

    # Add Trait 3 Stats
    if player.trait3.name != 'Empty':
        for condition in player.trait3.conditions:
            if condition in player.weapon.types:
                for stat in player.trait3.stats:
                    player.stats[stat] += player.trait3.stats[stat]
                break

    # Add Trait 4 Stats
    if player.trait4.name != 'Empty':
        for condition in player.trait4.conditions:
            if condition in player.weapon.types:
                for stat in player.trait4.stats:
                    player.stats[stat] += player.trait4.stats[stat]
                break

    # Add Trait 5 Stats
    if player.trait5.name != 'Empty':
        for condition in player.trait5.conditions:
            if condition in player.weapon.types:
                for stat in player.trait5.stats:
                    player.stats[stat] += player.trait5.stats[stat]
                break

    # Add Trait 6 Stats
    if player.trait6.name != 'Empty':
        for condition in player.trait6.conditions:
            if condition in player.weapon.types:
                for stat in player.trait6.stats:
                    player.stats[stat] += player.trait6.stats[stat]
                break


    calculate_nonstandardmods()
    calculate_traits()
    calculate_passives()

    # Multiply Move Speed by Move Speed Inc%
    player.stats['movespeed'] *= 1 + player.stats['movespeedinc']

# Calculate passives
def calculate_passives():
    if player.klass == 'Deprived':
        if player.helmet.name == 'Empty' and player.body.name == 'Empty' and player.boots.name == 'Empty':
            player.stats['strprof'] += 0.01
            player.stats['dexprof'] += 0.01
            player.stats['intprof'] += 0.01

    if player.klass == 'Warrior':
        player.stats['attspd'] += 0.06 * player.stats['hitpoints']

    if player.klass == 'Knight':
        player.stats['incdmg'] += 0.08 * player.stats['armor']

    '''if player.klass == 'Pyromancer':
        if player.weapon.types['Fire'] == 1:
            player.burnup += 1'''

# Calculate non-standard modifiers
def calculate_nonstandardmods():
    if player.boots.name == 'Peg Leg':
        player.stats['movespeedinc'] += player.stats['gold'] * 0.005
        player.stats['movespeed'] = 7.5 * (1 + player.stats['movespeedinc'])
        
# Calculate Traits
def calculate_traits():
    if player.trait1.name == 'Agility' or player.trait2.name == 'Agility' or player.trait3.name == 'Agility' or player.trait4.name == 'Agility' or player.trait5.name == 'Agility' or player.trait6.name == 'Agility':
        player.stats['attspd'] += player.stats['movespeedinc']

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
    hitdmg = avgdmg + player.stats['adddmg'] # Add Base Damage Bonuses
    hitdmg *= (1 + (player.weapon.uptier * player.weapon.uplevel)) # Add Upgrade Damage Bonuses
    hitdmg *= (1 + (player.strength * (player.weapon.strsc + player.stats['strprof'])) + (player.dexterity * (player.weapon.dexsc + player.stats['dexprof'])) + \
    (player.intelligence * (player.weapon.intsc + player.stats['intprof']))) # Add Scaling Damage Bonuses
    hitdmg *= 1 + player.stats['incdmg'] # Add Increased Damage %
    hitdmg += player.stats['bonusdmg'] # Add Bonus Damage
    critbonus = 1 - player.stats['critchance'] + player.stats['critchance'] * player.stats['critmulti'] # Calculate Crit Bonus
    critdmg = hitdmg * critbonus # Calculate Average Hit taking into account Criticals
    generalaps = player.weapon.aps * player.stats['attspd'] # Calculate the amount of shots fired per second
    firingtime = player.weapon.capacity / generalaps # Calculate the amount of time it takes to empty the magazine
    reloadingtime = player.weapon.relspd * player.stats['relspd'] # Calculate the amount of time it takes to reload
    uptime = firingtime / (firingtime + reloadingtime) # Calculate the uptime
    maindps = generalaps * (1 + player.stats['refire']) * player.weapon.shots * critdmg * uptime # Calculate the basic hit DPS

    # DOT DPS calculation
    burndmg = critdmg * player.weapon.burndmg * (1 + player.stats['dotup'] + player.stats['burnup'])
    bleeddmg = critdmg * player.weapon.bleeddmg * (1 + player.stats['dotup'] + player.stats['bleedup'])
    poisondmg = critdmg * player.weapon.poisondmg * (1 + player.stats['dotup'] + player.stats['poisonup'])
    frostdmg = critdmg * player.weapon.frostdmg * (1 + player.stats['dotup'] + player.stats['frostup'])
    burntickrate = player.weapon.dottickrate * (1 + player.stats['dotrateup'] + player.stats['burnrateup'])
    bleedtickrate = player.weapon.dottickrate * (1 + player.stats['dotrateup'] + player.stats['bleedrateup'])
    poisontickrate = player.weapon.dottickrate * (1 + player.stats['dotrateup'] + player.stats['poisonrateup'])
    frosttickrate = player.weapon.dottickrate * (1 + player.stats['dotrateup'] + player.stats['frostrateup'])
    dotdps = (burndmg * burntickrate) + (bleeddmg * bleedtickrate) + (poisondmg * poisontickrate) + (frostdmg * frosttickrate)

    # Total DPS calculation
    totaldps = maindps + dotdps

# Display all the information
def main_loop():
    line_operations.cls()
    choice = 0
    
    calculate_stats()
    calculate_dps()

    playhp = player.stats['hitpoints']
    playarm = player.stats['armor']
    playsta = player.stats['stamina']
    playmspd = player.stats['movespeed']
    mspd = format(player.stats['movespeedinc'], '.0%')
    aspd = format(player.stats['attspd'], '.0%')
    refc = format(player.stats['refire'], '.0%')
    critc = format(player.stats['critchance'], '.0%')
    critd = format(player.stats['critmulti'], '.0%')

    while True:
        print(f'{"CURRENT GEAR":40s}\t{"STATS":70s}\t{"TRAITS":35s}\tDPS')
        print(f'Weapon: {f"{player.weapon.name} + {player.weapon.uplevel}":35s}\t{f"STR: {player.strength} | DEX: {player.dexterity} | INT: {player.intelligence}":70s}\t{f"Trait 1: {player.trait1.name}":35s}\t{colors.bcolors.OKBLUE}DPS (Main hits){colors.bcolors.ENDC}')
        print(f'Offhand: {player.offhand.name:35s}\t{f"HP: {playhp} | ARMOR: {playarm} | STAMINA: {playsta}":70s}\t{f"Trait 2: {player.trait2.name}":35s}\t{colors.bcolors.OKBLUE}{format(maindps, ".2f")}{colors.bcolors.ENDC}')
        print(f'Helmet: {player.helmet.name:35s}\t{f"Movement Speed: {playmspd} (+{mspd})":70s}\t{f"Trait 3: {player.trait3.name}":35s}\t{colors.bcolors.OKGREEN}DPS (DOT){colors.bcolors.ENDC}')
        print(f'Body: {player.body.name:35s}\t{f"Attack Speed: {aspd} | Refire Chance: {refc}":70s}\t{f"Trait 4: {player.trait4.name}":35s}\t{colors.bcolors.OKGREEN}{format(dotdps, ".2f")}{colors.bcolors.ENDC}')
        print(f'Boots: {player.boots.name:35s}\t{f"Critical Chance: {critc}":70s}\t{f"Trait 5: {player.trait5.name}":35s}\t{colors.bcolors.WARNING}DPS (Total){colors.bcolors.ENDC}')
        print(f'Accessory: {player.accessory.name:35s}\t{f"Critical Multiplier: {critd}":70s}\t{f"Trait 6: {player.trait6.name}":35s}\t{colors.bcolors.WARNING}{format(totaldps, ".2f")}{colors.bcolors.ENDC}\n')

        print('OPTIONS')
        print('1. Change Equipment')
        print('2. Change Stats')
        print('3. Add or Change a Trait')
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
                change_trait()
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