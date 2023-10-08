people = list(map(int, input().split()))
k = int(input())
executed = []
current = 0

while people:
    current = (current + k - 1) % len(people)
    executed.append(people.pop(current))

print(executed)