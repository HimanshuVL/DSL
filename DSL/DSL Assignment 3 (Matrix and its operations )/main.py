def matrix():
    r = int(input("Enter the number of the rows :"))
    c = int(input("Enter the number of the columns :"))
    print("Enter the elements row wise")
    mat = []
    for i in range(0, r):
        temp = []
        for j in range(0, c):
            ele = int(input("Enter the elements :"))
            temp.append(ele)
        mat.append(temp)
    return mat


result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]


def addition():
    if len(X) == len(Y) and len(X[0]) == len(Y[0]):
        for i in range(len(X)):
            for j in range(len(Y)):
                result[i][j] = X[i][j]+Y[i][j]
        print("Addition is :")
        for r in result:
            print(r)
        print("\n")


def subtraction():
    if len(X) == len(Y) and len(X[0]) == len(Y[0]):
        for i in range(len(X)):
            for j in range(len(Y)):
                result[i][j] = X[i][j]-Y[i][j]
        print("Subtraction is :")
        for r in result:
            print(r)
        print("\n")


def mult():
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k]*Y[k][j]
    print("The multiplication is:")
    for r in result:
        print(r)
    print("\n")


def transpose():
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[j][i] = X[i][j]
    print("The Transpose of the matrix is :")
    for r in result:
        print(r)
    print("\n")


while True:
    print("Operations that can be performed on the matrix :")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Transpose")
    print("5.Exit")
    ch = int(input("Enter the number of the operation :"))
    if ch == 1:
        X = matrix()
        Y = matrix()
        addition()
    elif ch == 2:
        X = matrix()
        Y = matrix()
        subtraction()
    elif ch == 3:
        X = matrix()
        Y = matrix()
        mult()
    elif ch == 4:
        X = matrix()
        transpose()
    elif ch == 5:
        break
    else:
        print("Invalid Data")
        break
