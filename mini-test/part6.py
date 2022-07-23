districts = ["BD", "BTL", "CG", "DD", "HBT"]
populations = [247100, 333300, 266800, 420900, 318000]
mass = [9.224, 43.35, 12.04, 9.96, 10.09]
density = []

for i in range(len(populations)):
    dens = float(populations[i]) / mass[i]
    density.append(dens)
# bai 1
print("Population density of: ")
for i in range(len(districts)):
    print(f"- {districts[i]}: {density[i]}")

# bai 2
sum = 0
for i in density:
    sum+= i
average_density = sum / float(len(districts))
print(f"Average population density: {average_density}")