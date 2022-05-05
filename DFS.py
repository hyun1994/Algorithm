def DFS(graph, start, visited = []):
    visited.append(start)

    for n in graph[start]:
        if n not in visited:
            DFS(graph, n, visited)
    return visited