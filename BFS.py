from collections import deque
def BFS(graph, start):
    q = deque([start])
    visited = [start]

    while q:
        node = q.popleft()
        for n in graph[node]:
            if n not in graph[node]:
                q.append(n)
                visited.append(n)
    return visited