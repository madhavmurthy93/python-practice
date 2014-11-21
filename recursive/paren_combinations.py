def combinations(n):
    if (n == 1):
        combos = set()
        combos.add("()")
        return combos
    else:
        sets = combinations(n - 1)
        combos = set()
        for combo in sets:
            combos.add("()" + combo)
            combos.add("(" + combo + ")")
            combos.add(combo + "()")
        return combos
def main():
    combos = combinations(2)
    print combos
    combos = combinations(3)
    print combos

if __name__ == '__main__':
    main()
