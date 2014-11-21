
def insert(arr, val):
    recursive(arr, 0, len(arr) - 1, val)

def recursive(arr, left, right, val):
    if (left >= right):
        if (val < arr[left]):
            arr.insert(left, val)
        else:
            arr.insert(left + 1, val)
    else:
        mid = (left + right) / 2
        if (val < arr[mid]):
            recursive(arr, left, mid, val)
        else:
            recursive(arr, mid + 1, right, val)

def main():
    a = [3, 4, 5, 6, 7, 9]
    insert(a, 2)
    print a
    insert(a, 8)
    print a
    insert(a, 10)
    print a

if __name__ == '__main__':
    main()
