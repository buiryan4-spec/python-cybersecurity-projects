print('_________')
print("|      0|")
print('|-------|')
print("| □ □ □ |")
print('| □ □ □ |')
print('| □ □ □ |')
print('| □ □ □ |')
print(u'‎\u0304',u'‎\u0304',u'‎\u0304',u'‎\u0304',u'‎\u0304',u'‎\u0304',u'‎\u0304',u'‎\u0304',u'‎\u0304',u'‎\u0304')
print('\033[1;34;40m Welcome to the Calculator')
print('\033[2;31;40m -------------------------')
x = float(input('\033[2;34;40m Please enter any number: '))
y = float(input(" Please enter a second number: "))
print('\033[2;31;40m -------------------------')
print("\033[3;35;40m 1: Addition \n 2: Subtraction \n 3: Multiplication \n 4: Division \n 5: Modulus \n 6: All prime numbers between",x ,"and",y,)
a = int(input("\033[2;34;40m Please enter the appropriate number for an operation from the list above: "))
print('\033[2;31;40m -------------------------')
if a == 1:
    b = x+y
    print("\033[2;34;40m The sum of the numbers is:" '\033[4;31;40m' ,b)
elif a == 2:
    b = x-y
    print("\033[2;34;40m The difference of the two numbers is:"'\033[4;31;40m',b)
elif a == 3:
    b = x*y
    print("\033[2;34;40m The product of the two numbers is:"'\033[4;31;40m',b)
elif a == 4:
    if y==0:
        print("\033[2;34;40m Undefined")
    else:
        b = x/y
        print("\033[2;34;40m The quotient of the two numbers is:" '\033[4;31;40m',b)
elif a == 5:
    if y==0:
        print("\033[2;34;40m Undefined")
    else:
        b = x%y
        print("\033[2;34;40m The remainder of the two numbers is:"'\033[4;31;40m',b)
elif a == 6:
    if x < y:
        for Number in range(int(x), int(y)):
            count = 0
            for i in range(2, (Number // 2 + 1)):
                if Number % i == 0:
                    count += 1
                    break
            if count == 0 and Number != 1:
                print(Number, end=' ')
    else:
        print("\033[2;34;40m Second number is greater than first number.")
else:
    print(a, "\033[2;34;40m is not an appropriate operation.")
print('\033[2;31;40m \n -------------------------')
print("\033[3;35;40m Developed by: Ryan, Zainn, Aleese")
