def lis(A):
    d = [1] * len(A)
    for i in range(1, len(A)):
        for j in range(0, i):
            if A[j] < A[i] and d[i] < d[j] + 1:
                d[i] = d[j] + 1
    return max(d)

print(lis([1, 4, 5, 2, 6, 9, 8, 3, 2]))