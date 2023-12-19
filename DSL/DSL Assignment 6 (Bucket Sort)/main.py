def bucket_sort(input_list):
	max_value = max(input_list)
	size = max_value / len(input_list)

	buckets_list = []
	for x in range(len(input_list)):
		buckets_list.append([])

	for i in range(len(input_list)):
		j = int(input_list[i] / size)
		if j != len(input_list):
			buckets_list[j].append(input_list[i])
		else:
			buckets_list[len(input_list) - 1].append(input_list[i])

	for z in range(len(input_list)):
		bubble(buckets_list[z])

	final_output = []
	for x in range(len(input_list)):
		final_output = final_output + buckets_list[x]
	return final_output


def bubble(a):
	for k in range(n):
		for j in range(n - k - 1):
			if a[j] > a[j + 1]:
				temp = a[j]
				a[j] = a[j + 1]
				a[j + 1] = temp


A = []
n = int(input("Enter the number of the elements in the array :"))
for q in range(n):
	ele = float(input("Enter the elements in the array :"))
	A.append(ele)
print("The array of marks is :", A)
print(bucket_sort(A))
