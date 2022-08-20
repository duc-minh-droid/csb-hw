#1
prices = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400
}

quantities = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}

values = {}
for key, value in quantities.items():
    values[key] = value * prices[key]

print(f"Total value of available brands: ")
for key, value in values.items():
    print(f"- {key}: {value}")

#2
sum = 0
for value in values.values():
    sum += value
print(f"Total value of available items: {sum}")