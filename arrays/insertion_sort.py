def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        val = arr[j]
        while(j > 0):
            if (val < arr[j - 1]):
                arr[j] = arr[j - 1]
                j -= 1
            else:
                break
        arr[j] = val

def main():
    arr = [ 5, 4, 7, 2, 3, 1, 10]
    insertion_sort(arr)
    print arr

if __name__ == '__main__':
    main()
