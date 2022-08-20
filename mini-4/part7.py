#1
skills = {
    'Skill 1': {
        'Name': 'Tackle',
        'Minimum level': 1,
        'Damage': 5,
        'Hit rate': 0.3
    },
    'Skill 2': {
        'Name': 'Quick Attack',
        'Minimum level': 2,
        'Damage': 3,
        'Hit rate': 0.5
    },
    'Skill 3': {
        'Name': 'Strong Kick',
        'Minimum level': 4,
        'Damage': 9,
        'Hit rate': 0.2
    }
}

#2
for key, value in skills.items():
    print(f"{key}: {value['Name']}")