numbers = input().split()
text = input()

message = ""

for num in numbers:
    index = sum(int(digit) for digit in num)
    while index >= len(text):
        index -= len(text)

    message += text[index]
    text = text[:index] + text[index+1:]

print(message)
