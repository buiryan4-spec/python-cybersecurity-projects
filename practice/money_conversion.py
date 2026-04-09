print('\033[3;32;40m'
'░███████╗\n'
'██╔██╔══╝\n'
'╚██████╗░\n'
'░╚═██╔██╗\n'
"███████╔╝\n"
"╚══════╝░\n")




print("Welcome to the Money Converter for Dollars, Rupees, Pesos, Pounds, Euros")
print("\033[2;31;40m ----------")
print("\033[3;35;40m1: Dollar(s) \n2: Rupee(s) \n3: Peso(s) \n4: Pound(s) \n5: Euro(s)")
print("\033[2;31;40m ----------")
x = float(input("\033[1;34;40mPlease state the currency you want to convert from the list above (ex. 1 for Dollars):"))
y = float(input("Please state how much money you want to convert your selected currency into (ex. 100): "))
print("\033[2;31;40m ----------")
if x == 1:
    print("\033[3;35;40m1: Rupee(s) \n2: Peso(s) \n3: Pound(s) \n4: Euro(s)")
elif x == 2:
    print("1: Dollar(s) \n2: Peso(s) \n3: Pound(s) \n4: Euro(s)")
elif x == 3:
    print("1: Dollar(s) \n2: Rupee(s) \n3: Pound(s) \n4: Euro(s)")
elif x == 4:
    print("1: Dollar(s) \n2: Rupee(s) \n3: Peso(s) \n4: Euro(s)")
elif x == 5:
    print("1: Dollar(s) \n2: Rupee(s) \n3: Pesos(s) \n4: Pound(s)")
else:
    print("\033[1;36;40mNot a valid option.")
print("\033[2;31;40m ----------")
a = int(input("\033[1;34;40mPlease state which currency your selected currency should be converted to (ex. 3 for Pounds): "))
print("\033[2;31;40m ----------")
if y < 0:
    print("\033[1;36;40mYou're broke and in debt.")
    quit()
if x == 1:
    if a == 1:
        print('\033[4;31;40m',round(y*83.06,2), 'Rupees')
    elif a == 2:
        print(round(y*16.7, 6), 'Pesos')
    elif a == 3:
        print(round(y*0.78, 2), 'Pounds')
    elif a == 4:
        print(round(y/0.92, 2) ,'Euros')
    else:
        print("\033[1;36;40mNot a valid option.")
elif x == 2:
    if a == 1:
        print('\033[4;31;40m',round(y/83.06,2), 'Dollars')
    elif a == 2:
        print(round(y*0.20,2), 'Pesos')
    elif a == 3:
        print(round(y*0.0094,2), 'Pounds')
    elif a == 4:
        print(round(y/0.011,2), 'Euros')
    else:
        print("\033[1;36;40mNot a valid option.")
elif x == 3:
    if a == 1:
        print('\033[4;31;40m',round(y/16.7,2), 'Dollars')
    elif a == 2:
        print(round(y*4.96,2), 'Rupees')
    elif a == 3:
        print(round(y*0.047,2), 'Pounds')
    elif a == 4:
        print(round(y/0.052,2), 'Euros')
    else:
        print("\033[1;36;40mNot a valid option.")
elif x == 4:
    if a == 1:
        print('\033[4;31;40m',round(y/0.78,2), 'Dollars')
    elif a == 2:
        print(round(y/0.0094,2), 'Rupees')
    elif a == 3:
        print(round(y/0.047,2), 'Pesos')
    else:
        print("\033[1;36;40mNot a valid option.")
elif x == 5:
    if a == 1:
        print(round(y*1.09,2), 'Dollars')
    elif a == 2:
        print(round(y*90.6,2), 'Rupees')
    elif a == 3:
        print(round(y*19.05,2), 'Pesos')
    elif a == 4:
        print(round(y/0.85,2), 'Pounds')
else:
    print("\033[1;36;40mNot a valid option.")
print("\033[0;31;40m ----------")
print("\033[1;34;40mThank you for using the Money Conversion tool for Dollars, Rupees, Pesos, Pounds, Euros!")
print("Developed by Zainn, Aleese, and Ryan!")