import math

budget = float(input())
students = int(input())
flourPrice = float(input())
eggPrice = float(input())
apronPrice = float(input())
freePackages = 0

flourPackages = students
for flourPackages in range(1, students + 1):
    if flourPackages % 5 == 0:
        freePackages += 1

eggs = 10.0 * students
aprons = math.ceil(students * 1.2)

totalCost = flourPrice * (flourPackages - freePackages) + eggs * eggPrice + aprons * apronPrice

if totalCost <= budget:
    print(f"Items purchased for {totalCost:.2f}$.")
else:
    print(f"{totalCost - budget:.2f}$ more needed.")
