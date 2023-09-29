word = input()
list_upper = []
letter = 0

for let in word:

    if let.isupper():
        list_upper.append(letter)

    letter += 1

print(list_upper)
