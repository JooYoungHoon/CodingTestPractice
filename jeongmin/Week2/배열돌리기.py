"""

    재귀적 호출을 사용

    n => 2k + 1
    i 로 나타내서 연속적 숫자로 나타내기

    테두리를 step(i)만큼 이동시키면 됨.

    해당 점에 있는 좌표 값들을 구해

    차례대로 옮겨주는 연산을 실행

    45도 회전


"""


def find_outlier(k, arr_size):
    """ 테두리 찾기 """
    n = 2 * k + 1
    gap = arr_size - k
    move = [1, 1]
    x = list(range(0, n, k))

    idx = [[j + move[0] * gap, move[1] * gap] for j in x[1:]]
    for j in x[1:]:
        idx.append([n - 1 + move[0] * gap, j + move[1] * gap])
    for j in x[1::-1]:
        idx.append([j + move[0] * gap, n - 1 + move[1] * gap])
    for j in x[1::-1]:
        idx.append([move[0] * gap, j + move[1] * gap])

    return idx


def get_rotate(degree):
    """
        return value
        flag => 반전을 하는 경우
        회전 수
    """
    flag = 0

    if degree < 0:
        degree += 360

    if degree == 180:
        return 1, 0

    if degree == 360 or degree == 0:
        return flag, 0

    if degree < 180:
        return flag, degree // 45

    same_degree = {i + 180: i for i in [45, 90, 135]}
    if degree in same_degree.keys():
        return 1, same_degree[degree] // 45


def mirror(arr, i, arr_size):
    if i < 1:
        return arr

    outlier = find_outlier(i, arr_size)

    # 무조건 8개 나옴 [0:4] [4:-1]

    for a, b in zip(outlier[0:4], outlier[4:8]):
        swap = arr[a[1]][a[0]]
        arr[a[1]][a[0]] = arr[b[1]][b[0]]
        arr[b[1]][b[0]] = swap

    arr = mirror(arr, i - 1, arr_size)
    return arr


def rotate(arr, i, d_i, arr_size):
    """ 45도 시계 방향으로 회전 """
    if i < 1:
        return arr

    outlier = find_outlier(i, arr_size)

    for _ in range(d_i):
        temp = arr[outlier[-1][1]][outlier[-1][0]]
        for j in range(len(outlier) - 2, -1, -1):
            x = outlier[j][0]
            y = outlier[j][1]

            # x, y 이전 point
            before_x = outlier[j + 1][0]
            before_y = outlier[j + 1][1]

            arr[before_y][before_x] = arr[y][x]
        arr[outlier[0][1]][outlier[0][0]] = temp
    arr = rotate(arr, i - 1, d_i, arr_size)
    return arr

if __name__ == '__main__':

    T = int(input())
    for _ in range(T):
        n, d = map(int, input().split())
        board = []
        for _ in range(n):
            board.append(list(map(int, input().split())))
        k = (n - 1) // 2
        # flag => 반전 여부(mirror), count 회전 횟수)
        flag, count = get_rotate(degree=d)
        board = rotate(board, k, count, arr_size=k)
        if flag:
            board = mirror(board, k, arr_size=k)

        for i in range(n):
            print(' '.join(map(str, board[i])))
