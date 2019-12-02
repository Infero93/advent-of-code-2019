from math import floor

sum = 0
with open('input.txt', 'r') as f:
    for number in f:
        mass = int(number)
        fuel = floor(mass / 3) - 2
        sum += fuel

        print(number)

print(sum)