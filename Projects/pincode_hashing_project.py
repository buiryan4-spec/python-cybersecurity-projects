print("\033[3;32;40mWelcome to the Pincode Hasher.")
print("\033[2;31;40m----------")

print("\033[3;35;40mPassword requirements: \nOnly 6 numbers allowed (From 0-9). \nNo decimals allowed.")
print("\033[2;31;40m----------")
y = str(input("\033[1;34;40mPlease enter a pincode: "))
for a in y:
    if a.isupper == True:
        print('Password must only have numbers.')
        exit()
    if a.islower() == True:
        print('Pincode must only have numbers')
        exit()
    if a == "!" or a == "@" or a == "#" or a == "$" or a == "%" or a == "^" or a == "&" or a == "*" or a == "/" or a == '-' or a == '_' or a == '(' or a == ')' or a == '+' or a == '=':
        print("Pincode must only have numbers.")
        exit()
    if len(y) > 6 or len(y) < 6:
        print("Pincode needs to be 6 numbers long.")
        exit()

hash = ''

for a in y:
    if a == '0':
        hash = hash+'8'
    if a == '1':
        hash = hash+'2'
    if a == '2':
        hash = hash+'9'
    if a == '3':
        hash = hash+'1'
    if a == '4':
        hash = hash+'5'
    if a == '5':
        hash = hash+'3'
    if a == '6':
        hash = hash+'7'
    if a == '7':
        hash = hash+'0'
    if a == '8':
        hash = hash+'4'
    if a == '9':
        hash = hash+'6'
print(hash)
print("Made by Zainn, Ryan, and Aleese!")