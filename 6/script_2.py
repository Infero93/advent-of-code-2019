def read_input():
    values = []
    with open('6/input.txt', 'r') as f:
        values = f.readlines()
    return [value.strip() for value in values]

def count_steps(dest_planet, start_planet, orbits, route, count = 0):
    if dest_planet == start_planet:
        return count

    planets = orbits[start_planet]
    if len(planets) == 0:
        return 0

    for planet in planets:
        new_count = count_steps(dest_planet, planet, orbits, route, count + 1)

        if new_count and new_count > 0:
            route.add(planet)
            return new_count
    return 0

values = read_input()
orbits1 = {}
planets = set()

for value in values:
    planet1, planet2 = value.split(')')

    if planet1 not in orbits1:
        orbits1[planet1] = set()

    if planet2 not in orbits1:
        orbits1[planet2] = set()
    
    orbits1[planet1].add(planet2)

    planets.add(planet1)
    planets.add(planet2)

count = 0
start_planet = 'COM'
dest_planet_1 = 'YOU'
dest_planet_2 = 'SAN'

route_to_you = set()
route_to_san = set()

count_steps(dest_planet_1, start_planet, orbits1, route_to_you)
print(f"From {start_planet} to {dest_planet_1} route is: {route_to_you}")

count_steps(dest_planet_2, start_planet, orbits1, route_to_san)
print(f"From {start_planet} to {dest_planet_2} route is: {route_to_san}")

difference = route_to_you.symmetric_difference(route_to_san)
difference_size = len(difference)
answer = difference_size - 2
print(f"Difference: {difference} (size: {len(difference)})")
print(f"Answer: {answer}")