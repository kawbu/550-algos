def dag_dp(G, s):
    d = [100000] * len(G)
    d[s] = 0
    #topo sort