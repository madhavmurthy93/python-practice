def sort(arr):
    for i in range(0, len(arr)):
        min_val = arr[i]
        min_index = i
        for j in range(i + 1, len(arr)):
            if (arr[j] < min_val):
                min_val = arr[j]
                min_index = j
        arr[min_index] = arr[i]
        arr[i] = min_val

def main():
    arr = [ 3, 6, 2, 1, 4, 5, 9]
    sort(arr)
    print arr
    arr = [1]
    sort(arr)
    print arr

if __name__ == '__main__':
    main()
