# Educational project demonstrating how keyloggers work for cybersecurity awareness
# Created as part of a learning program (UOP Summer Institute, 2024)

from PIL import ImageGrab

print("\033[3;32;40m           ▓▓▓▓\n"                                                                                  
         "            ██▒▒████\n     "                                                                         
"        ██▒▒▒▒██▓▓\n"                                                                          
"              ██▒▒▒▒▒▒████\n"                                                                      
"        ████    ██▒▒▒▒▒▒▒▒████\n"                                                                  
"        ██▒▒▓▓  ░░████▒▒▒▒▒▒▒▒▓▓████                                    ████░░░░░░██\n"            
"        ██▒▒▒▒██      ██▒▒▒▒▒▒▒▒▒▒▒▒██▓▓██                        ██████░░░░░░░░░░░░██████\n"      
"        ██▒▒▒▒▒▒██      ████▒▒▒▒▒▒▒▒▒▒▒▒▒▒████              ██████░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒████\n"  
"        ██▒▒▒▒▒▒▒▒██        ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████████░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░██\n"
"          ██▒▒▒▒▒▒▒▒▓▓        ████▒▒▒▒▒▒▒▒████▓▓▓▓▓▓▒▒▓▓██░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░██\n"
"████████  ██▒▒▒▒▒▒▒▒▒▒██    ████████▒▒▒▒██▓▓▓▓▓▓▓▓▓▓▒▒▓▓██▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██\n"
"██▒▒▒▒▒▒████████████████████░░░░░░░░████▒▒██▓▓▓▓▓▓▓▓▒▒▓▓██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████\n"  
"  ██▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████▓▓████░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓██\n"      
"    ████████▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████████\n"              
"      ██▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████\n"                        
"        ████████▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░██▒▒██▒▒▒▒▓▓▓▓▓▓▒▒▓▓██\n"                            
"            ██▒▒██      ██████████████████████    ██▒▒██▓▓▓▓▓▓▒▒▓▓██\n"                            
"            ████                                    ██▒▒████████████\n"                            
"                                                      ██▒▒██\n"                                    
"                                                        ████\n" )



print("Welcome to the Travel Site!")
print("\033[2;31;40m----------")

a = str("Paris")
b = ("$616")
c = ("$173")
d = str("Baguette")

e = str("London")
f = ("$771")
g = ("$211")
h = str("Fish and Chips")

i = str("Italy")
j = ("$670")
k = ("$188")
l = str("Spaghetti and Meatballs")

m = str("New York")
n = ("$198")
o = ("$205")
p = str("Dollar pizza")

file1 = open("Keylogged.txt", "w")

import pyautogui

choice = 'y'

while choice == 'y':
    x = str(input("\033[1;34;40mPlease enter your destination (Case sensitive)(ex. London): "))
    if x == ("Paris"):
        print('\033[3;35;40m',b, 'for a flight to Paris from the SFO airport.')
        print(c, 'per night at a hotel in Paris.')
        print(d, 'is the food specialty of Paris.')
        my_screenshot = pyautogui.screenshot()
        my_screenshot.save(r"C:\Users\shsi_c115\Downloads\screenshot_1.png")
        file1.write(x+b+c+d + "\n")
    elif x==('London'):
        print('\033[3;35;40m',f,"for a flight to London from the SFO airport.")
        print(g, 'per night at a hotel in London.')
        print(h,'is the food specialty of London.')
        my_screenshot = pyautogui.screenshot()
        my_screenshot.save(r"C:\Users\shsi_c115\Downloads\screenshot_1.png")
        file1.write(x+f+g+h+ "\n")
    elif x == ('Italy'):
        print('\033[3;35;40m',j,'for a flight to London from the SFO airport.')
        print(k,'per night at a hotel in Italy.')
        print(l, 'is the food specialty in Italy.')
        my_screenshot = pyautogui.screenshot()
        my_screenshot.save(r"C:\Users\shsi_c115\Downloads\screenshot_1.png")
        file1.write(x+j+k+l+ "\n")
    elif x==('New York'):
        print('\033[3;35;40m',n,'for a flight to New York.')
        print(o,'per night at a hotel in New York.')
        print(p,'is the food specialty in New York.')
        my_screenshot = pyautogui.screenshot()
        my_screenshot.save(r"C:\Users\shsi_c115\Downloads\ss1.png")
        file1.write(x+n+o+p+ "\n")
    else:
        print("\033[2;31;40mDestination Not Found")

    choice = str(input("\033[1;34;40mDo you want to try again? (y/n)"))
print("Thank you for using the Travel Application!")
print("Made by Zainn, Ryan, Aleese!")