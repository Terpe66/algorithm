def find_min_sum(N, board, col_list, row, col, cur_sum, best_sum):
    for prev in range(row):
        if col_list[prev] == col:
            return 1000
    
    cur_sum += board[row][col]
    if cur_sum > best_sum:
        return 1000

    if row == N-1:
        return cur_sum

    col_list[row] = col
    for next_col in range(N):
        result = find_min_sum(N, board, col_list, row + 1, next_col, cur_sum, best_sum)
        if result < best_sum:
            best_sum = result

    return best_sum


for t in range(1, int(input()) + 1):
    N = int(input())
    board = [0] * N
    for i in range(N):
        board[i] = [int(ch) for ch in input().split()]
    
    col_list = [0] * N
    min_sum = 1000
    for col in range(N):
        result = find_min_sum(N, board, col_list, 0, col, 0, min_sum)
        if result < min_sum:
            min_sum = result

    print('#{t} {min_sum})
