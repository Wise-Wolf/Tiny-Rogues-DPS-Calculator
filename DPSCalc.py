import line_operations

class Player:
    stats = {'hitpoints':2, 'soulhearts':0, 'armor':0, 'stamina':2, 'mana':2, 'movespeed':7.5, 'movespeedinc':0.0, 'attspd':1.01, 'relspd':1.0, 'refire':0.0, \
    'critchance':0.05, 'critmulti':2.0, 'incdmg':0.0, 'adddmg':0, 'bonusdmg':0, 'arbreak':0.0, 'shock':0.0, 'strprof':0.0, 'dexprof':0.0, 'intprof':0.0, \
    'dotup':0.0, 'burnup':0.0, 'bleedup':0.0, 'poisonup':0.0, 'frostup':0.0, 'dotrateup':0.0, 'burnrateup':0.0, 'bleedrateup':0.0, 'poisonrateup':0.0, 'frostrateup':0.0}

    gold = 0
    weaponstacks = 0
    hitpointsinc = 0
    soulheartsinc = 0
    armorinc = 0
    manainc = 0

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
        self.modifier = klass.empty
        self.trait1 = klass.empty
        self.trait2 = klass.empty
        self.trait3 = klass.empty
        self.trait4 = klass.empty
        self.trait5 = klass.empty
        self.trait6 = klass.empty

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

        self.empty = itemempty

        self.weapon = weapon

class Weapon:
    slot = 'Weapon'

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
                print('Please input a correct number corresponding to the class you\'re playing!')

    global player
    player = Player(klass)

# Perform the initial setup. A goal here would be to load in items from a file into a dictionary from which they'd be easily accessible.
def initial_setup():
    # Create an empty placeholder item
    itemempty = Item('Any', 'Empty')
    # Create Magic Quiver
    item1 = Item('Offhand', 'Magic Quiver', ['Bow', 'Crossbow'], {'refire':0.2})
    # Create Molotov Cocktail
    weapon1 = Weapon('Molotov Cocktail', 0.13, 0, 0.0, 0.03, 0.01, 175, 200, 2, 1, 1, 0, 0.6, 0, 0, 0, 1, ['One-handed', 'Ranged', 'Physical', 'Unconditional'], {'burnup':0.75})
    # Create Alacrity Trait
    trait1 = Item('Trait', 'Alacrity', ['Unconditional'], {'attspd':0.3})
    # Create Agility Trait
    trait2 = Item('Trait', 'Agility', ['Unconditional'], {'movespeedinc':0.1})
    # Create Lethality Trait
    trait3 = Item('Trait', 'Lethality', ['Unconditional'], {'critmulti':1.5})
    # Create Crappy Modifier
    modifier1 = Item('Modifier', 'Crappy', ['Unconditional'], {'incdmg':-0.1, 'attspd':-0.05})
    # Initialize Ranger's starting equipment manually
    rangerweapon = Weapon('Shortbow', 0.16, 0, 0.01, 0.03, 0.00, 150, 175, 2.75, 1, 1, 0, 0, 0, 0, 0, 0, ['Two-handed', 'Ranged', 'Physical', 'Bow', 'Unconditional'])
    rangerhelmet = Item('Helmet', 'Hunter Cap', ['Ranged'], {'attspd':0.1})
    rangerbody = Item('Body', 'Ranger Cloak')
    # Create dictionaries of all items and all perks manually
    global allitems
    allitems = {'empty' : itemempty, 'motail' : weapon1, 'shtbow' : rangerweapon, 'hutcap' : rangerhelmet, 'racloak' : rangerbody, 'maiver': item1, \
    'alacrity':trait1, 'agility':trait2, 'lethality':trait3, \
    'crappy':modifier1}
    initialize_classes()

# Let the user change a piece of their equipment
def change_equip():
    choice = 0
    name = ''

    while True:
        line_operations.cls()

        print('Which item do you want to swap?')
        print('1. Weapon')
        print('2. Offhand')
        print('3. Helmet')
        print('4. Body')
        print('5. Boots')
        print('6. Accessory')

        try:
            choice = int(input('>'))
        except:
            input('Please input a number!')

        if choice not in [1, 2, 3, 4, 5, 6]:
                input('Please input a correct option!')
        else:
            while True:
                line_operations.cls()
                name = input('Please input the name of the new item >').lower()

                if name not in allitems:
                    input('Item of this name does not exist!')
                else:
                    match choice:
                        case 1:
                            if allitems[name].slot != 'Weapon' and allitems[name].slot != 'Any':
                                print('That\'s not a weapon!')
                                input('Returning to menu...')
                            else:
                                player.weapon = allitems[name]

                                while True:
                                    try:
                                        choice = int(input('Input the weapon\'s current upgrade level >'))
                                        break
                                    except:
                                        input('Please input a number!')
                                        line_operations.delete_last_line()
                                        line_operations.delete_last_line()

                                player.weapon.uplevel = choice

                                while True:
                                    name = input('Input the weapon\'s modifier >').lower()
                                    if name not in allitems:
                                        input('Modifier of this name does not exist!')
                                        line_operations.delete_last_line()
                                        line_operations.delete_last_line()
                                    elif allitems[name].slot != 'Modifier' and allitems[name].slot != 'Any':
                                        input('That\'s not a modifier!')
                                        line_operations.delete_last_line()
                                        line_operations.delete_last_line()
                                    else:
                                        player.modifier = allitems[name]
                                        break

                            return
                        case 2:
                            if allitems[name].slot != 'Offhand' and allitems[name].slot != 'Any':
                                print('That\'s not an offhand!')
                                input('Returning to menu...')
                            else:
                                player.offhand = allitems[name]
                            return
                        case 3:
                            if allitems[name].slot != 'Helmet' and allitems[name].slot != 'Any':
                                print('That\'s not a helmet!')
                                input('Returning to menu...')
                            else:
                                player.helmet = allitems[name]
                            return
                        case 4:
                            if allitems[name].slot != 'Body' and allitems[name].slot != 'Any':
                                print('That\'s not a body!')
                                input('Returning to menu...')
                            else:
                                player.body = allitems[name]
                            return
                        case 5:
                            if allitems[name].slot != 'Boots' and allitems[name].slot != 'Any':
                                print('That\'s not boots!')
                                input('Returning to menu...')
                            else:
                                player.boots = allitems[name]
                            return
                        case 6:
                            if allitems[name].slot != 'Accessory' and allitems[name].slot != 'Any':
                                print('That\'s not an accessory!')
                                input('Returning to menu...')
                            else:
                                player.accessory = allitems[name]
                            return

# Let the user add or change a Trait
def change_trait():
    choice = 0
    name = ''

    while True:
        line_operations.cls()
        name = input('Input the trait\'s name >').lower()
        if name not in allitems:
            input('Trait of this name does not exist!')
        elif allitems[name].slot != 'Trait' and allitems[name].slot != 'Any':
            print('That\'s not a trait!')
            input('Returning to menu...')
            return
        else:
            while True:
                print('Which slot do you want to add this trait to?')
                try:
                    choice = int(input('1-6 >'))
                except:
                    input('Please input a number!')
                    line_operations.delete_last_line()

                match choice:
                    case 1:
                        player.trait1 = allitems[name]
                        return
                    case 2:
                        player.trait2 = allitems[name]
                        return
                    case 3:
                        player.trait3 = allitems[name]
                        return
                    case 4:
                        player.trait4 = allitems[name]
                        return
                    case 5:
                        player.trait5 = allitems[name]
                        return
                    case 6:
                        player.trait6 = allitems[name]
                        return
                    case _:
                        input('Please input a correct option!')
                        line_operations.delete_last_line()
                        line_operations.delete_last_line()
                        line_operations.delete_last_line()
                
# Let the user change one of their stats
def change_stats():
    choice = 0
    line_operations.cls()

    while True:
        print('Which stat do you want to change?')
        print('1. STR')
        print('2. DEX')
        print('3. INT')
        
        try:
            choice = int(input('>'))
        except:
            input('Please input a number!')

        match choice:
            case 1:
                try:
                    player.strength = int(input('Input new STR value >'))
                except:
                    input('Not a number! Returning to menu...')
                return
            case 2:
                try:
                    player.dexterity = int(input('Input new DEX value >'))
                except:
                    input('Not a number! Returning to menu...')
                return
            case 3:
                try:
                    player.intelligence = int(input('Input new INT value >'))
                except:
                    input('Not a number! Returning to menu...')
                return
            case _:
                line_operations.cls()
                print('Please input a correct option!')

# Let the user change one of their counters
def change_counters():
    choice = 0
    line_operations.cls()

    while True:
        print('Which counter do you want to change?')
        print('1. Hearts')
        print('2. Soul Hearts')
        print('3. Armor')
        print('4. Mana')
        print('5. Gold')
        print('6. Weapon Stacks')

        try:
            choice = int(input('>'))
        except:
            input('Please input a number!')
        
        match choice:
            case 1:
                while True:
                    line_operations.cls()
                    try:
                        print('How many extra hearts do you have?')
                        choice = int(input('>'))
                        break
                    except:
                        input('Please input a number!')
                player.hitpointsinc = choice
                return
            case 2:
                while True:
                    line_operations.cls()
                    try:
                        print('How many extra soul hearts do you have?')
                        choice = int(input('>'))
                        break
                    except:
                        input('Please input a number!')
                player.soulheartsinc = choice
                return
            case 3:
                while True:
                    line_operations.cls()
                    try:
                        print('How many extra armor points do you have?')
                        choice = int(input('>'))
                        break
                    except:
                        input('Please input a number!')
                player.armorinc = choice
                return
            case 4:
                while True:
                    line_operations.cls()
                    try:
                        print('How many extra mana points do you have?')
                        choice = int(input('>'))
                        break
                    except:
                        input('Please input a number!')
                player.manainc = choice
                return
            case 5:
                while True:
                    line_operations.cls()
                    try:
                        print('How much gold do you have?')
                        choice = int(input('>'))
                        break
                    except:
                        input('Please input a number!')
                player.gold = choice
                return
            case 6:
                while True:
                    line_operations.cls()
                    try:
                        print('How many weapon stacks do you have?')
                        choice = int(input('>'))
                        break
                    except:
                        input('Please input a number!')
                player.weaponstacks = choice
                return
            case _:
                line_operations.cls()
                print('Please input a correct option!')

# Calculate player's stats based on their gear and Traits
def calculate_stats():
    # Initialize stats
    player.stats = {'hitpoints':2, 'soulhearts':0, 'armor':0, 'stamina':2, 'mana':2, 'movespeed':7.5, 'movespeedinc':0.0, 'attspd':1.01, 'relspd':1.0, 'refire':0.0, \
    'critchance':0.05, 'critmulti':2.0, 'incdmg':0.0, 'adddmg':0, 'bonusdmg':0, 'arbreak':0.0, 'shock':0.0, 'strprof':0.0, 'dexprof':0.0, 'intprof':0.0, \
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

    # Add Modifier Stats
    if player.modifier.name != 'Empty':
        for stat in player.modifier.stats:
            player.stats[stat] += player.modifier.stats[stat]

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

    # Calculate Move Speed by multiplying it by Move Speed Inc%
    player.stats['movespeed'] *= 1 + player.stats['movespeedinc']

    # Calculate Player's Hearts, Soul Hearts, Armor, and Mana
    player.stats['hitpoints'] += player.hitpointsinc
    player.stats['soulhearts'] += player.soulheartsinc
    player.stats['armor'] += player.armorinc
    player.stats['mana'] += player.manainc

    # Cap Critical Chance at 100%
    if player.stats['critchance'] > 1:
        player.stats['critchance'] = 1
    
    # Cap Armor Break at 25%
    if player.stats['arbreak'] > 0.25:
        player.stats['arbreak'] = 0.25
    
    # Cap Shock at 24%
    if player.stats['shock'] > 0.24:
        player.stats['shock'] = 0.24

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
    finaldmg = critdmg * (1 + player.stats['arbreak'] + player.stats['shock'])
    generalaps = player.weapon.aps * player.stats['attspd'] # Calculate the amount of shots fired per second
    firingtime = player.weapon.capacity / generalaps # Calculate the amount of time it takes to empty the magazine
    reloadingtime = player.weapon.relspd * player.stats['relspd'] # Calculate the amount of time it takes to reload
    uptime = firingtime / (firingtime + reloadingtime) # Calculate the uptime
    maindps = generalaps * (1 + player.stats['refire']) * player.weapon.shots * finaldmg * uptime # Calculate the basic hit DPS

    # DOT DPS calculation
    burndmg = finaldmg * player.weapon.burndmg * (1 + player.stats['dotup'] + player.stats['burnup'])
    bleeddmg = finaldmg * player.weapon.bleeddmg * (1 + player.stats['dotup'] + player.stats['bleedup'])
    poisondmg = finaldmg * player.weapon.poisondmg * (1 + player.stats['dotup'] + player.stats['poisonup'])
    frostdmg = finaldmg * player.weapon.frostdmg * (1 + player.stats['dotup'] + player.stats['frostup'])
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
    playsh = player.stats['soulhearts']
    playarm = player.stats['armor']
    playsta = player.stats['stamina']
    playmp = player.stats['mana']
    playmspd = player.stats['movespeed']
    mspd = format(player.stats['movespeedinc'], '.0%')
    aspd = format(player.stats['attspd'], '.0%')
    refc = format(player.stats['refire'], '.0%')
    critc = format(player.stats['critchance'], '.0%')
    critd = format(player.stats['critmulti'], '.0%')

    while True:
        print(f'{"CURRENT GEAR":40s}\t{"STATS":70s}\t{"TRAITS":35s}\tDPS')
        if player.modifier.name == 'Empty':
            print(f'Weapon: {f"{player.weapon.name} + {player.weapon.uplevel}":35s}\t{f"STR: {player.strength} | DEX: {player.dexterity} | INT: {player.intelligence}":70s}\t{f"Trait 1: {player.trait1.name}":35s}\tDPS (Main hits)')
        else:
            print(f'Weapon: {f"{player.modifier.name} {player.weapon.name} + {player.weapon.uplevel}":35s}\t{f"STR: {player.strength} | DEX: {player.dexterity} | INT: {player.intelligence}":70s}\t{f"Trait 1: {player.trait1.name}":35s}\tDPS (Main hits)')

        print(f'Offhand: {player.offhand.name:35s}\t{f"HP: {playhp} | SOUL: {playsh} | ARMOR: {playarm}":70s}\t{f"Trait 2: {player.trait2.name}":35s}\t{format(maindps, ".2f")}')        
        
        print(f'Helmet: {player.helmet.name:35s}\t{f"STAMINA: {playsta} | MANA: {playmp}":70s}\t{f"Trait 3: {player.trait3.name}":35s}\tDPS (DOT)')
        
        print(f'Body: {player.body.name:35s}\t{f"Attack Speed: {aspd} | Refire Chance: {refc}":70s}\t{f"Trait 4: {player.trait4.name}":35s}\t{format(dotdps, ".2f")}')
        
        print(f'Boots: {player.boots.name:35s}\t{f"Crit Chance: {critc} | Crit Multiplier: {critd}":70s}\t{f"Trait 5: {player.trait5.name}":35s}\tDPS (Total)')
        
        print(f'Accessory: {player.accessory.name:35s}\t{f"Movement Speed: {playmspd} (+{mspd})":70s}\t{f"Trait 6: {player.trait6.name}":35s}\t{format(totaldps, ".2f")}\n')

        print('OPTIONS')
        print('1. Change Stats')
        print('2. Change Equipment')
        print('3. Add or Change a Trait')
        print('4. Change counters')
        choice = int(input('>'))

        match choice:
            case 1:
                change_stats()
                break
            case 2:
                change_equip()
                break
            case 3:
                change_trait()
                break
            case 4:
                change_counters()
                break
            case _:
                line_operations.cls()
                print('Please input a correct option!')

# Main program
def Main():
    initial_setup()
    while True:
        main_loop()

# Run the main program
Main()