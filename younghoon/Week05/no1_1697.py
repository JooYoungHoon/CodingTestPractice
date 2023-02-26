# 백준 1697 숨바꼭질

def fast_way(N, K):
    '''
    ways:       방문해야하는 중간 경로
    road:       방문한 경로 저장용
    idx:        몇번째 이동인지 확인
    w1, w2, w3: 이동 가능한 경우의 수 세 가지
    fast:       가장 빠른 경로 저장
    '''
    maximum = 100000

    ways = [[N]]
    road = [0 for i in range(maximum+1)]
    idx = 0

    
    w1, w2, w3 = 0, 0, 0

    fast = 0

    # 경로 탐색
    while not fast:
        # t초 후의 이동 가능한 경로를 저장할 임시 배열 (추후 ways에 append)
        ways_temp = list()
        for way in ways[idx]:
            w1, w2, w3 = way+1, way-1, way*2
            # 이동할 경로가 동생이 있는 경우 탐색 종료
            if K in (w1, w2, w3):
                fast = idx+1
                break
            
            # 세 가지 경우의 수 확인
            if 0 <= w1 <= maximum and not road[w1]:
                road[w1] = idx+1
                ways_temp.append(w1)
            if 0 <= w2 <= maximum and not road[w2]:
                road[w2] = idx+1
                ways_temp.append(w2)
            if 0 <= w3 <= maximum and not road[w3]:
                road[w3] = idx+1
                ways_temp.append(w3)

        # 이동 후 시간 증가 및 중간 이동 경로 업데이트
        idx += 1
        ways.append(ways_temp)
    # for i in ways:
    #     print(i)
    print(fast)
    exit(0)

if __name__ == "__main__":
    # 수빈 위치 N, 동생 위치 K
    N, K = map(int, input().split())

    if N == K:
        print(0)
        exit(0)

    elif N > K:
        print(N-K)
        exit(0)

    fast_way(N, K)