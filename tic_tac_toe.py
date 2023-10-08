field = [list(map(int, input().split())) for _ in range(3)]


def check_winner(player):
    for i in range(3):
        if all(field[i][j] == player for j in range(3)) or all(field[j][i] == player for j in range(3)):
            return True

    if all(field[i][i] == player for i in range(3)) or all(field[i][2 - i] == player for i in range(3)):
        return True

    return False


if check_winner(1):
    print("First player won")
elif check_winner(2):
    print("Second player won")
else:
    print("Draw!")
