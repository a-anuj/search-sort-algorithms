def bubble_sort(n):
    for i in range(len(n)):
        for j in range(i):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
            print(f"Step {i} : {n}")
    return n


print(bubble_sort([3, 5, 1, 2, 9]))