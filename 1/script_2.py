from math import floor

def calc_fuel(mass):
    return floor(mass / 3) - 2

fuel_list = []
mass_list = []
with open('input.txt', 'r') as f:
    for number in f:
        mass = int(number)
        mass_list.append(int(number))

while len(mass_list) > 0:
    
    mass = mass_list.pop()
    fuel = calc_fuel(mass)
    if fuel > 0:
        mass_list.append(fuel)
        fuel_list.append(fuel)

    print(f"Mass: {mass}")
    print(f"Fuel: {fuel}")
    print()

print(sum(fuel_list))