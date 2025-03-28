def select_compatible_intervals(A):
    A = sorted(A, key=lambda x: x[1])
    s = [A[0]]
    for i in range(1, len(A)):
        if A[i][0] > s[-1][1]:
            s.append(A[i])
    return s


input =A = [[4, 36], [17, 147], [5, 18], [62, 67], [16, 32], [96, 128], [21, 117], [19, 122], [64, 168], [45, 99], [12, 55], [20, 26], [79, 126], [3, 9], [89, 101], [55, 112], [26, 157], [1, 2], [16, 116], [49, 70], [26, 60], [52, 153], [16, 28], [20, 83], [158, 166], [3, 7], [7, 8], [61, 140], [1, 4], [12, 170], [19, 57], [35, 110], [54, 155], [93, 137], [47, 58], [49, 114], [115, 174], [60, 61], [64, 90], [3, 142], [4, 145], [89, 119], [24, 76], [22, 154], [63, 108], [8, 27], [26, 49], [18, 77], [106, 175], [2, 87], [7, 148], [65, 66], [36, 135], [17, 118], [96, 130], [38, 171], [4, 40], [24, 38], [22, 132], [129, 144]]
for i in range(len(input)):
    for x in range(len(input[i])):
        input[i][x] -= 1

result = select_compatible_intervals(input)
for i in range(len(result)):
    for x in range(len(result[i])):
        result[i][x] += 1

print(result)