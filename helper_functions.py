# Dictionary with model mappings for different manufacturers
MODEL_MAPPINGS = {
    'Boeing': {
        '737': '737', '747': '747', '757': '757', '767': '767',
        '777': '777', '787': '787', '727': '727', 'A75': 'A75',
        '717': '717', 'B75': 'B75', '707': '707'
    },
    'Airbus': {
        '319': 'A319', '320': 'A320', '321': 'A321', '330': 'A330'
    },
    'Embraer': {
        '170': 'ERJ-170', '175': 'ERJ-175', '190': 'ERJ-190', '195': 'ERJ-195',
        '110': 'EMB-110', '11O': 'EMB-110', '120': 'EMB-120', '135': 'EMB-135', '145': 'EMB-145'
    },
    'Mitsubishi': {
        '2B-10': 'MU-2D', '2B-15': 'MU-2DP', '2B-20': 'MU-2F', '2B-25': 'MU-2K',
        '2B-26': 'MU-2M', '2B-26A': 'MU-2P', '2B-40': 'Solitaire', '2B-30': 'MU-2G',
        '2B-35': 'MU-2J', '2B-36': 'MU-2L', '2B-60': 'Marquise'
    },
    'Bombardier': {
        '600': 'CL-600', '700': 'BD-700'
    },
    'Beechcraft': {
        '35': 'Bonanza', '55': 'Bonanza', '36': 'Bonanza', '33': 'Debonair',
        '24': 'Sierra', '58': 'Baron', 'C90': 'King Air', '390': 'Premier',
        '99': 'Airliner', '1900': 'Airliner', '45': 'Mentor - Military',
        '23': 'Musketeer', '200': 'Super King Air'
    },
    'Cessna': {
        '152': 'C-152', '172': 'Skyhawk', '150': 'C-150', '180': 'Skywagon', '185': 'Skywagon',
        '183': 'Skywagon', '182': 'Skylane', '140': 'C-140', '170': 'C-140', '177': 'Cardinal',
        '188': 'C-188', '210': 'Centurion', '201': 'Centurion', '21O': 'Centurion', '206': 'C-206',
        '401': 'C-401', '337': 'Skymaster', '336': 'Skymaster', '120': 'C-120', '145': 'C-145',
        '162': 'Skycatcher', '175': 'Skylark', '190': 'C-190', '195': 'C-195', '205': 'C-205',
        '207': 'C-207', '208': 'Caravan', '305': 'C-305', '31': 'C-310', '310': 'C-310',
        '320': 'Skyknight', '335': 'C-335', '340': 'C-340', '402': 'C-402', '404': 'Titan',
        '411': 'C-411', '414': 'C-414', '421': 'Golden Eagle', '425': 'C-425', '441': 'Conquest II',
        '500': 'Citation I', '501': 'Citation I', '510': 'Citation Mustang', '525': 'CitationJet',
        '550': 'Citation II', '551': 'Citation II', '560': 'Citation V', '650': 'Citation III',
        '680': 'Citation Sovereign', '750': 'Citation X', '0-1A': 'Bird Dog', 'L-19': 'Bird Dog',
        'L19': 'Bird Dog', 'T-50': 'Bobcat', 'T303': 'Crusader'
    },
    'Dassault': {
        '20': 'Falcon 20', '50': 'Falcon 50', '900': 'Falcon 900'
    },
    'Gulfstream': {
        '112': 'Rockwell Commander 112', '500': 'G500', '520': 'NASA Langley Gulfstream III',
        '681': 'G-V', '690': 'Twin Commander', '695': 'Twin Commander', 'AA-5': 'Grumman American AA-5',
        'AA5': 'Grumman American AA-5', 'IV': 'G-IV', 'V': 'G-V', '1159': 'Grumman Gulfstream II',
        '159': 'Grumman Gulfstream I', '164': 'Grumman Ag-Cat'
    },
    'Pilatus': {
        '12': 'PC-12', '05': 'P3'
    },
    'Hawker': {
        '58': 'Hunter 58'
    },
    'Bell': {
        '206': '206', '47-B': '47B', '47G': '47G', '47-G': '47G', '47D': '47D', '47J': '47J',
        'UH-1': 'UH-1', '407': '407', '222': '222', '212': '212', '412': '412', '205': '205',
        'OH-58': 'OH-58', 'OH 58': 'OH-58', 'OH58': 'OH-58', '204': '204', '214': '214', '74': 'OH-13',
        '13': 'OH-13', '39': 'P-39', 'UH': 'UH-1'
    },
    'Robinson': {
        '22': 'R-22', 'Beta': 'R-22', '44': 'R-44', '66': 'R-66'
    }
}


def update_model(row):
    make = row['Make']
    model = row['Model']
    if make in MODEL_MAPPINGS:
        for key, value in MODEL_MAPPINGS[make].items():
            if key in model:
                return value
    return model  # Handle the other manufacturers
