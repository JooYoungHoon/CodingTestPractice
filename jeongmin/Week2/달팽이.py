"""

    dx dy
    [0, 1] 하
    [1, 0] 우
    [0, -1] 상
    [-1, 0] 좌
    N = 5 : N-1 (하 우 상)
            N-2 (좌)
    N = 3 : N-1 (하 우 상)
            N-2 (좌)

    N = 1 : N(1) (하)

    최대 큰 수 N^2

    dir = {5:{하:4, 우:4, 상:4, 좌:3}, 3:{하:2,우:2,상:2,좌:1}, 1:{하:1}}
    2k-1 => N
    1 => 1
    3 => 5
    dp[1] = [하]
    dp[2] = [하,좌,상상,우우,..하하]
    dp[3] = [하,좌 .. 하하,좌좌좌,상상상하,...하하하하]

"""

# memory 초과
# def make_dir(k, m):
#     """ 방향 순서 리스트 만들기"""
#     global dp, dx, dy
#     if k == 0:
#         return [[-1, -1]]
#     if dp[k]:
#         return dp[k]
#
#     cnt = (2 * k - 2, 2 * k - 3)
#     dp[k] = make_dir(k-1, m) + [[dx[0], dy[0]]] * cnt[1]
#     for x, y in zip(dx[1:], dy[1:]):
#         dp[k] += [[x, y]] * cnt[0]
#     if m != k:
#         dp[k] += [[0, 1]]
#
#     # dp[0] = [[-1, -1]]
#     # dp[1] = [[0, 1]]
#     # for i in range(2, k + 1):
#     #     dp[i] = dp[i - 1] + [[dx[0], dy[0]]] * cnt[1]
#
#     return dp[k]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def snail(N, loc):
    arr = [[0] * N for _ in range(N)]
    tmp = [0, 0]
    dir_idx = 0
    i = N ** 2
    while i > 0:

        if i == loc:
            find_loc = [tmp[0], tmp[1]]
        arr[tmp[0]][tmp[1]] = i
        x = tmp[1] + dx[dir_idx]
        y = tmp[0] + dy[dir_idx]

        if i == 1:
            break

        if x < 0 or x >= N or y < 0 or y >= N:
            dir_idx += 1
            if dir_idx > 3:
                dir_idx = 0
            continue
        else:
            if arr[y][x] != 0:
                dir_idx += 1
                if dir_idx > 3:
                    dir_idx = 0
                continue

        i -= 1
        tmp = [y, x]

    return find_loc, arr


if __name__ == '__main__':
    N = int(input())
    loc = int(input())
    find_loc = []

    find_loc, arr = snail(N, loc)
    find_loc = map(lambda a: a + 1, find_loc)
    for i in range(len(arr)):
        print(' '.join(map(str, arr[i])), sep='\n')
    print(' '.join(map(str, find_loc)))
