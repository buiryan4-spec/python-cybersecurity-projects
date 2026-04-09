import time

print("\033[3;32;40mWelcome to the Message Cipher.")
print("\033[2;31;40m----------")
x = str(11111111)

key = str(10000000)
cipher = ""
for i in range(0, 8):
    multiplication = int(key[i]) + int(x[i])
    cipher = cipher + str(multiplication)
print(cipher)
print("Please wait while we crack your key.")

start = time.time()
for a in range(0, 100000000):
    for i in range(0, 8):
        test_cipher = ""
        test_cipher = test_cipher + str(int(a) + int(x))
        if test_cipher == cipher:
            print("Key found: ",a)
            end = time.time()
            print("Time Taken:", abs(end - start), "seconds\n")
            quit()
