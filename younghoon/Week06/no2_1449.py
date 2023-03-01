# 백준 1449 수리공 항승

if __name__ == "__main__":
    # 초기 입력
    N, L = map(int, input().split())
    repair = list(map(int, input().split()))

    # 테이프 길이가 1이면 물이 새는 위치만큼 테이프 필요
    if L == 1:
        print(N)

    else:
        need = 1
        # 물이 새는 곳 정렬
        repair.sort()
        
        prev_point = repair.pop(0)
        for point in repair:
            # 테이프 하나로 두 지점 수리 가능
            if point - prev_point + 1 <= L:
                pass
            # 두 지점을 테이프 하나로 수리하지 못할 때
            else:
                prev_point = point
                need += 1

        print(need)