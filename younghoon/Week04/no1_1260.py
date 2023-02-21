# 백준 1260 DFS와 BFS

import sys
from pprint import pprint

class Graph:
    def __init__(self, graph=dict()):
        self.graph = graph

    def dfs(self, start_node):
        need_visit, visted = list(), list()
        for key in range(1, N+1):
            self.graph[key].sort(reverse=True)
        
        need_visit.append(start_node)
        
        while need_visit:
            node = need_visit.pop()
            if node not in visted:
                visted.append(node)
                need_visit.extend(self.graph[node])
        return visted
    
    def bfs(self, start_node):
        need_visit, visted = list(), list()
        
        for key in range(1, N+1):
            self.graph[key].sort()
        
        need_visit.append(start_node)
        
        while need_visit:
            node = need_visit.pop(0)
            if node not in visted:
                visted.append(node)
                need_visit.extend(self.graph[node])
                
        return visted
            
'''

# dfs 구현
def dfs(graph, start_node):
    need_visit, visted = list(), list()
    
    need_visit.append(start_node)
    
    while need_visit:
        node = need_visit.pop()
        if node not in visted:
            visted.append(node)
            need_visit.extend(graph[node])
            
    return visted

# bfs 구현
def bfs(graph, start_node):
    need_visit, visted = list(), list()
    
    need_visit.append(start_node)
    
    while need_visit:
        node = need_visit.pop(0)
        if not need_visit:
            visted.append(node)
            need_visit.extend(graph[node])
    
    return visted
'''
     
if __name__ == "__main__":
    # 초기입력 N 정점의 개수 // V 간선의 개수 // start 탐색 시작 정점 번호
    N, V, start = map(int, input().split())

    # 그래프 생성
    graph = {key+1: list() for key in range(N)}
    n1, n2 = 0, 0 # 정점번호
    for _ in range(V):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    A = Graph(graph=graph)
    
    answer_dfs = A.dfs(start)
    answer_bfs = A.bfs(start)
    for ele in answer_dfs:
        print(ele, end=' ')
    print()
    for ele in answer_bfs:
        print(ele, end =' ')
    # print(answer_dfs)
    # print(answer_bfs)