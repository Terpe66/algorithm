import sys
sys.stdin = open("4880.txt")


right_win_condition = {'1': '2', '2': '3', '3': '1'}
def find_winner(card_list, left, right):
    if left == right:
        return left
    
    mid = (left + right) // 2
    left_winner = find_winner(card_list, left, mid)
    right_winner = find_winner(card_list, mid + 1, right)

    if right_win_condition[card_list[left_winner]] == card_list[right_winner]:
        return right_winner
    else:
        return left_winner

for t in range(1, int(input()) + 1):
    N = int(input())
    card_list = input().split()
    print(f"#{t} {find_winner(card_list, 0, N - 1) + 1}")
