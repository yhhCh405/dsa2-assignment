# In-Place Quicksort Pseudocode

```
FUNCTION quicksort(A, low, high):
    IF low < high:
        pivot_index = (low + high) // 2
        pivot = A[pivot_index]
        i = low; j = high
        WHILE i <= j:
            WHILE A[i] < pivot: i += 1
            WHILE A[j] > pivot: j -= 1
            IF i <= j:
                SWAP A[i], A[j]
                i += 1; j -= 1
        quicksort(A, low, j)
        quicksort(A, i, high)
```
Citations:

Classic algorithm: C. A. R. Hoare, original quicksort (Hoare, 1962).
