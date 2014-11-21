def combine(a, b, a_len, b_len):
    i = a_len - 1
    j = b_len - 1
    full_length = len(a)
    while (i >= 0 and j >= 0):
        if (a[i] > b[j]):
            a[full_length - 1] = a[i]
            i -= 1
        else:
            a[full_length - 1] = b[j]
            j -= 1
        full_length -= 1
    if (i < 0):
        for k in range(0, full_length):
            a[k] = b[k]

def main():
    a = [2, 7, 9, 10, 12, 0, 0, 0, 0, 0]
    b = [1, 3, 4, 8, 11]
    combine(a, b, 5, 5)
    print a

if __name__ == '__main__':
    main()
