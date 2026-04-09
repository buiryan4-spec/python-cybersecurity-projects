x=float(input("Please Enter Your Grade Percent:"))
if (x<=59.99):
    print("F")
elif (x>=60 and x<= 63.99):
    print("D-")
elif (x<=66.99 and x>=64):
    print("D")
elif (x<=69.99 and x>=67):
    print("D+")
elif (x<= 73.99 and x>= 70):
    print("C-")
elif (x<=76.99 and x>=74):
    print("C")
elif (x<=79.99 and x>= 77):
    print("C+")
elif (x<= 83.99 and x>= 80):
    print("B-")
elif (x <= 86.99 and x >=84):
    print("B")
elif (x<=89.99 and x>=87):
    print("B+")
elif (x<= 93.99 and x>= 90):
    print("A-")
elif (x<=96.99 and x>= 94):
    print("A")
elif (x<=100 and x>= 97):
    print("A+")
elif (x>100):
    print("Not a valid percentage.")
elif (x<0):
    print("Not a valid percentage.")