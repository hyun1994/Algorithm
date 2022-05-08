import heapq
def dijkstra(graph, start):
    distance = {}
    for node in graph:
        distance[node] = float('inf')
    distance[start] = 0
    q = []
    heapq.heappush(q, [distance[start], start])

    while q:
        prev_distance, prev_goal = heapq.heappop(q)
        if distance[prev_goal] < prev_distance:
            continue
        for now_goal, now_distance in graph[prev_goal].items():
            distance = prev_distance + now_distance

            if distance < distance[now_goal]:
                distance[now_goal] = distance
                heapq.heappush(q, [distance, now_goal])
    return distance