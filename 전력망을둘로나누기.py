from collections import deque

n = 4
wires = [[1,2],[2,3],[3,4]]

def dfs(arr,vertex, visited=[]):
    visited.append(vertex)
    for item in arr[vertex]:
        if not item in visited:
            visited = dfs(arr, item, visited)
    return visited

def solution(n, wires):
    arr = [[] for _ in range(n+1)]
    q = deque()
    while wires:
        x,y=wires.pop()
        arr[x].append(y)
    dfs(arr,0,visited)

