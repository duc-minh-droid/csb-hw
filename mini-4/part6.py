#1
character = {
    'Name': 'Light',
    'Age': 17,
    'Strengths': 8,
    'Defense': 10,
    'HP': 100,
    'Backpack': ['Shield', 'Bread Loaf'],
    'Gold': 100,
    'Level': 2
}

#2
character['Gold'] += 50
print(f"Gold: {character['Gold']}")

#3
character['Backpack'].append('Flint stone')
print(f"Backpack: {character['Backpack']}")