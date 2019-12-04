valid_numbers = []
pairs = {'11', '22', '33', '44', '55', '66', '77', '88', '99'}

for number in range(156218, 652527 + 1):
    number_as_string = str(number)
    
    for pair in pairs:
        if pair in number_as_string:
            #print(f"Pair {pair} found in {number_as_string}")
            number_sorted = "".join(sorted([digit for digit in number_as_string]))
            #print(f"Sorted number {number_sorted}")
            if number_sorted == number_as_string:
                #print(f"Number {number} is sorted")
                valid_numbers.append(number)
    
print(len(set(valid_numbers)))