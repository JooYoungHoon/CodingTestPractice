"""

    [Baekjoon] https://www.acmicpc.net/problem/3187

    같은 울타리 영역 안의 양들의 숫자가 늑대의 숫자보다 더 많을 경우 늑대가 전부 잡아 먹힌다.

    늑대의 숫자가 더 많거나 같으면 늑대가 양을 잡아먹는다.


"""
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

S = 'k'
W = 'v'
B = '#'


def dfs(graph, visited, wolf_r, wolf_c, count_s, count_w, row_size, col_size):
    if graph[wolf_r][wolf_c] == W:
        count_w += 1
    if graph[wolf_r][wolf_c] == S:
        count_s += 1

    visited[wolf_r][wolf_c] = 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for idx, idy in zip(dx, dy):
        ny = wolf_r + idy
        nx = wolf_c + idx
        if visited[ny][nx]:
            continue
        if ny < 0 or ny >= row_size or nx < 0 or nx >= col_size:
            continue
        if graph[ny][nx] == B:
            continue
        count_s_idx, count_w_idy = dfs(graph, visited, ny, nx, 0, 0, row_size, col_size)
        count_s += count_s_idx
        count_w += count_w_idy

    return count_s, count_w


def solve(graph, w, count_s, count_w, row_size, col_size):
    visited = [[0] * col_size for _ in range(row_size)]

    while w:
        wolf_r, wolf_c = w.popleft()

        if not visited[wolf_r][wolf_c]:
            count_s_in_barrier, count_w_in_barrier = dfs(graph, visited, wolf_r, wolf_c, 0, 0, row_size, col_size)

            if count_w_in_barrier >= count_s_in_barrier:
                count_s -= count_s_in_barrier
            else:
                count_w -= count_w_in_barrier

    return count_s, count_w


if __name__ == '__main__':
    R, C = map(int, input().split())

    # 양의 수 늑대의 수
    count_S = 0
    count_W = 0

    wolf = deque()
    board = []
    for i in range(R):
        board.append(list(input()))
        for j in range(C):
            # 양인 경우
            if board[i][j] == S:
                count_S += 1
            elif board[i][j] == W:
                count_W += 1
                wolf.append([i, j])

    remain_S, remain_W = solve(board, wolf, count_S, count_W, R, C)

    print(f'{remain_S} {remain_W}')
