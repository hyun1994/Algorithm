def floyd_warshall(graph):
    distance = list(map(lambda i: list(map(lambda j: j,i)), graph))
    for k in range(V):
        for i in range(V):
            for j in range(V):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
    return distance