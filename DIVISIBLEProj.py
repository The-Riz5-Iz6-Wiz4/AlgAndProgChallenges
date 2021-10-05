#input an integer value, if divisible by 11 print a
#if divisible by 9, print b
#if divisible by 7, print c
#if it's divisible by 2, print d
#everything else print e

Number = int(input("Enter a number here: "))

if Number%11 == 0:
    print("a", end="")
if Number%9 == 0:
    print("b", end="")
if Number%7 == 0:
    print("c", end="")
if Number%2 == 0:
    print("d", end="")
if Number%11 > 0 and Number%9 > 0 and Number%7 > 0 and Number%2 > 0:
    print("e")