valid_numbers = []
pairs = ['11', '22', '33', '44', '55', '66', '77', '88', '99']
wrong = {}

for pair in pairs:
    digit = pair[0]
    wrong[pair] = [digit * n for n in range(3, 8)]

for number in range(156218, 652527 + 1):
    number_as_string = str(number)
    
    for pair in pairs:
        if pair in number_as_string:
            not_found = True
            for wrong_pair in wrong[pair]:
                if wrong_pair in number_as_string:
                    not_found = False
                    break
            
            if not_found:
                number_sorted = "".join(sorted([digit for digit in number_as_string]))
                if number_sorted == number_as_string:
                    valid_numbers.append(number)
    
print(len(set(valid_numbers)))