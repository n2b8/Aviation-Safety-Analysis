from pyexpat import model


def update_boeing_model(model):
    if '737' in model:
        return '737'
    elif '747' in model:
        return '747'
    elif '757' in model:
        return '757'
    elif '767' in model:
        return '767'
    elif '777' in model:
        return '777'
    elif '787' in model:
        return '787'
    elif '727' in model:
        return '727'
    elif 'A75' in model:
        return 'A75'
    elif '717' in model:
        return '717'
    elif 'B75' in model:
        return 'B75'
    elif '707' in model:
        return '707'
    else:
        return model

def update_airbus_model(model):
    if '319' in model:
        return 'A319'
    elif '320' in model:
        return 'A320'
    elif '321' in model:
        return 'A321'
    elif '330' in model:
        return 'A330'
    else:
        return model

def update_embraer_commercial_model(model):
    if '170' in model:
        return 'ERJ-170'
    elif '175' in model:
        return 'ERJ-175'
    elif '190' in model:
        return 'ERJ-190'
    elif '195' in model:
        return 'ERJ-195'
    else:
        return model

def update_mitsubishi_model(model):
    if '2B-10' in model:
        return 'MU-2D'
    elif '2B-15' in model:
        return 'MU-2DP'
    elif '2B-20' in model:
        return 'MU-2F'
    elif '2B-25' in model:
        return 'MU-2K'
    elif '2B-26' in model:
        return 'MU-2M'
    elif '2B-26A' in model:
        return 'MU-2P'
    elif '2B-40' in model:
        return 'Solitaire'
    elif '2B-30' in model:
        return 'MU-2G'
    elif '2B-35' in model:
        return 'MU-2J'
    elif '2B-36' in model:
        return 'MU-2L'
    elif '2B-60' in model:
        return 'Marquise'
    else:
        return model


def update_bombardier_model(model):
    if '600' in model:
        return 'CL-600'
    elif '700' in model:
        return 'BD-700'
    else:
        return model

def update_beechcraft_model(model):
    if '35' in model or '55' in model or '36' in model:
        return 'Bonanza'
    elif '33' in model:
        return 'Debonair'
    elif '24' in model:
        return 'Sierra'
    elif '58' in model:
        return 'Baron'
    elif 'C90' in model:
        return 'King Air'
    elif '390' in model:
        return 'Premier'
    elif '99' in model or '1900' in model:
        return 'Airliner'
    elif '45' in model:
        return 'Mentor - Military'
    elif '23' in model:
        return 'Musketeer'
    elif '200' in model:
        return 'Super King Air'
    else:
        return model

# def update_cessna_model(model):
#     if '152' in model:
#         return 'C-152'
#     elif '172' in model:
#         return 'Skyhawk'
#     elif '150' in model:
#         return 'C-150'
#     elif '180' in model or '185' in model or '183' in model:
#         return 'Skywagon'
#     elif '182' in model:
#         return 'Skylane'
#     elif '140' in model:
#         return 'C-140'
#     elif '170' in model:
#         return 'C-140'
#     elif '177' in model:
#         return 'Cardinal'
#     elif '188' in model:
#         return 'C-188'
#     elif '210' in model or '201' in model or '21O' in model:
#         return 'Centurion'
#     elif '206' in model:
#         return 'C-206'
#     elif '401' in model:
#         return 'C-401'
#     elif '337' in model or '336' in model:
#         return 'Skymaster'
#     elif '120' in model:
#         return 'C-120'
#     elif '145' in model:
#         return 'C-145'
#     elif '162' in model:
#         return 'Skycatcher'
#     elif '175' in model:
#         return 'Skylark'
#     elif '190' in model:
#         return 'C-190'
#     elif '195' in model:
#         return 'C-195'
#     elif '205' in model:
#         return 'C-205'
#     elif '207' in model:
#         return 'C-207'
#     elif '208' in model:
#         return 'Caravan'
#     elif '305' in model:
#         return 'C-305'
#     elif '31' in model or '310' in model:
#         return 'C-310'
#     elif '320' in model:
#         return 'Skyknight'
#     elif '335' in model:
#         return 'C-335'
#     elif '340' in model:
#         return 'C-340'
#     elif '402' in model:
#         return 'C-402'
#     elif '404' in model:
#         return 'Titan'
#     elif '411' in model:
#         return 'C-411'
#     elif '414' in model:
#         return 'C-414'
#     elif '421' in model:
#         return 'Golden Eagle'
#     elif '425' in model:
#         return 'C-425'
#     elif '441' in model:
#         return 'Conquest II'
#     elif '500' in model or '501' in model:
#         return 'Citation I'
#     elif '510' in model:
#         return 'Citation Mustang'
#     elif '525' in model:
#         return 'CitationJet'
#     elif '550' in model or '551' in model:
#         return 'Citation II'
#     elif '560' in model:
#         return 'Citation V'
#     elif '650' in model:
#         return 'Citation III'
#     elif '680' in model:
#         return 'Citation Sovereign'
#     elif '750' in model:
#         return 'Citation X'
#     elif '0-1A' in model or 'L-19' in model or 'L19' in model:
#         return 'Bird Dog'
#     elif 'T-50' in model:
#         return 'Bobcat'
#     elif 'T303' in model:
#         return 'Crusader'
#     else:
#         return model

def update_cessna_model(model):
    model_mappings = {
        '152': 'C-152',
        '172': 'Skyhawk',
        '150': 'C-150',
        '180': 'Skywagon', '185': 'Skywagon', '183': 'Skywagon',
        '182': 'Skylane',
        '140': 'C-140', '170': 'C-140',
        '177': 'Cardinal',
        '188': 'C-188',
        '210': 'Centurion', '201': 'Centurion', '21O': 'Centurion',
        '206': 'C-206',
        '401': 'C-401',
        '337': 'Skymaster', '336': 'Skymaster',
        '120': 'C-120',
        '145': 'C-145',
        '162': 'Skycatcher',
        '175': 'Skylark',
        '190': 'C-190',
        '195': 'C-195',
        '205': 'C-205',
        '207': 'C-207',
        '208': 'Caravan',
        '305': 'C-305',
        '31': 'C-310', '310': 'C-310',
        '320': 'Skyknight',
        '335': 'C-335',
        '340': 'C-340',
        '402': 'C-402',
        '404': 'Titan',
        '411': 'C-411',
        '414': 'C-414',
        '421': 'Golden Eagle',
        '425': 'C-425',
        '441': 'Conquest II',
        '500': 'Citation I', '501': 'Citation I',
        '510': 'Citation Mustang',
        '525': 'CitationJet',
        '550': 'Citation II', '551': 'Citation II',
        '560': 'Citation V',
        '650': 'Citation III',
        '680': 'Citation Sovereign',
        '750': 'Citation X',
        '0-1A': 'Bird Dog', 'L-19': 'Bird Dog', 'L19': 'Bird Dog',
        'T-50': 'Bobcat',
        'T303': 'Crusader'
    }

    for key, value in model_mappings.items():
        if key in model:
            return value
    return model


def update_dassault_model(model):
    if '20' in model:
        return 'Falcon 20'
    elif '50' in model:
        return 'Falcon 50'
    elif '900' in model:
        return 'Falcon 900'
    else:
        return model

def update_embraer_private_model(model):
    return

def update_gulfstream_model(model):
    if '112' in model:
        return 'Rockwell Commander 112'
    elif '500' in model:
        return 'G500'
    elif '520' in model:
        return 'NASA Langley Gulfstream III'
    elif '681' in model:
        return 'G-V'
    elif '690' in model or '695' in model:
        return 'Twin Commander'
    elif 'AA-5' in model or 'AA5' in model:
        return 'Grumman American AA-5'
    else:
        return model

def update_pilatus_model(model):
    return

def update_hawker_model(model):
    return

def update_model(row):
    if row['Make'] == 'Mitsubishi':
        return update_mitsubishi_model(row['Model'])
    elif row['Make'] == 'Boeing':
        return update_boeing_model(row['Model'])
    elif row['Make'] == 'Airbus':
        return update_airbus_model(row['Model'])
    elif row['Make'] == 'Embraer':
        return update_embraer_commercial_model(row['Model'])
    elif row['Make'] == 'Bombardier':
        return update_bombardier_model(row['Model'])
    elif row['Make'] == 'Beechcraft':
        return update_beechcraft_model(row['Model'])
    elif row['Make'] == 'Cessna':
        return update_cessna_model(row['Model'])
    elif row['Make'] == 'Dassault':
        return update_dassault_model(row['Model'])
    elif row['Make'] == 'Gulfstream':
        return update_gulfstream_model(row['Model'])
    else:
        return row['Model']  # Handle the 'Other' or default case





#%%
