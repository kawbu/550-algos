def floyd_warshall(G):
    n = len(G)
    d = [[[float('inf') for _ in range(n)] for _ in range(n)] for _ in range(n)]

    for u in range(n):
        d[u][u][0] = 0
        for target, weight in G[u]:
            d[u][target][0] = weight

    for r in range(1, n):
        for u in range(n):
            for v in range(n):
                d[u][v][r] = min(d[u][v][r - 1], d[u][r][r - 1] + d[r][v][r - 1])

     # Return the final distance matrix
    return [[d[u][v][n - 1] for v in range(n)] for u in range(n)]


G = [[[2, 4]], [[3, -2], [4, 3]], [[1, 1], [4, 3]], []]

G_updated = [
    [[pair[0] - 1, pair[1]] for pair in sublist]
    for sublist in G
]

result = floyd_warshall(G_updated)
print(result)
