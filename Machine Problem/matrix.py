import numpy

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
    r1, c1 = map(int, input().split())
    matrix_a(r1, c1)
    r2, c2 = map(int, input().split())
    matrix_b(r2, c2)

    print(numpy.dot(a, b))


def transpose():
    r, c = map(int, input().split())
    matrix_a(r, c)

    x = [[0 for x in range(r)] for y in range(c)]
    for i in range(c):
        for j in range(r):
            x[i][j] = a[j][i]

    for i in range(c):
        for j in range(r):
            print(x[i][j], end=" ")
        print()
