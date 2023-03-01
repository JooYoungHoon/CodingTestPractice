"""

    [Baekjoon] https://www.acmicpc.net/problem/2644

    가족 혹은 친척들 사이의 관계를 촌수

    부모와 자식 사이를 1촌으로 정의

     나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌

     아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌

     전체 사람의 수 n
     촌수를 계산해야 하는 서로 다른 두 사람의 번호
     부모 자식들 간의 관계의 개수 m
     넷째줄 부터는 부모 자식간의 관계를 나타내는 두 번호 xy가 나온다.

     1: [2,3]
     2: [7,8,9]
     4: [5,6]

     2:[1]
     3:[1]
     7:[2]
     8:[2]
     9:[2]
     5:[4]
     6:[4]

"""
from collections import defaultdict
from collections import deque


def dfs(i, j, child, parent, visited):
    """

        i, j는 촌수를 계산해야 하는 서로 다른 두 사람의 번호
        c: child
        p: parent
        v: visited
        relation : 촌수
    """

    q = deque()
    relations = 0
    q.append([i, relations])
    while q:
        temp, relations = q.popleft()
        if temp == j:
            return relations
        if visited[temp] >= 1:
            continue
        visited[temp] = relations
        if child[temp]:
            if i in child[temp]:
                if j in child[temp]:
                    return relations + 1
                else:
                    for c in child[temp]:
                        if visited[c] == -1:
                            q.append([c, relations + 1])
            else:
                for c in child[temp]:
                    if visited[c] == -1:
                        q.append([c, relations + 1])
        if parent[temp]:
            if j in parent[temp]:
                return relations + 1
            else:
                if visited[parent[temp][0]] >= 1:
                    continue
                q.append([parent[temp][0], relations + 1])

    return visited[j]


if __name__ == '__main__':

    n = int(input())
    a, b = map(int, input().split())
    m = int(input())
    child = defaultdict(list)
    # 각 사람의 부모는 최대 한명
    parent = defaultdict(list)

    for _ in range(m):
        x, y = map(int, input().split())
        child[x].append(y)
        parent[y].append(x)

    visited = [-1] * (n + 1)
    relation = dfs(a, b, child, parent, visited)
    print(relation)
