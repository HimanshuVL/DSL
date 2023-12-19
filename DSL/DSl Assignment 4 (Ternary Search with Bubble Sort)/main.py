array = []
n = int(input("Enter number of elements in the array :"))
for i in range(n):
    ele = int(input("Enter the number of the elements :"))
    array.append(ele)
print("Array is :", array)

for i in range(n):
    for j in range(n-i-1):
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
print("Sorted array is :", array)
Sorted_Array = array

key = int(input("Enter the value to be searched :"))


def ternary(l, r, array, key):
    if r >= l:
        m1 = l+(r-l)//3
        m2 = r-(r-l)//3
        if Sorted_Array[m1] == key:
            return m1
        elif Sorted_Array[m2] == key:
            return m2
        elif key < Sorted_Array[m1]:
            return ternary(l, m1-1, Sorted_Array, key)
        elif key > Sorted_Array[m2]:
            return ternary(m2+1, r, Sorted_Array, key)
        else:
            return ternary(m1-1, m2+1, Sorted_Array, key)


p = ternary(0, 3, Sorted_Array, key)
print("Index of ", key, "is", p)
