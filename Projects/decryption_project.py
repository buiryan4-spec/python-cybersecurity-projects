print("\033[3;32;40mWelcome to the decrypter! This program encrypts a message, then decrypts it.")
print('\033[2;31;40m -------------------------')
x = input("\033[2;34;40mPlease enter a string of 8 characters (numbers or letters only): ")
print('\033[2;31;40m -------------------------')
for a in x:
    if a == "!" or a == '-' or a == "@" or a == "#" or a == "$" or a == "%" or a == "^" or a == "&" or a == "*" or a == "/" or a == '-' or a == '_' or a == '(' or a == ')' or a == '+' or a == '=':
        print("Message must only have numbers or letters.")
        quit()
    if len(x) != 8:
        print("Not a valid length.")
        quit()
key = "10313211"
cipher = ""
decrypt = ""
while len(cipher) < 100:
    for i in range(len(key)):
        value = ord(x[i])
        multiplication = value + int(key[i])
        final = str(chr(multiplication))
        cipher += final

print("\033[3;35;40mYour cipher is:",cipher)

print("Your decrypted message is:")
for a in range(len(key)):
    value = ord(cipher[a])
    multiplication = value - int(key[a])
    final = str(chr(multiplication))
    decrypt += final
print(decrypt)
print("\033[3;35;40m\nDeveloped by: Zainn, Ryan, and Aleese")
