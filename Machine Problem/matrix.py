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
    r1, c1 = map(int, input().split())
    matrix_a(r1, c1)
    r2, c2 = map(int, input().split())
    matrix_b(r2, c2)

    if r1 != r2 and c1 != c2:
        print("""Invalid input. Addition of matrices follows conformability; 
                matrices should be of the same dimensions.""")
        quit()

    for i in range(r1):
        for j in range(c1):
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

    if r2 != c1:
        print( """Invalid input. Multiplication of matrices follows conformability.
                Matrices, say A and B, should have same column and row, respectively.""")
        quit()
    
    for i in range(r1):                    
        for j in range(c2):
            p = 0
            for k in range(r2):
                p += a[i][k] * b[k][j]
            print(p, end=(" "))
        print()


def transpose():
    r, c = map(int, input().split())
    matrix_a(r, c) 

    for i in range(c):
        for j in range(r):
            print(a[j][i], end=" ")
        print()


