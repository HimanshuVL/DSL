def longest_word():
    n = int(input("Enter the number of elements in the list :"))
    string = []
    for i in range(0, n):
        ele = input("Enter the words :")
        string.append(ele)
    print("The list is :", string)
    max_length = len(string[0])
    temp = string[0]
    for words in string:
        if len(words) > max_length:
            temp = words
    print("The word with maximum length is :", temp)
    print("The length of the word is :", max_length)


def palindrome():
    string = input("Enter the string :")
    if string == string[::-1]:
        print("The string is palindrome")
    else:
        print("It is not a palindrome string")


def frequency():
    string = input("Enter some string: ")
    dic = {}
    for i in string:
        keys = dic.keys()
        if i in keys:
            dic[i] += 1
        else:
            dic[i] = 1
    print(dic)


def occur_words():
    string = input("\n Enter some statement: ")
    counts = dict()
    words = string.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    print(counts)


def find_substring():
    string = input("\n Enter some statement: ")
    word = input("\n Enter the substring to be searched: ")
    for i in range(len(string) - len(word) + 1):
        if string[i:i + len(word)] == word:
            return i
    return 'Not Found'


while True:
    print("Operation on string are :")
    print("1.Longest Word")
    print("2.Frequency")
    print("3.Palindrome")
    print("4.Find Substring")
    print("5.Occur words")
    print("6.Exit")
    c = int(input("Enter  the number of the operation :"))
    if c == 1:
        longest_word()
    elif c == 2:
        frequency()
    elif c == 3:
        palindrome()
    elif c == 4:
        find_substring()
    elif c == 5:
        occur_words()
    elif c == 6:
        break
    else:
        print("Not Found")
        break
