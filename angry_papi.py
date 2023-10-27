ratings = list(map(int, input().split(", ")))
entryPoint = int(input())
typeItems = input()

leftSum = sum(ratings[:entryPoint])
rightSum = sum(ratings[entryPoint + 1:])

if typeItems == "cheap":
    leftSum = sum(filter(lambda x: x < ratings[entryPoint], ratings[:entryPoint]))
    rightSum = sum(filter(lambda x: x < ratings[entryPoint], ratings[entryPoint + 1:]))
elif typeItems == "expensive":
    leftSum = sum(filter(lambda x: x >= ratings[entryPoint], ratings[:entryPoint]))
    rightSum = sum(filter(lambda x: x >= ratings[entryPoint], ratings[entryPoint + 1:]))

if leftSum >= rightSum:
    print(f"Left - {leftSum}")
else:
    print(f"Right - {rightSum}")
