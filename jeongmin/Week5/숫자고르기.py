"""

    [Baekjoon] https://www.acmicpc.net/problem/2668

    세로 두 줄, 가로로 N개의 칸으로 이루어진 표

    첫째 줄의 각 칸에는 정수 1, 2, …, N이 차례대로

    둘째 줄의 각 칸에는 1이상 N이하인 정수

    첫째 줄에서 뽑는 Set와 둘째 줄에서 뽑는 Set가 같아야함.

    # 1. idx = 0부터 숫자를 뽑는다.
    # 2. 뽑힌 숫자의 개수가 2보다 작을 경우
     2-1. 처음 뽑은 숫자가 첫째 줄과 둘째 줄과 다르면 다음 idx부터 숫자를 뽑는다.
     2-2. 만약 일치하는 경우 count와 s1, s2를 갱신한다.
    # 3. 뽑힌 숫자의 개수가 2보다 큰 경우
    3-1. idx=0인 숫자와 j = [idx+1:N+1]인 숫자의 세트를 확인한다.
    3-2. 같으면 idx += 1올린다.
    3-3. 다르면 3-1의 j를 순회
    3번 경우 반복


"""

from collections import defaultdict
from collections import deque


def dfs(graph, s1, s2, q, visited):
    temp_s1 = []
    temp_s2 = []
    for start in graph.keys():
        if start == graph[start]:
            temp_s1.append(start)
            temp_s2.append(graph[start])
            continue

        q.append([start, graph[start]])

        while q:
            t1, t2 = q.popleft()
            if visited[t1]:
                continue
            s1.append(t1)
            s2.append(t2)
            visited[t1] = 1
            if len(s1) < 2 and len(s2) < 2:
                continue
            if set(s1) == set(s2):
                q.append([t1, graph[t2]])
            else:
                s1.pop(-1)
                s2.pop(-1)
                continue
    if set(s1) != set(s2):
        s1 = []
        s2 = []

    while temp_s2 and temp_s1:
        s1.append(temp_s1.pop(-1))
        s2.append(temp_s2.pop(-1))
    return s1, s2


if __name__ == '__main__':
    N = int(input())
    graph = defaultdict(list)
    second = []
    for i in range(1, N + 1):
        num = int(input())
        graph[i] = num

    s1 = []
    s2 = []
    q = deque()
    visited = [0] * (N + 1)
    s1, s2 = dfs(graph, s1, s2, q, visited)

    print(len(s1))
    print('\n'.join(map(str, set(s1).union(set(s2)))))
