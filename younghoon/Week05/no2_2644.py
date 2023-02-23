# 백준 2644 촌수계산

def dfs_check_chon(p1, p2):
    need_visit, visted = list(), [0 for i in range(n+1)]

    need_visit.append((p1, 1))

    # 형제 자매 관계인지 확인
    p1_parent = find_parent(p1)
    p1_parent_siblings = find_sibling(p1_parent)
    if p2 in p1_parent_siblings:
        return 0
    
    # dfs로 촌수 계산 부모와 자식 사이 관계만 확인
    while need_visit:
        p, d = need_visit.pop()
        if not visted[p]:
            visted[p] = d
            # 자식들 확인
            if famliy[p]:
                for child in famliy[p]:
                    if visted[child] == 0:
                        need_visit.append((child, d+1))

            # 부모 확인
            parent = find_parent(p)
            if parent and visted[parent] == 0:
                need_visit.append((parent, d+1))

    answer = visted[p2]
    return answer - 1 if answer >0 else -1


def find_parent(p):
    for idx, siblings in enumerate(list(famliy.values())):
        if p in siblings:
            return idx + 1
    return 0

def find_sibling(p_parent):
    if p_parent:
        return famliy[p_parent]
    else:
        return []

if __name__ == "__main__":
    # 전체 사람 n
    n = int(input())

    # 촌수를 계산할 사람 p1, p2
    p1, p2 = map(int, input().split())

    # 부모 자식들간 관계의 개수 m
    m = int(input())

    # m개의 부모-자식 관계도
    famliy = {key+1: list() for key in range(n)}
    for _ in range(m):
        x, y = map(int, input().split())
        famliy[x].append(y)
    
    # 정답 출력
    answer = dfs_check_chon(p1, p2)
    print(answer)