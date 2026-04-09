print("------------------------------------")
x = str(input("Please enter a word: "))
print("------------------------------------")
y = str(input("Please state which letter from the word you want (case sensitive): "))
print("------------------------------------")
a = 0
for i in x:
    if i==y:
        a = a+1
if a>1 or a<1:
    print("------------------------------------")
    print("The letter", y, "appears", a, "times.")
    print("------------------------------------")
elif a == 1:
    print("------------------------------------")
    print("The letter", y, "appears", a, "time.")
    print("------------------------------------")