def bellman_ford(graph, start):
    distance, prev_distance = {}, {}
    for node in graph:
        distance[node] = float('inf')
        prev_distance[node] = None
    distance[start] = 0

    for i in range(len(graph)-1):
        for node in graph:
            for neighbor in graph[node]:
                if distance[neighbor] > distance[node] + graph[node][neighbor]:
                    distance[neighbor] = distance[node] + graph[node][neighbor]
                    prev_distance[neighbor] = node

    for node in graph:
        for neighbor in graph[node]:
            if distance[neighbor] > distance[node] + graph[node][neighbor]:
                return -1
    return distance, prev_distance