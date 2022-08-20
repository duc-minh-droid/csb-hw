#1
laptops = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}
laptops['TOSHIBA'] = 10

print("Available products:")
for key, value in laptops.items():
    print(f"- {key}: {value}")
    
#2
laptop = input("Input a brand")
qty = input("Input amount: ")
laptops[laptop] = qty

print("Available products:")
for key, value in laptops.items():
    print(f"- {key}: {value}")
    
#3
laptops = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}

laptops['MACBOOK'] = 2
laptops['DELL'] = 60

print("Available products:")
for key, value in laptops.items():
    print(f"- {key}: {value}")

#4
laptops = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}
sum = 0
for qty in laptops.values():
    sum += qty
print(f"Total products: {sum}")