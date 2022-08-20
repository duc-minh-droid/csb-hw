#1
laptops = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400
}

#2
print(f"Price of ASUS: {laptops['ASUS']}")

#3
laptop = input("Input a brand: ")
print(f"Price of {laptop}: {laptops[laptop]}")