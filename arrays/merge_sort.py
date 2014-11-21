def mergesort(a, target, left, right):
    if (left < right):
        mid = (left + right) / 2
        mergesort(a, target, left, mid)
        mergesort(a, target, mid + 1, right)
        merge(a, target, left, mid, right)

def merge(a, target, left, mid, right):
    i = left
    j = mid + 1
    t = left
    while (i <= mid and j <= right):
        if (a[i] <= a[j]):
            target[t] = a[i]
            i += 1
        else:
            target[t] = a[j]
            j += 1
        t += 1

    if (i > mid):
        for k in range(left, t):
            a[k] = target[k]
    if (j > right):
        k = mid
        l = right
        while (k >= i):
            a[l] = a[k]
            l -= 1
            k -= 1
        for k in range(left, t):
            a[k] = target[k]


def main():
    a = [3, 5, 10, 7, 2, 4, 1, 8]
    t = [0, 0, 0, 0, 0, 0, 0, 0]
    mergesort(a, t, 0, len(a) - 1)
    print a

if __name__ == '__main__':
    main()
