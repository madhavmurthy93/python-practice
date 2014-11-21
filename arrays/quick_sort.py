def quicksort(a, left, right):
    if (left < right):
        medianof3pivot(a, left, right)
        pivot = partition(a, left, right - 1)
        quicksort(a, left, pivot - 1)
        quicksort(a, pivot + 1, right)

def partition(a, left, right):
    pivot = a[right]
    i = left
    j = right - 1

    while(i < j):
        while (a[i] < pivot):
            i += 1
        while(a[j] > pivot):
            j -= 1
        if (i < j):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            i += 1
            j -= 1
        else:
            break
    a[right] = a[i]
    a[i] = pivot
    return i

def medianof3pivot(a, left, right):
    mid = (left + right) / 2
    if (a[mid] < a[left]):
        temp = a[left]
        a[left] = a[mid]
        a[mid] = temp
    if (a[right] < a[left]):
        temp = a[left]
        a[left] = a[right]
        a[right] = temp
    if (a[right] < a[mid]):
        temp = a[mid]
        a[mid] = a[right]
        a[right] = temp
    temp = a[mid]
    a[mid] = a[right - 1]
    a[right - 1] = temp

def main():
    a = [3, 5, 2, 1, 9, 8, 6, 7]
    quicksort(a, 0, len(a) - 1)
    print a

if __name__ == '__main__':
    main()
