# cook your dish here
T  = int(input("Enter number of testcase: "))
for i in range(T):
    pal = str(input("enter the string: ")).lower()
    palin = pal[::-1]
    if pal == palin:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")