def bubble_sort(n):
    for i in range(len(n)):
        for j in range(len(n)-i-1):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]

    return n


print(bubble_sort([3, 5, 1, 2, 9]))