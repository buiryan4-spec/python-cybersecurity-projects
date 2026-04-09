print("\033[3;32;40mWelcome to the Password Analyzer! \nThis program analyzes your password to rate it.")
print("\033[2;31;40m----------")
x = str(input("\033[1;34;40mPlease enter a username: "))
print("\033[2;31;40m----------")

lowercase = 0
Pass = 'y'

while Pass == 'y' or Pass == 'Y' :
    print("\033[3;35;40mPassword requirements: \nOnly lowercase characters. \nAt least 8 characters.")
    print("\033[2;31;40m----------")
    y = str(input("\033[1;34;40mPlease enter a password: "))
    for a in y:
        if a.isupper == True:
            print('Password must only contain lowercase characters.')
            quit()
        if a == "!" or a == "@" or a == "#" or a == "$" or a == "%" or a == "^" or a == "&" or a == "*" or a == "/":
            print("Password must only contain lowercase characters.")
            quit()
        if a == '1' or a == '2' or a == '3' or a == '4' or a == '5' or a == '6' or a == '7' or a == '8' or a == '9' or a == '0':
            print("Password must only contain lowercase characters.")
            quit()
        if a.islower == True:
            lowercase += 1
            if lowercase < 1:
                print("Password needs lowercase characters.")
                quit()
        if len(y) < 8:
            print("Password needs at least 8 characters.")
            quit()
    Pass = 'n'

hash = ""

for a in y:
    if a == 'a':
        hash = hash+'e'
    if a == 'b':
        hash = hash+'u'
    if a == 'c':
        hash = hash+'g'
    if a == 'd':
        hash = hash+'n'
    if a == 'e':
        hash = hash+'o'
    if a == 'f':
        hash = hash+'t'
    if a == 'g':
        hash = hash+'x'
    if a == 'h':
        hash = hash+'q'
    if a == 'i':
        hash = hash+'z'
    if a == 'j':
        hash = hash+'j'
    if a == 'k':
        hash = hash+'m'
    if a == 'l':
        hash = hash+'s'
    if a == 'm':
        hash = hash+'l'
    if a == 'n':
        hash = hash+'b'
    if a == 'o':
        hash = hash+'i'
    if a == 'p':
        hash = hash+'h'
    if a == 'q':
        hash = hash+'y'
    if a == 'r':
        hash = hash+'v'
    if a == 's':
        hash = hash+'a'
    if a == 't':
        hash = hash+'p'
    if a == 'u':
        hash = hash+'c'
    if a == 'v':
        hash = hash+'d'
    if a == 'w':
        hash = hash+'w'
    if a == 'x':
        hash = hash+'r'
    if a == 'y':
        hash = hash+'f'
    if a == 'z':
        hash = hash + 'k'
print(hash)