def fractional_knapsack(v, w, B):
    items = [(i, v[i], w[i]) for i in range(len(v))]
    items.sort(key= lambda x: x[1]/x[2], reverse=True)
    x = [0] * len(v)
    for idx, value, weight in items:
        if weight <= B:
            x[idx] = 1
            B -= weight
        else:
            fraction = B / weight
            x[idx] = fraction
            B = 0
    return x

v = [64, 111, 58, 168, 98, 192, 142, 129, 214, 205, 240, 243, 127, 190, 150, 216, 221, 242, 242, 123, 215, 237, 113, 93, 202, 187, 71]
w = [1, 2, 2, 23, 10, 38, 16, 24, 8, 18, 31, 59, 14, 27, 46, 21, 64, 49, 35, 40, 37, 11, 3, 10, 14, 44, 5]
B = 31

res = fractional_knapsack(v, w, B)
print(fractional_knapsack(v, w, B))
opt_val = sum([res[i] * v[i] for i in range(len(v))])
print(opt_val)