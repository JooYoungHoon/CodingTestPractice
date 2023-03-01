"""

    https://www.acmicpc.net/problem/1202

    보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를 가지고 있다.

    1. 가방 K개
    2. 각 가방에 담을 수 있는 최대 무게 Ci
    3. 최대 한 개의 보석만 담을 수 있음

    훔칠 수 있는 보석의 최대 가격을 구해라

    N, K => 2, 1
    Mi Vi => [5, 10],[100, 100]

    11


"""
import sys
from collections import deque


def solution(n, k, g, b):
    g = sorted(g, key=lambda x: [x[0], -x[1]])

    total = 0

    stolen = deque()

    i = 0
    flag = 0
    while i <= k and g:
        temp = g.pop(0)
        if not stolen:
            if b[i] >= temp[0]:
                stolen.append(temp)
                i += 1
        else:
            if b[i] >= temp[0]:
                if stolen[-1][1] < temp[1]:
                    stolen.pop()
                    stolen.append(temp)
                    i = i
            else:
                i += 1

    return total


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())

    gems = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    bag = [int(input()) for _ in range(K)]

    print(solution(N, K, gems, bag))
