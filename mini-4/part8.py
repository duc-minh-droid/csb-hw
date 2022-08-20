from numpy import random as rd

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

for key, value in skills.items():
    print(f"{key}: {value['Name']}")
chose_skill = int(input("Choose skill by number: "))
current_skill = skills[f"Skill {chose_skill}"]
print(f"\nYou chose {current_skill['Name']}.")

current_level = chose_skill # can change
if current_level < current_skill['Minimum level']:
    print(f"Cannot deploy. Required level {current_skill['Minimum level']}")
else:
    current_hit_rate = rd.rand(1)
    if current_hit_rate < current_skill['Hit rate']:
        print(f"Damage: {current_skill['Damage']}")
    else:
        print('Missed.')
    