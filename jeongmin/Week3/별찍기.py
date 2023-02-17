"""

    1 => '*'
    0 => ' '

    오른쪽 위 방향으로 향하는 방향은
    위 , 오른쪽 위 대각선, 오른쪽 말고 이외에 있다.
    dx, dy
    move = [0, -1*N]
    move = [1, -1*N]
    move = [1*N, -1*N]
    move = [1*N, -1]
    move = [1*N, 0]

    dy * (-1) 방향 반전 오른쪽 아래로 이동
    dx * (-1) 방향 반전 왼쪽 위로 이동
    dy, dx (-1) 방향 반전 왼쪽 아래로 이동

"""


def change(x):
    if x:
        return '*'
    else:
        return ' '


def star(n, stars, mid_point):
    if n < 2:
        return stars
    # 중심점 찾기
    # 오른쪽 위 방향들을 나타냄

    k = 3 * n + (n - 3)

    gap = k - (k // 2)
    m = gap - 1
    moves = [[0, -1 * m], [1 * m, -1 * m], [1 * m, 0]]
    temps_x = [[x, -1 * m] for x in range(1, gap)]
    temps_y = [[-1 * m, y] for y in range(1, gap)]
    mirror = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
    # arr만들기

    for mdx, mdy in mirror:
        for dx, dy in moves:
            nx = mid_point[0] + dx * mdx
            ny = mid_point[1] + dy * mdy
            stars[ny][nx] = 1
        for dx, dy in temps_x:
            nx = mid_point[0] + dx * mdx
            ny = mid_point[1] + dy * mdy
            stars[ny][nx] = 1
        for dx, dy in temps_y:
            nx = mid_point[0] + dx * mdx
            ny = mid_point[1] + dy * mdy
            stars[ny][nx] = 1

    stars[mid_point[1]][mid_point[0]] = 1

    stars = star(n - 1, stars, mid_point)

    return stars


if __name__ == '__main__':
    N = int(input())

    if N == 1:
        print('*')

    else:
        k = 3 * N + (N - 3)
        mid = [k // 2, k // 2]
        arr = [[0] * k for _ in range(k)]
        arr = star(N, arr, mid)
        ret = []
        for arr_y in arr:
            ret.append(list(map(change, arr_y)))
        for i in range(k):
            print(''.join(ret[i]))
