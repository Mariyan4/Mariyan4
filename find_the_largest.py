number = int(input())

number_str = str(number)

sorted_digits = sorted(number_str, reverse=True)

largest_number = ''.join(sorted_digits)

largest_number = int(largest_number)

print(largest_number)
