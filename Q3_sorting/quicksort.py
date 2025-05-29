import random

def quicksort(A, low, high):
    if low < high:
        pivot = A[(low+high)//2]
        i, j = low, high
        while i <= j:
            while A[i].lower() < pivot.lower(): i+=1
            while A[j].lower() > pivot.lower(): j-=1
            if i <= j:
                A[i],A[j]=A[j],A[i]; i+=1; j-=1
        quicksort(A, low, j); quicksort(A, i, high)

if __name__=='__main__':
    words=["apple","Banana","cherry","Date"]
    random.shuffle(words); print('Before:',words)
    quicksort(words,0,len(words)-1)
    print('After:',words)