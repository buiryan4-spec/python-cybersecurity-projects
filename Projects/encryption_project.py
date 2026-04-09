print("\033[3;32;40mWelcome to the Message Cipher.")
print("\033[2;31;40m----------")
print("\033[3;35;40mMessage requirements: \nOnly 8 numbers allowed (From 0-9). \nNo decimals allowed.")
print("\033[2;31;40m----------")
ans = 'y'
final =''
while ans == 'y'or ans == 'Y':
    x = input("Please enter a message consisting of only 8 numbers (ex. 12345678): ")
    print("\033[2;31;40m----------")
    for a in x:
        if a == "!" or a == "@" or a == "#" or a == "$" or a == "%" or a == "^" or a == "&" or a == "*" or a == "/" or a == '-' or a == '_' or a == '(' or a == ')' or a == '+' or a == '=':
            print("Message must only have numbers.")
            exit()
        if a.isupper == True:
            print('Message must only have numbers.')
            exit()
        if a.islower() == True:
            print('Message must only have numbers')
            exit()
        if len(x) != 8:
            print('Message must only have  8 numbers')
            exit()
    key = str(11111111)
    cipher = ""
    for i in range(0, len(x)):
        multiplication = int(key[i]) + int(x[i])
        cipher = cipher + str(multiplication)
        final = final + cipher
    ans = input("Would you like to try again? (y/n)")
print(final)