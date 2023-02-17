"""

    [Baekjoon] https://www.acmicpc.net/problem/17276

    크기가 n * n
    n은 홀수
    2차원 정수 배열
    45도의 배수만큼 시계방향 혹은 반시계방향으로 돌린다.

    X의 주 대각선 (1,1), (2,2), ... (n,n)을 ((n+1)/2번째 열로 옮긴다)
    X의 가운데 열을 X의 부 대각선으로 옮긴다. ((n,1), (n-1, 2), ... (1, n))
    X 부 대각선은 X의 가운데 행으로 옮긴다.

    모든 원소의 기존 순서는 유지되어야함

    X의 다른 원소들의 위치는 변하지 않는다.

    45도 반시계 방향도 이와 비슷하게 정의된다.

    main-digonal(주 대각선) => md
    가운데 열 => mid-rol => mr
    sub-digonal => sd
    mid-col => mc

    mr와 mc를 기준선으로 정하며 중간점을 나타나면 -> (N//2, N//2)이다.

    왼쪽 위는 1
    왼쪽 아래는 2
    오른쪽 아래는 3
    오른쪽 위는 4

    (y, x)
    중간점과 좌표의 거리를 측정했을 때 거리가 => dis(distance)
    여기서 dis는 간단하게 mr과 mc와 수직으로 내린 거리라고 정의함.
    + md 위에 있는 원소 중 중간점 (y, x)좌표보다 작은 경우 dis만큼 움직인다.
    방향에 따라 아래, 오른쪽으로 이동한다.
    + mr 위에 있는 원소 중 중간점 (y, x) 좌표보다 작은 경우 dis만큼 움직인다.
    방향에 따라 왼쪽, 오른쪽으로 이동한다.

    점의 위치를 알려주는 함수 2개 필요
    1. md,mr,mc,sd 에 있는지 1, 2, 3, 4
    2. 중간점 좌표보다 작은 쪽에 있는 지 큰 쪽에 있는지 확인. 0, 1
    3. 각도의 방향 (-1, 1)

"""


def pos(y, x, N):
    """
        y, x 좌표값
        return line_pos(int), is_big(bool)

        md => 1
        mr => 2
        mc => 3
        md => 4

        is_big => 0(small), 1(big)
    """
    mid = [N // 2, N // 2]
    area = -1
    if mid == [y, x]:
        return -1, -1

    md = [[y, x] for y, x in zip(range(N), range(N))]
    mr = [[y, mid[1]] for y in range(N)]
    mc = [[y, x] for y, x in zip(range(N), range(N - 1, -1, -1))]
    sd = [[mid[0], x] for x in range(N)]

    if [y, x] in md:
        line_pos = 1
    elif [y, x] in mr:
        line_pos = 2
    elif [y, x] in mc:
        line_pos = 3
    elif [y, x] in sd:
        line_pos = 4
    else:
        line_pos = -1

    if line_pos == 1 or line_pos == 4:
        if y < mid[0] and x < mid[1]:
            area = 1
        elif y < mid[0] and x > mid[1]:
            area = 2
        elif y > mid[0] and x > mid[1]:
            area = 3
        elif y > mid[0] and x < mid[1]:
            area = 4
    elif line_pos == 2:
        if y < mid[0]:
            area = 5
        else:
            area = 6
    elif line_pos == 3:
        if x < mid[0]:
            area = 7
        else:
            area = 8

    return line_pos, area


def solve(n, arr, d):
    if n == 1:
        return arr
    ret_arr = [[0] * n for _ in range(n)]
    k = abs(d) // 45
    if d > 0:
        forward = 1
    else:
        forward = 0

    for _ in range(k):
        for y in range(n):
            for x in range(n):
                line_pos, area = pos(y, x, n)
                dy = abs(n // 2 - y)
                dx = abs(n // 2 - x)
                if line_pos == -1:
                    ret_arr[y][x] = arr[y][x]
                    continue
                # move = [y, x]
                if area == 1 and line_pos == 1:
                    if forward:
                        move = [0, 1]
                    else:
                        move = [1, 0]
                    dy, dx = map(lambda a: a * dy, move)
                elif area == 2 and line_pos == 4:
                    if forward:
                        move = [1, 0]
                    else:
                        move = [0, 1]
                    dy, dx = map(lambda a: a * dx, move)
                elif area == 3 and line_pos == 1:
                    if forward:
                        move = [0, -1]
                    else:
                        move = [-1, 0]
                    dy, dx = map(lambda a: a * dy, move)
                elif area == 4 and line_pos == 4:
                    if forward:
                        move = [-1, 0]
                    else:
                        move = [0, 1]
                    dy, dx = map(lambda a: a * dx, move)
                elif area == 5 and line_pos == 2:
                    if forward:
                        move = [0, 1]
                    else:
                        move = [0, -1]
                    dy, dx = map(lambda a: a * dy, move)
                elif area == 6 and line_pos == 2:
                    if forward:
                        move = [0, -1]
                    else:
                        move = [0, 1]
                    dy, dx = map(lambda a: a * dy, move)
                elif area == 7 and line_pos == 3:
                    if forward:
                        move = [-1, 0]
                    else:
                        move = [1, 0]
                    dy, dx = map(lambda a: a * dx, move)
                elif area == 8 and line_pos == 3:
                    if forward:
                        move = [1, 0]
                    else:
                        move = [-1, 0]
                    dy, dx = map(lambda a: a * dx, move)
                else:
                    ret_arr[y][x] = arr[y][x]

                ny = y + dy
                nx = x + dx

                ret_arr[ny][nx] = arr[y][x]

        arr = ret_arr

    return ret_arr


if __name__ == '__main__':

    T = int(input())
    for _ in range(T):
        arr = []
        n, d = map(int, input().split())
        for _ in range(n):
            arr.append(list(map(int, input().split())))

        print(solve(n, arr, d))

        # print()
