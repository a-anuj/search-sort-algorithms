def selection_sort(n):
    for i in range(len(n)-1):
        minpos = i
        for j in range(i + 1, len(n)):
            if n[minpos] > n[j]:
                minpos = j
        n[i], n[minpos] = n[minpos], n[i]
    return n


print(selection_sort([3, 4, 2, 5, 8, 7]))
