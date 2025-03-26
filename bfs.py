def ALGbfs(g, s):
    for i in range(len(g)):
        for x in range(len(g[i])):
            g[i][x] -= 1
    sol = [1000 for i in range(len(g))]
    sol[s] = 0
    queue = [s]
    while len(queue) > 0:
        curr = queue.pop()
        for val in g[curr]:
            if (sol[val]) == 1000:
                sol[val] = sol[curr] + 1
                queue.append(val)
    return sol

print(ALGbfs([[3], [1], [4], [1, 2]], 0))