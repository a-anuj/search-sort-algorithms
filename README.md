# Searching and Sorting Algorithms
## Sorting
- Sorting is the process of arranging items in a particular order, typically in ascending or descending sequence. It is used to organize data, making it easier to search, analyze, and understand. 
  
- Sorting algorithms like bubble sort, insertion sort, quick sort , merge sort are some of the famous methods in sorting

### Bubble sort
- Bubble sort repeatedly compares and swaps adjacent elements if they are in the wrong order

- Time complexity is O(n^2)

- Syntax : 
```py
for i in range(len(n)):
        for j in range(len(n)-i-1):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
```

### Selection sort
- Selection sort repeatedly finds the minimum element from the unsorted portion of the list and swaps it with the first unsorted element, gradually building the sorted portion from left to right.

- Time complexity is O(n^2)
- Syntax:
```py
  for i in range(len(n)-1):
        minpos = i
        for j in range(i + 1, len(n)):
            if n[minpos] > n[j]:
                minpos = j
        n[i], n[minpos] = n[minpos], n[i]
```
