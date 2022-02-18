import re
from turtle import st

print(' Our Magic no. ')
print(" Type 'quit' to exit \n ")

prev = 0
run = True

def perfMath():
    global run, prev
    eq = ""
    if prev == 0:
        eq = input(" Enter Eq :- ")
    else:
        eq = input(str(prev))
    if eq == 'quit':
        print("Good Bye!!!")
        run = False
    else:
        eq = re.sub( '[a-zA-Z,.:()" "]', '', eq)
        if prev == 0:
            prev = eval(eq)
        else:
            prev = eval(str(prev) + eq)
        #print("You Typed", prev)
    #print(" You Typed", eq)
while run:
    perfMath()
