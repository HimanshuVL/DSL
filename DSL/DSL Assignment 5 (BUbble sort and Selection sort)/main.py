def bubble(a):
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
    print("The sorted array of marks  is ;", a)


def selection(a):
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                temp = a[j]
                a[j] = a[i]
                a[i] = temp
                ++j
                ++i
    print("The sorted array of marks  is :", a)


def top(a):
    print("Top 5 Marks are :")
    print(*a[:-6:-1], sep="\n")


a = []
n = int(input("Enter the number of the elements in the array :"))
for i in range(n):
    ele = float(input("Enter the elements in the array :"))
    a.append(ele)
print("The array of marks is :", a)

while True:
    print("The operation that can be performed on the marks are :")
    print("1.Sort marks by Bubble sort")
    print("2.Sort marks by selection sort")
    print("3.Top 5 marks ")
    print("4.Exit")
    ch = int(input("Enter your choice :"))
    if ch == 1:
        bubble(a)
    if ch == 2:
        selection(a)
    if ch == 3:
        top(a)
    if ch == 4:
        break
