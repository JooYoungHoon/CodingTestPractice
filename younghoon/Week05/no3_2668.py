# 백준 2668 숫자 고르기

def select_num(table):
    # 원본 숫자 1~n 배열과 뽑은 숫자 배열
    original_nums, selected_nums = table[0], table[1]
    
    # 같은 열에 있는 숫자 조합들
    possible_combi = {x: y for x, y in zip(original_nums, selected_nums)}
    
    # 정답 출력용 변수 교집합 크기 및 원소들
    len_intersection = 0
    elements = []
    
    # 오름차순으로 탐색
    for idx in range(1, N+1):
        # 교집합 비교를 위한 set 변수
        set_ori, set_sel = set(), set()
        
        # dfs 탐색용
        need_visit, visted = [idx], [0 for _ in range(N+1)]
        
        # dfs
        while need_visit:
            n = need_visit.pop()
            if visted[n] == 0:
                visted[n] = 1
                
                # 오리지널 원소
                set_ori.add(n)
                to_sel = possible_combi[n]
                
                # 뽑은 원소
                need_visit.append(to_sel)
                set_sel.add(to_sel)
        
        # 오리지널과 뽑은 원소가 같을 때
        if set_ori == set_sel:
            len_intersection += 1
            elements.append(idx)
    
    # 정답 출력
    print(len_intersection)
    for ele in elements:
        print(ele)
            
if __name__ == "__main__":
    # 초기 입력 N: 정수
    N = int(input())
    # 2xn 표 생성
    table = [[i+1 for i in range(N)] for _ in range(2)]
    for idx in range(N):
        table[1][idx] = int(input())
    
    select_num(table)