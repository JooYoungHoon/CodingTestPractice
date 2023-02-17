"""

    19 * 19 배열이 있다.

    연속해서 5개 이어져있는 색이 이김

    검은색은 1 흰색은 2
    안놓아져있는건 0

"""
import sys
from collections import deque


def dfs(arr, player, num, counter):
    dx = [0, 0, 1, -1, 1, 1, -1, -1]
    dy = [1, -1, 0, 0, 1, -1, -1, 1]
    visited = [[0] * 19 for _ in range(19)]
    point = []
    before_direction = None
    while player:
        ty, tx, direction = black.popleft()
        if direction is None:
            for x, y in zip(dx, dy):
                ny = ty + y
                nx = tx + x

                if ny < 0 or ny >= 19 or nx < 0 or ny >= 19:
                    continue

                if arr[ny][nx] == counter:
                    continue

                if arr[ny][nx] == 0:
                    continue

                if visited[ny][nx] == 0:
                    black.appendleft([ty, tx, [y, x]])
            continue
        else:
            if visited[ty][tx] == 0:
                visited[ty][tx] = 1
            if before_direction is None:
                point.append([ty, tx])
                before_direction = direction
            else:
                if before_direction != direction:
                    before_direction = None
                    point = []
                else:
                    ny = ty + direction[0]
                    nx = tx + direction[1]
                    visited[ny][nx] = visited[ty][tx] + 1
                    point.append([ny, nx])

        if visited[ty][tx] == 5:
            # player가 이긴경우
            return [point], 1

    return 0


def who_won(arr, p1, p2):
    p1_start, p1_won = dfs(arr, p1, 1, 2)
    p2_start, p2_won = dfs(arr, p2, 2, 1)
    if p1_won:
        point = p1_start
        won = 1
    if p2_won:
        point = p2_start
        won = 2

    return point, won


if __name__ == '__main__':

    board = []
    black = deque()
    white = deque()
    for y in range(19):
        board.append(list(map(int, sys.stdin.readline().split())))
        for x in range(19):
            if board[y][x] == 1:
                black.append([y, x, None])
            elif board[y][x] == 2:
                white.append([y, x, None])

    print(who_won(board, black, white))
