def attack(ship, index, damage):
    if index < 0 or index >= len(ship):
        return False
    ship[index] -= damage
    if ship[index] <= 0:
        print("You won! The enemy ship has sunken.")
        return True
    return False


def defend(ship, start, end, damage):
    if start < 0 or end >= len(ship) or start > end:
        return False
    for i in range(start, end + 1):
        ship[i] -= damage
        if ship[i] <= 0:
            print("You lost! The pirate ship has sunken.")
            return True
    return False


def repair(ship, section, health, max_hp):
    if section < 0 or section >= len(ship):
        return False
    ship[section] += health
    ship[section] = min(ship[section], max_hp)
    return True


def status(ship, max_hp):
    count = 0
    for sections in ship:
        if sections < 0.2 * max_hp:
            count += 1

    print(f"{count} sections need repair.")


pirate_ship = [int(x) for x in input().split('>')]
warship = [int(x) for x in input().split('>')]
max_health = int(input())

running = True
while running:
    command = input().split()

    if command[0] == "Retire":
        break

    if command[0] == "Fire":
        if attack(warship, int(command[1]), int(command[2])):
            running = False
            break
    elif command[0] == "Defend":
        if defend(pirate_ship, int(command[1]), int(command[2]), int(command[3])):
            running = False
            break
    elif command[0] == "Repair":
        repair(pirate_ship, int(command[1]), int(command[2]), max_health)
    elif command[0] == "Status":
        status(pirate_ship, max_health)

if running:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
