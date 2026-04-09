import requests
def repeat():
  addr = input()
  vendor = requests.get('http://api.macvendors.com/' + addr).text


x = float(input('Enter any number:'))
a = float(input('Enter a second number: '))
print('a = Add \n s = Subtract \n m = Multiply \n d = Divide')
y = str(input('Enter an operator from the list above:'))
if (y == 'a'):
    print(x+a)
elif (y == 's'):
    print(x-a)
elif (y == 'm'):
    print(x*a)
elif (y == 'd'):
    print(x/a)
else:
    print('You did not choose an appropriate operator.')

r = int(input('To repeat the program, enter 1.\n To end the program, enter any number. \n Please enter a number:'))
if (r == 1):
    repeat()
else:
    quit()