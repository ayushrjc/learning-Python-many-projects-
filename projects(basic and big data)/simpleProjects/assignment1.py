def qsn1():
    print("To check weather two strings are anagrams. Ex- LISTEN and SILENT\n")
    a = input("Enter any String\n")
    b = input("ENter another String\n")
    if sorted(a) == (sorted(b)):
        print("yes They are anagram")
    else:
        print("No they are not")
    main()


def qsn2():
    print("To reverse to strings without using reverse function\n")
    a = input("Enter any String\n")
    # b= " "
    # j = len(a)
    # for i in range(len(a)):
    #     b[j - 1] = a[i]
    #     j -= 1
    # s = ""
    # print(s.join(b))
    a=a[::-1]
    print(a)
    main()


def qsn3():
    print("Program to write no. of upper case letter and lower case letter\n")
    c1 = 0
    c2 = 0
    s = input("Enter any String")
    for i in range(len(s)):
        if s[i] == " ":
            i += 1
        else:
            if s[i].isupper():
                c1 += 1
            else:
                c2 += 1
    print("upper case : ", c1, "\nLowwer case : ", c2)
    main()





def gs(arr, n):
    i = 0
    while i < n:
        if i == 0:
            i = i + 1
        if arr[i] >= arr[i - 1]:
            i = i + 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i = i - 1

    return arr


def qsn4():
    arr = list(map(int,input("Enter list elements with space\n").split()))
    n = len(arr)

    arr = gs(arr, n)

    print("Sorted elements: ")
    for i in arr:
        print(i,end=" ")
    print("\n")
    main()

def qsn5():
    arr = list(map(int,input("Enter list elements with space\n").split()))
    a = []
    flag = 0
    for i in range(len(arr)):
        a = arr[0:i]
        a.extend(arr[i + 1:])
        if arr[i] in a:
            flag == 1
            print(arr[i])
            break
        else:
            continue
    if flag==0:
        print("-1")
    main()

def main():
    n = int(input("Enter any number (1-5) to execute question\nPress 0 to exit\n"))
    f=True
    while(f):
        if n == 1:
            qsn1()
        elif n == 2:
            qsn2()
        elif n == 3:
            qsn3()
        elif n == 4:
            qsn4()
        elif n == 5:
            qsn5()
        elif n==0:
            f=False
        else:
            print("Invalid Input")

main()
