#1
laptops = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}

#2
print(f"Available MACBOOKs: {laptops['MACBOOK']}")

#3
laptop = input('Input a brand: ')
print(f"Available {laptop}: {laptops[laptop]}")
