# 백준 2615번 오목

import sys

def find_omog(x, y):
    '''
    x: 바둑판 row
    y: 바둑판 column
    field: 바둑판
    bw: 바둑알
    cnt: 바둑알 카운트
    '''
    # 바둑알 확인 흑돌 or 백돌
    bw = field[x][y]

    # 방향 dx_, dy_ (→ ↘ ↓ ↗)
    dx_ = [0, 1, 1, -1]
    dy_ = [1, 1, 0, 1]

    # 네 방향으로 각각 탐색
    for d in range(4):

        # 시작 시 값 저장
        cnt, xi, yi = 1, x, y
        dx = dx_[d]
        dy = dy_[d]
        # 바둑알 다섯개 확인
        for _ in range(4):
            xi += dx
            yi += dy
            # 오목판을 벗어나면 루프 종료
            if xi < 0 or yi < 0 or xi >=19 or yi >= 19:
                break

            # 다음 방향에도 같은 바둑알이 있는 경우 바둑알 카운트 증가
            if field[xi][yi] == bw:
                cnt += 1

        # 오목인 경우 육목인지 아닌지 확인
        if cnt == 5:
            # 시작점 바로 이전과 마지막 점 바로 다음을 확인
            if 0 <= xi+dx < 19 and 0 <= yi+dy < 19 and field[xi + dx][yi + dy] == bw:
                continue
            if 0 <= x-dx < 19 and 0 <= y-dy < 19 and field[x - dx][y - dy] == bw:
                continue
            print(f'{bw}\n{x+1} {y+1}')
            exit(0)
        
if __name__ == "__main__":
    # 입력 바둑판
    field = []
    for _ in range(19):
        field.append(list(map(int, sys.stdin.readline().split())))

    # 바둑판 탐색
    for row in range(19):
        for col in range(19):
            # 바둑알이 있을 때
            if field[row][col]:
                find_omog(row, col)
    print(0)
