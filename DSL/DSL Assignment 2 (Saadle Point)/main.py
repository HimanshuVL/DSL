def saddle_point():
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
    print("The matrix is :")
    for i in range(0, r):
        for j in range(0, c):
            print(mat[i][j], end=" ")
        print()
    for i in range(c):
        row_min = mat[i][0]
        m = 0
        for j in range(1, c):
            if row_min > mat[i][j]:
                row_min = mat[i][j]
                m = j
    k = 0
    while k < c:
        if row_min < mat[k][m]:
            break
        k += 1
    if k == c:
        print("Saddle point exist :", row_min)
    else:
        print("Saddle point does not exist")


saddle_point()
