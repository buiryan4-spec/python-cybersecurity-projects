import time
from playsound import playsound
a = float(input("\033[1;34;40mPlease state the number of hours (Only a number): "))
b = float(input("Please state the number of minutes (Only a number):" ))
c = float(input("Please state the number of seconds (Only a number): "))
if a < 0 or b < 0 or b >= 60 or c < 0 or c >= 60:
    print("Not a valid answer")
    quit()
a = int(a)
b = int(b)
c = int(c)
for i in range(int(a), -1, -1):
    for d in range(int(b), -1, -1):
        for e in range(int(c), -1, -1):
            time.sleep(1)
            print('\033[0;31;40m',i, ':',d,  ':' ,e)
            if e == 0:
                c = 59
                d = d-1
                if d == 0:
                    b=59
                    i = i-1
                    if i == -1:
                        i = 0
print("Your timer has ended!")
print("Made by Aleese, Ryan, Zainn!")
playsound(r'C:\Users\shsi_c115\Downloads\oversimplified-alarm-clock-113180.mp3')