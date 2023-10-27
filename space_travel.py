route_space = list(input().split('||'))
fuel_starting = int(input())
ammunition_starting = int(input())

for i in range(len(route_space)):
    command_list = route_space[i].split(' ')
    command = command_list[0]

    if command == 'Travel':
        distance = int(command_list[1])
        if fuel_starting >= distance:
            fuel_starting -= distance
            print(f'The spaceship travelled {distance} light-years.')
        else:
            print('Mission failed.')
            break
    elif command == 'Enemy':
        enemies_armour = int(command_list[1])
        if ammunition_starting >= enemies_armour:
            ammunition_starting -= enemies_armour
            print(f'An enemy with {enemies_armour} armour is defeated.')
        else:
            run = fuel_starting // 2
            if run > enemies_armour:
                fuel_starting -= enemies_armour * 2
                print(f'An enemy with {enemies_armour} armour is outmaneuvered.')
            else:
                print('Mission failed.')
                break
    elif command == 'Repair':
        ammunition_and_fuel = int(command_list[1])
        fuel_starting += ammunition_and_fuel
        ammunition_starting += ammunition_and_fuel * 2
        print(f'Ammunitions added: {ammunition_and_fuel * 2}.')
        print(f'Fuel added: {ammunition_and_fuel}.')
    elif command == 'Titan':
        print('You have reached Titan, all passengers are safe.')
        break
