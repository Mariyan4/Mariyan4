n = int(input())

for number in range(n):
    number_eo= int(input())
    if  number_eo % 2 != 0:
        print(f"{number_eo} is odd!")
        break
else:
    print("All numbers are even.")