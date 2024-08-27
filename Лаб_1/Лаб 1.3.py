n = int(input("Введіть число N (2-8): "))

if not 1 < n < 9:
    print("Число повинно бути в межах від 2 до 8.")
else:
    for i in range(n, 0, -1):
        for j in range(i, n + 1):
            print(j, end=' ')
        print()
