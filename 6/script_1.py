def read_input():
    values = []
    with open('6/input.txt', 'r') as f:
        values = f.readlines()
    return [value.strip() for value in values]

def count_steps(dest_planet, start_planet, orbits, count = 0):
    if dest_planet == start_planet:
        return count

    planets = orbits[start_planet]
    if len(planets) == 0:
        return 0

    for planet in planets:
        new_count = count_steps(dest_planet, planet, orbits, count + 1)

        if new_count and new_count > 0:
            return new_count
    return 0

values = read_input()
orbits = {}
planets = set()

for value in values:
    planet1, planet2 = value.split(')')

    if planet1 not in orbits:
        orbits[planet1] = set()

    if planet2 not in orbits:
        orbits[planet2] = set()
    
    orbits[planet1].add(planet2)
    planets.add(planet1)
    planets.add(planet2)

count = 0
start_planet = 'COM'
for dest_planet in planets:
    result = count_steps(dest_planet, start_planet, orbits)
    print(f"From {start_planet} to reach {dest_planet} it takes {result} steps")
    count += result

print(f"Overall steps: {count}")