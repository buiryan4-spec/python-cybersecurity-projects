import time


print("\033[3;32;40mEnter 5 pincodes into the program.")
print("\033[2;31;40m----------")

print("\033[3;35;40mPassword requirements: \nOnly 8 numbers. \nNo decimals allowed.")
print("\033[2;31;40m----------")
y = str(input("\033[1;34;40mPlease enter a pincode: "))
x = str(input("\033[1;34;40mPlease enter a 2nd pincode: "))
z = str(input("\033[1;34;40mPlease enter a 3rd pincode: "))
c = str(input("\033[1;34;40mPlease enter a 4th pincode: "))
v = str(input("\033[1;34;40mPlease enter a 5th pincode: "))

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
    if len(y) != 8:
        print("Pincode needs to be 8 numbers long.")
        exit()
    # exit()
for a in x:
    if a.isupper == True:
        print('Password must only have numbers.')
        exit()
    if a.islower() == True:
        print('Pincode must only have numbers')
        exit()
    if a == "!" or a == "@" or a == "#" or a == "$" or a == "%" or a == "^" or a == "&" or a == "*" or a == "/" or a == '-' or a == '_' or a == '(' or a == ')' or a == '+' or a == '=':
        print("Pincode must only have numbers.")
        exit()
    if len(x) != 8:
        print("Pincode needs to be 8 numbers long.")
        exit()
    # exit()
for a in z:
    if a.isupper == True:
        print('Password must only have numbers.')
        exit()
    if a.islower() == True:
        print('Pincode must only have numbers')
        exit()
    if a == "!" or a == "@" or a == "#" or a == "$" or a == "%" or a == "^" or a == "&" or a == "*" or a == "/" or a == '-' or a == '_' or a == '(' or a == ')' or a == '+' or a == '=':
        print("Pincode must only have numbers.")
        exit()
    if len(z) != 8:
        print("Pincode needs to be 8 numbers long.")
        exit()
    # exit()
for a in c:
    if a.isupper == True:
        print('Password must only have numbers.')
        exit()
    if a.islower() == True:
        print('Pincode must only have numbers')
        exit()
    if a == "!" or a == "@" or a == "#" or a == "$" or a == "%" or a == "^" or a == "&" or a == "*" or a == "/" or a == '-' or a == '_' or a == '(' or a == ')' or a == '+' or a == '=':
        print("Pincode must only have numbers.")
        exit()
    if len(c) != 8:
        print("Pincode needs to be 8 numbers long.")
        exit()
    # exit()
for a in v:
    if a.isupper == True:
        print('Password must only have numbers.')
        exit()
    if a.islower() == True:
        print('Pincode must only have numbers')
        exit()
    if a == "!" or a == "@" or a == "#" or a == "$" or a == "%" or a == "^" or a == "&" or a == "*" or a == "/" or a == '-' or a == '_' or a == '(' or a == ')' or a == '+' or a == '=':
        print("Pincode must only have numbers.")
        exit()
    if len(v) != 8:
        print("Pincode needs to be 8 numbers long.")
        exit()
    # exit()

hash1 = ''
hash2 = ''
hash3 = ''
hash4 = ''
hash5 = ''

for a in y:
    if a == '0':
        hash1 = hash1+'8'
    if a == '1':
        hash1 = hash1+'2'
    if a == '2':
        hash1 = hash1+'9'
    if a == '3':
        hash1 = hash1+'1'
    if a == '4':
        hash1 = hash1+'5'
    if a == '5':
        hash1 = hash1+'3'
    if a == '6':
        hash1 = hash1+'7'
    if a == '7':
        hash1 = hash1+'0'
    if a == '8':
        hash1 = hash1+'4'
    if a == '9':
        hash1 = hash1+'6'
for a in x:
    if a == '0':
        hash2 = hash2+'8'
    if a == '1':
        hash2 = hash2+'2'
    if a == '2':
        hash2 = hash2+'9'
    if a == '3':
        hash2 = hash2+'1'
    if a == '4':
        hash2 = hash2+'5'
    if a == '5':
        hash2 = hash2+'3'
    if a == '6':
        hash2 = hash2+'7'
    if a == '7':
        hash2 = hash2+'0'
    if a == '8':
        hash2 = hash2+'4'
    if a == '9':
        hash2 = hash2+'6'
for a in z:
    if a == '0':
        hash3 = hash3+'8'
    if a == '1':
        hash3 = hash3+'2'
    if a == '2':
        hash3 = hash3+'9'
    if a == '3':
        hash3 = hash3+'1'
    if a == '4':
        hash3 = hash3+'5'
    if a == '5':
        hash3 = hash3+'3'
    if a == '6':
        hash3 = hash3+'7'
    if a == '7':
        hash3 = hash3+'0'
    if a == '8':
        hash3 = hash3+'4'
    if a == '9':
        hash3 = hash3+'6'
for a in c:
    if a == '0':
        hash4 = hash4+'8'
    if a == '1':
        hash4 = hash4+'2'
    if a == '2':
        hash4 = hash4+'9'
    if a == '3':
        hash4 = hash4+'1'
    if a == '4':
        hash4 = hash4+'5'
    if a == '5':
        hash4 = hash4+'3'
    if a == '6':
        hash4 = hash4+'7'
    if a == '7':
        hash4 = hash4+'0'
    if a == '8':
        hash4 = hash4+'4'
    if a == '9':
        hash4 = hash4+'6'
for a in v:
    if a == '0':
        hash5 = hash5+'8'
    if a == '1':
        hash5 = hash5+'2'
    if a == '2':
        hash5 = hash5+'9'
    if a == '3':
        hash5 = hash5+'1'
    if a == '4':
        hash5 = hash5+'5'
    if a == '5':
        hash5 = hash5+'3'
    if a == '6':
        hash5 = hash5+'7'
    if a == '7':
        hash5 = hash5+'0'
    if a == '8':
        hash5 = hash5+'4'
    if a == '9':
        hash5 = hash5+'6'

print("Please wait.")
start = time.time()

for a in range(0, 100000000):
    if a == int(hash1):
        print("Hash found:",a)
        end = time.time()
        print("Time Taken:", abs(end - start), "seconds\n")
    elif a == int(hash2):
        print("Hash found:", a)
        end = time.time()
        print("Time Taken:", abs(end - start), "seconds\n")
    elif a == int(hash3):
        print("Hash found:", a)
        end = time.time()
        print("Time Taken:", abs(end - start), "seconds\n")
    elif a == int(hash4):
        print("Hash found:", a)
        end = time.time()
        print("Time Taken:", abs(end - start), "seconds\n")
    elif a == int(hash5):
        print("Hash found:", a)
        end = time.time()
        print("Time Taken:", abs(end - start), "seconds\n")
print("Made by Zainn, Ryan, and Aleese!")