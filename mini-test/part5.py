districts = ["BD", "BTL", "CG", "DD", "HBT"]
populations = [247100, 333300, 266800, 420900, 318000]

highest_value = 0
highest_index = populations[-1]
for index, value in enumerate(populations):
    if value > highest_value:
        highest_value = value
        highest_index = index

lowest_value = populations[-1]
lowest_index = -1
for index, value in enumerate(populations):
    if value < lowest_value:
        lowest_value = value
        lowest_index = index
        
# bai 1
print("Indices of: ")
print(f"- Most populated dist.: {highest_index}")
print(f"- Lease populated dist.: {lowest_index}")
# bai 2
print("Names of: ")
print(f"- Most populated dis.: {districts[highest_index]}")
print(f"- Least populated dis.: {districts[lowest_index]}")
