a = []
b = []


def matrix_a(r, c):
    for i in range(r):
        x = list(map(int, input().split()))
        a.append(x)


def matrix_b(r, c):
    for i in range(r):
        y = list(map(int, input().split()))
        b.append(y)


def add():
    r, c = map(int, input().split())
    matrix_a(r, c)
    r, c = map(int, input().split())
    matrix_b(r, c)

    for i in range(r):
        for j in range(c):
            print(a[i][j] + b[i][j], end=" ")
        print()


def scalar_multiply():
    r, c = map(int, input().split())
    matrix_a(r, c)
    k = int(input())

    for i in range(r):
        for j in range(c):
            print(a[i][j] * k, end=" ")
        print()


def multiply():
    print("under maintance!")


def transpose():
    r, c = map(int, input().split())
    matrix_a(r, c)
    n = len(a)
    temp = 0

    for i in range(0, n):
        for j in range(i + 1, n):
            temp = a[i][j]
            a[i][j] = a[j][i]
            a[j][i] = temp

    for i in range(c):
        for j in range(r):
            print(a[i][j], end=" ")
        print()



    
    






