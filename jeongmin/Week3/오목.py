"""

    19 * 19 배열이 있다.

    연속해서 5개 이어져있는 색이 이김

    검은색은 1 흰색은 2
    안놓아져있는건 0

"""
import sys
from collections import deque


def who_won(arr):
    # direction [x, y]
    dx = [1, 1, -1, 0]
    dy = [0, 1, 1, 1]

    for idx, idy in zip(dx, dy):
        visited = [[0] * 19 for _ in range(19)]
        if idy == 1 and idx == 1:
            area_y = range(15)
            area_x = range(15)
        if idy == 1 and idx == 0:
            area_y = range(15)
            area_x = range(19)
        if idy == 0 and idx == 1:
            area_y = range(19)
            area_x = range(15)
        if idy == 1 and idx == -1:
            area_y = range(15)
            area_x = range(4, 19)
        for i in area_y:
            for j in area_x:
                if arr[i][j] == 1:
                    count = 0
                    point = [i, j]
                    ty = i
                    tx = j
                    while 0 <= ty < 19 and 0 <= tx < 19:
                        if arr[ty][tx] != 1:
                            break
                        if visited[ty][tx] == 1:
                            break
                        else:
                            visited[ty][tx] = 1
                            ty += idy
                            tx += idx
                            count += 1

                    if count == 5:
                        if idx == -1 and idy == 1:
                            point = [ty - 1, tx + 1]
                        return point, 1
                elif arr[i][j] == 2:
                    count = 0
                    point = [i, j]
                    ty = i
                    tx = j
                    while 0 <= ty < 19 and 0 <= tx < 19:
                        if arr[ty][tx] != 2:
                            break
                        if visited[ty][tx] == 1:
                            break
                        else:
                            visited[ty][tx] = 1
                            ty += idy
                            tx += idx
                            count += 1
                    if count == 5:
                        if idx == -1 and idy == 1:
                            point = [ty - 1, tx + 1]
                        return point, 2

    return None, 0


if __name__ == '__main__':

    board = []
    black = deque()
    white = deque()
    for y in range(19):
        board.append(list(map(int, sys.stdin.readline().split())))

    start_point, player = who_won(board)
    if start_point is None:
        print(player)
    else:
        start_point = list(map(str, map(lambda a: a + 1, start_point)))
        print(player)
        print(' '.join(start_point))
