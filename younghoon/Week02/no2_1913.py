# 백준 1913 달팽이

import sys
import math

def snail(N, tofind):
    # NxN 행렬 초기화
    matrix = []
    for _ in range(N):
        matrix.append([0]*N)
    
    # 찾아야할 좌표
    i_ = 0
    j_ = 0
    if tofind == 1:
        i_ = N//2
        j_ = N//2
    # 시작점
    num = 1
    x, y = N//2, N//2
    matrix[x][y] = num
    
    # 방향
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # 길이
    length = []
    for i in range(1, 2*N - 1):
        length.append(math.ceil(i/2))
    length.append(N-1)

    # 달팽이 배열 생성
    for idx, go in enumerate(length):
        dx, dy = direction[idx%4]
        for _ in range(go):
            num += 1
            x += dx
            y += dy
            # 찾아야 할 좌표 값 저장
            if num == tofind:
                i_ = x
                j_ = y
            matrix[x][y] = num
    return matrix, i_ + 1, j_ + 1

if __name__ == "__main__":
    # 입력 N: 홀수 자연수 // tofind: 찾으려는 수
    N = int(input())
    tofind = int(input())
    
    matrix, x, y = snail(N, tofind)

    # 정답 출력
    for row in matrix:
        for elm in row:
            print(elm, end=' ')
        print()
    print(f'{x} {y}')