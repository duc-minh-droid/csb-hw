#1
laptops = {
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 1200,
    'ASUS': 400
}

print(f"Total price: {laptops['ASUS']*5}")

#2
laptop = input("Input a brand: ")
qty = input('Input amount to buy: ')
print(f"Total price: {laptops[laptop] * qty}")

#3
store = {
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30
}

mergedStore = {}
for key, value in store.items():
    mergedStore[key] = {
        'quantity': value,
        'price': laptops[key]
    }

brand = input('Input a brand: ')
quantity = int(input('Input amount to buy: '))
print(f"Total price: {mergedStore[brand]['price'] * (quantity)}")

mergedStore[brand]['quantity'] -= quantity
print("Available products:")
for key, item in mergedStore.items():
    print(f"- {key}: {item['quantity']}")