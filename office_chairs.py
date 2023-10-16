def check_the_rooms(number_of_rooms):
    free_chairs = 0
    for number_of_rooms in range(1, number_of_rooms + 1):
        free_chairs_in_current_room, visitors = input().split()
        difference = len(free_chairs_in_current_room) - int(visitors)
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {number_of_rooms}")
        else:
            free_chairs += difference

    return free_chairs


count_of_rooms = int(input())
total_free_chair = check_the_rooms(count_of_rooms)
if total_free_chair >= 0:
    print(f"Game On, {total_free_chair} free chairs left")
