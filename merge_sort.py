def merge_sort(A):
    if len(A) == 1:
        return A
    k = len(A) // 2
    A_left = merge_sort(A[0:(k + 1)])
    A_right = merge_sort(A[(k + 2):len(A)])
    i, j, B = 1, 1, []
    while i <= k  and j <= len(A) - k:
        if A_left[i] <= A_right[j]:
            B.append(A_left[i])
            i += 1
        else:
            B.append(A_right[j])
            j += 1
    if i > k:
        for n in A_right[j:(len(A) - k + 1)]:
            B.append(n)
    else:
        for n in A_left[i:(k + 1)]:
            B.append(n)
    A = B
    return A

print(merge_sort([18, 73, 98, 9, 33, 16, 64, 58]))