# 백준 3187 양치기 꿍

'''
빈 공간    .
울타리     #
늑대       v
양         k
dx,dy     → ↓ ← ↑

풀이방법
1) (0, 0)에서 dfs를 통해 울타리 내부를 탐색 시작
2) 이때 전체를 한번에 탐색하지 않고 울타리를 만나는 경우 탐색 중지
3) 1~2 사이클 동안 찾은 늑대와 염소 개수 확인
4) 탐색하지 않은 지점부터 1~3 과정 반복
'''
import sys

def findalive(space):
    
    need_visit = list()
    visted = [[0 for _ in range(C)] for _ in range(R)]
    x, y = 0, 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    v, k = 0, 0
    cnt = 0
    wolf, sheep = 0, 0
    
    for x in range(R):
        for y in range(C):
            need_visit.append((x, y))

            # dfs
            while need_visit:
                x, y = need_visit.pop()
                # 방문하지 않았을 때
                if visted[x][y] == 0:
                    visted[x][y] = 1
                    # 울타리를 만나면 더 이상 탐색하지 않도록 need_visit에 append X
                    if space[x][y] == "#":
                        continue
                    else:
                        if space[x][y] == "v":
                            v += 1
                        if space[x][y] == "k":
                            k += 1
                        for i in range(4):
                            if 0 <= x+dx[i] < R and 0 <= y+dy[i] < C:
                                need_visit.append((x+dx[i], y+dy[i]))                                       

            # 한 영역 내에서 양과 늑대의 수 확인 및 살아남은 늑대 양 반환
            if k + v > 0:         
                if k > v:
                    sheep += k
                else:
                    wolf += v
                
                # 늑대와 양의 수 초기화
                v, k = 0, 0
            
    return sheep, wolf
        
          
            
        
if __name__ == "__main__":
    # 초기 입력 C: column R: row space: 울타리
    R, C = map(int, input().split())
    space = list()
    for _ in range(R):
        space.append(list(input()))

    # 정답
    sheep, wolf = findalive(space)
    print(sheep, wolf)
