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