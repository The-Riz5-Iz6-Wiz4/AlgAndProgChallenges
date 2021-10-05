Score = int(input("Enter your score here:"))

if Score == 100:
    print("A+")
elif 90 <= Score < 100:
    print("A")
elif 80 <= Score < 90:
    print("B")
elif 70 <= Score < 80:
    print("C")
elif 60 <= Score < 70:
    print("D")
elif 50 <= Score < 60:
    print("E")
elif Score < 50:
    print("F")