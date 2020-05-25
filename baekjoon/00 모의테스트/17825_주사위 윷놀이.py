import sys
sys.stdin = open("17825.txt")


def play_game(idx, point):
    global answer

    if idx == 10:
        if answer < point:
            answer = point
        return

    for h in range(4):
        if horse[h] == (4, 4):
            continue
        temp = horse[h]
        new = temp[1] + turns[idx]
        if temp[0] == 0:
            if new == 5:
                comp = (1, 0)
            elif new == 10:
                comp = (2, 0)
            elif new == 15:
                comp = (3, 0)
            elif new == 20:
                comp = (4, 3)
            elif new < 20:
                comp = (0, new)
            else:
                comp = (4, 4)
        elif temp[0] == 1:
            if new < 4:
                comp = (1, new)
            else:
                comp = (4, new - 4)
        elif temp[0] == 2:
            if new < 3:
                comp = (2, new)
            else:
                comp = (4, new - 3)
        elif temp[0] == 3:
            if new < 4:
                comp = (3, new)
            else:
                comp = (4, new - 4)
        else:
            if new < 4:
                comp = (4, new)
            else:
                comp = (4, 4)

        if comp in horse and comp != (4, 4):
            continue

        if comp == (4, 4):
            horse[h] = (4, 4)
            play_game(idx + 1, point)
            horse[h] = temp
            continue

        horse[h] = comp
        if comp[0] == 0:
            play_game(idx + 1, point + comp[1] * 2)
        elif comp[0] == 1:
            play_game(idx + 1, point + (10 + comp[1] * 3))
        elif comp[0] == 2:
            play_game(idx + 1, point + (20 + comp[1] * 2))
        elif comp[0] == 3:
            if comp[1] == 0:
                play_game(idx + 1, point + 30)
            else:
                play_game(idx + 1, point + (29 - comp[1]))
        elif comp[0] == 4:
            play_game(idx + 1, point + (25 + comp[1] * 5))
        horse[h] = temp
        pass


for T in range(int(input())):
    answer = 0
    turns = list(map(int, input().split()))
    horse = [(0, 0) for _ in range(4)]
    play_game(0, 0)

    print(answer)