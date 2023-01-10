import line_operations, math, load_data

class Player:
    stats = {'hitpoints':2, 'soulhearts':0, 'armor':0, 'stamina':2, 'mana':2, 'movespeed':7.5, 'movespeedinc':0.0, 'attspd':1.01, 'relspd':1.0, 'refire':0.0, \
    'critchance':0.05, 'critmulti':2.0, 'incdmg':0.0, 'adddmg':0, 'bonusdmg':0, 'arbreak':0.0, 'shock':0.0, 'strprof':0.0, 'dexprof':0.0, 'intprof':0.0, 'manabonusinc': 0.0, \
    'dotup':0.0, 'burnup':0.0, 'bleedup':0.0, 'poisonup':0.0, 'frostup':0.0, 'dotrateup':0.0, 'burnrateup':0.0, 'bleedrateup':0.0, 'poisonrateup':0.0, 'frostrateup':0.0}

    gold = 0
    weaponstacks = 0
    armorstacks = 0
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
        self.traits = {'Trait 1' : klass.empty, 'Trait 2' : klass.empty, 'Trait 3' : klass.empty, 'Trait 4' : klass.empty, 'Trait 5' : klass.empty, 'Trait 6' : klass.empty}

# Perform the initial setup.
def initial_setup():
    
    choice = 0

    print('Loading data...')

    global allitems
    allitems = load_data.parse_data()
    
        # Let the user choose their starting class
    while True:
        line_operations.cls()
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
        try:
            choice = int(input('>'))
        except:
            print('Please input a number!')

        match choice:
            case 1:
                klass = allitems['deprived']
                break
            case 2:
                klass = allitems['the hero']
                break
            case 3:
                klass = allitems['warrior']
                break
            case 4:
                klass = allitems['ranger']
                break
            case 5:
                klass = allitems['sorcerer']
                break
            case 6:
                klass = allitems['wanderer']
                break
            case 7:
                klass = allitems['knight']
                break
            case 8:
                klass = allitems['thief']
                break
            case 9:
                klass = allitems['pyromancer']
                break
            case 10:
                klass = allitems['cleric']
                break
            case 11:
                klass = allitems['bandit']
                break
            case 12:
                klass = allitems['gunslinger']
                break
            case 99:
                klass = allitems['doppelganger']
                break
            case _:
                input('Please input a correct number corresponding to the class you\'re playing!')
    
    global player
    player = Player(klass)

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
            print('Please input a number!')

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
                            if allitems[name].slot != 'Weapon':
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
                    print('Please input a number!')
                    line_operations.delete_last_line()

                match choice:
                    case 1:
                        player.traits['Trait 1'] = allitems[name]
                        return
                    case 2:
                        player.traits['Trait 2'] = allitems[name]
                        return
                    case 3:
                        player.traits['Trait 3'] = allitems[name]
                        return
                    case 4:
                        player.traits['Trait 4'] = allitems[name]
                        return
                    case 5:
                        player.traits['Trait 5'] = allitems[name]
                        return
                    case 6:
                        player.traits['Trait 6'] = allitems[name]
                        return
                    case _:
                        input('Please input a correct option!')
                        line_operations.delete_last_line()
                        line_operations.delete_last_line()
                        line_operations.delete_last_line()
                
# Let the user change one of their stats
def change_stats():
    choice = 0

    while True:
        line_operations.cls()
        print('Which stat do you want to change?')
        print('1. STR')
        print('2. DEX')
        print('3. INT')
        
        try:
            choice = int(input('>'))
        except:
            print('Please input a number!')

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
                input('Please input a correct option!')

# Let the user change one of their counters
def change_counters():
    choice = 0

    while True:
        line_operations.cls()
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
            print('Please input a number!')
        
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
                input('Please input a correct option!')

# Calculate player's stats based on their gear and Traits
def calculate_stats():
    # Initialize stats
    player.stats = {'hitpoints':2, 'soulhearts':0, 'armor':0, 'stamina':2, 'mana':2, 'movespeed':7.5, 'movespeedinc':0.0, 'attspd':1.01, 'relspd':1.0, 'refire':0.0, \
    'critchance':0.05, 'critmulti':2.0, 'incdmg':0.0, 'adddmg':0, 'bonusdmg':0, 'arbreak':0.0, 'shock':0.0, 'strprof':0.0, 'dexprof':0.0, 'intprof':0.0, 'manabonusinc': 0.0, \
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
        if 'Two-handed' not in player.weapon.types or (('Bow' or 'Crossbow') in player.weapon.types):
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

    # Add Trait Stats
    for trait in player.traits:
        if player.traits[trait].name != 'Empty':
            for condition in player.traits[trait].conditions:
                if condition in player.weapon.types:
                    for stat in player.traits[trait].stats:
                        player.stats[stat] += player.traits[trait].stats[stat]
                    break

    # Calculate Player's Hearts, Soul Hearts, Armor, and Mana
    player.stats['hitpoints'] += player.hitpointsinc
    player.stats['soulhearts'] += player.soulheartsinc
    player.stats['armor'] += player.armorinc
    player.stats['mana'] += player.manainc

    calculate_nonstandardmods()
    calculate_traits()
    calculate_passives()

    # Calculate Mana Damage Bonus
    manaincdmg = 0.05 * (1 + player.stats['manabonusinc'])
    if 'Magic' in player.weapon.types:
        player.stats['incdmg'] += player.stats['mana'] * manaincdmg
    elif 'Elemental' in player.weapon.types:
        for trait in player.traits:
            if player.traits[trait].name == 'Power Of Nature':
                player.stats['incdmg'] += player.stats['mana'] * manaincdmg
                break

    # Calculate Reload Speed based on DEX
    player.stats['relspd'] += 0.25 * player.dexterity

    # Calculate Move Speed by multiplying it by Move Speed Inc%
    player.stats['movespeed'] *= 1 + player.stats['movespeedinc']

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
    for trait in player.traits:
        if player.traits[trait].name == 'Agility':
            player.stats['attspd'] += player.stats['movespeedinc']
        break

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
    finaldmg = critdmg * (1 + player.stats['arbreak'] + player.stats['shock']) # Calculate the amount of damage done to Armor Broken/Shocked enemies
    generalaps = player.weapon.aps * player.stats['attspd'] # Calculate the amount of shots fired per second
    reloadingtime = player.weapon.relspd * player.stats['relspd'] # Calculate the amount of time spent reloading
    attackinterval = 1 / generalaps # Calculate the Attack Interval
    adjustedaps = player.weapon.capacity / (player.weapon.capacity * attackinterval + max(0, (reloadingtime - attackinterval) * math.ceil((math.pi * reloadingtime) % 1))) # Calculate the Adjusted APS

    maindps = adjustedaps * (1 + player.stats['refire']) * player.weapon.shots * finaldmg  # Calculate the basic hit DPS

    # DOT DPS calculation
    if player.weapon.burndmg > 0:
        burndmg = finaldmg * player.weapon.burndmg * (1 + player.stats['dotup'] + player.stats['burnup'])
        burntickrate = player.weapon.dottickrate * (1 + player.stats['dotrateup'] + player.stats['burnrateup'])
        dotdps += burndmg * burntickrate

    if player.weapon.bleeddmg > 0:    
        bleeddmg = finaldmg * player.weapon.bleeddmg * (1 + player.stats['dotup'] + player.stats['bleedup'])
        bleedtickrate = player.weapon.dottickrate * (1 + player.stats['dotrateup'] + player.stats['bleedrateup'])
        dotdps += bleeddmg * bleedtickrate

    if player.weapon.poisondmg > 0:
        poisondmg = finaldmg * player.weapon.poisondmg * (1 + player.stats['dotup'] + player.stats['poisonup'])
        poisontickrate = player.weapon.dottickrate * (1 + player.stats['dotrateup'] + player.stats['poisonrateup'])
        dotdps += poisondmg * poisontickrate

    if player.weapon.frostdmg > 0:
        frostdmg = finaldmg * player.weapon.frostdmg * (1 + player.stats['dotup'] + player.stats['frostup'])
        frosttickrate = player.weapon.dottickrate * (1 + player.stats['dotrateup'] + player.stats['frostrateup'])
        dotdps += frostdmg * frosttickrate
    
    if player.weapon.specialdotdmg > 0:
        specialdotdmg = finaldmg * player.weapon.specialdotdmg * (1 + player.stats['dotup'])
        specialdottickrate = player.weapon.dottickrate * (1 + player.stats['dotrateup'])
        dotdps += specialdotdmg * specialdottickrate

    # Total DPS calculation
    totaldps = maindps + dotdps

# Display all the information
def main_loop():
    choice = 0
    
    calculate_stats()
    calculate_dps()

    trait1 = player.traits['Trait 1'].name
    trait2 = player.traits['Trait 2'].name
    trait3 = player.traits['Trait 3'].name
    trait4 = player.traits['Trait 4'].name
    trait5 = player.traits['Trait 5'].name
    trait6 = player.traits['Trait 6'].name

    weptypes = '/'.join(player.weapon.types[:-1])
    playhp = player.stats['hitpoints']
    playsh = player.stats['soulhearts']
    playarm = player.stats['armor']
    playsta = player.stats['stamina']
    playmp = player.stats['mana']
    playmspd = player.stats['movespeed']
    playadddmg = player.stats['adddmg']
    playbonusdmg = player.stats['bonusdmg']
    playdmginc = format(player.stats['incdmg'], '.0%')

    mspd = format(player.stats['movespeedinc'], '.0%')
    aspd = format(player.stats['attspd'], '.0%')
    refc = format(player.stats['refire'], '.0%')
    critc = format(player.stats['critchance'], '.0%')
    critd = format(player.stats['critmulti'], '.0%')

    while True:
        line_operations.cls()

        print(f'{"CURRENT GEAR":50s}\t{"STATS":70s}\t{"TRAITS":35s}\tDPS')

        print(f'{"------------":50s}\t{"-----":70s}\t{"------":35s}\t---')

        if player.modifier.name == 'Empty':
            print(f'Weapon: {f"{player.weapon.name} + {player.weapon.uplevel}":40s}\t{f"STR: {player.strength} | DEX: {player.dexterity} | INT: {player.intelligence}":70s}\t{f"Trait 1: {trait1}":35s}\tDPS (Main hits)')
        else:
            print(f'Weapon: {f"{player.modifier.name} {player.weapon.name} + {player.weapon.uplevel}":40s}\t{f"STR: {player.strength} | DEX: {player.dexterity} | INT: {player.intelligence}":70s}\t{f"Trait 1: {trait1}":35s}\tDPS (Main hits)')

        print(f'Types: {weptypes:45s}\t{f"HP: {playhp} | SOUL: {playsh} | ARMOR: {playarm}":70s}\t{f"Trait 2: {trait2}":35s}\t{format(maindps, ".2f")}')

        if 'Two-handed' not in player.weapon.types or (('Bow' or 'Crossbow') in player.weapon.types and (('Bow' or 'Crossbow') in player.offhand.conditions or player.offhand.name == 'Empty')):
            print(f'Offhand: {player.offhand.name:40s}\t{f"GOLD: {player.gold} | STAMINA: {playsta} | MANA: {playmp}":70s}\t{f"Trait 3: {trait3}":35s}\tDPS (DOT)')        
        else:
            print(f'Offhand: {f"{player.offhand.name} (Inactive - 2H Weapon Equipped.)":40s}\t{f"GOLD: {player.gold} | STAMINA: {playsta} | MANA: {playmp}":70s}\t{f"Trait 3: {trait3}":35s}\tDPS (DOT)')

        print(f'Helmet: {player.helmet.name:40s}\t{f"DMG INC%: {playdmginc} | ADD DMG: {playadddmg} | BONUS DMG: {playbonusdmg}":70s}\t{f"------":35s}\t{format(dotdps, ".2f")}')
        
        print(f'Body: {player.body.name:45s}\t{f"ATT SPD%: {aspd} | REFIRE%: {refc}":70s}\t{f"Trait 4: {trait4}":35s}\t{f"---"}')
        
        print(f'Boots: {player.boots.name:45s}\t{f"CRIT%: {critc} | CRIT MULTI%: {critd}":70s}\t{f"Trait 5: {trait5}":35s}\tDPS (Total)')
        
        print(f'Accessory: {player.accessory.name:40s}\t{f"MOVE SPD (INC%): {playmspd} (+{mspd})":70s}\t{f"Trait 6: {trait6}":35s}\t{format(totaldps, ".2f")}\n')

        print('OPTIONS')
        print('1. Change Stats')
        print('2. Change Equipment')
        print('3. Add or Change a Trait')
        print('4. Change counters')
        try:
            choice = int(input('>'))
        except:
            print('Please input a number!')

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
                input('Please input a correct option!')

# Main program
def Main():
    initial_setup()
    while True:
        main_loop()

# Run the main program
Main()