# 백준 2178 미로탐색

import sys

def shortcut(mirro):
    '''
    x, y : 미로 위치
    d: 해당 위치까지 이동 거리
    dx, dy: → ↓ ↑ ←
    need_visit: 방문해야할 배열 (x, y, d) (pop(0)을 통해 queue 구현)
    visted: 방문한 위치 저장
    distance: 미로의 각 위치까지 이동하는데 필요한 거리 배열
    '''
    
    x, y, d = 0, 0, 1
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]

    need_visit, visted = [(x, y, d)], list()
    distance = [[0 for _ in range(M)] for _ in range(N)]
    
    # bfx를 통해 최단 거리 구하기
    while need_visit:
        x, y, d = need_visit.pop(0)
        # 방문하지 않았으면서 해당 위치로 가능할 때
        if (x, y) not in visted and mirro[x][y] == '1':
            visted.append((x, y))
            distance[x][y] = d
            # 네 방향으로 탐색
            for i in range(4):
                if 0 <= x + dx[i] < N and 0 <= y + dy[i] < M:
                    need_visit.append((x + dx[i], y + dy[i], distance[x][y] + 1))

    return distance[N-1][M-1]

if __name__ == "__main__":
    # 초기 입력
    N, M = map(int, input().split())
    
    # '1' '0' 으로 입력 받기
    mirro = [list(str(input())) for _ in range(N)]

    # 정답
    print(shortcut(mirro))