# Using Loops

'''def rev(s):
    str = " "
    for i in s:
        str = i + str
    return str
s="live.interviews@joinsuperset.com"    

print ("The reversed string(using loops) is : ",end=" ")
print (rev(s))
'''

#Using Recursion

'''
from re import S


def rev(s):
    if len(s)==0:
        return s
    else:
        return rev(s[1:])+s[0]

s="live.interviews@joinsuperset.com" 

print ("The reversed string(using loops) is : ",end=" ")
print (rev(s))
'''

#Using extended slice syntax

'''
def rev(s):
    s=s[::-1]
    return s'''

def rev(s):
    s = "".join(reversed(s))
    return s

s=" Nixk.Jadhav " 

print ("The reversed string(using loops) is : ",end=" ")
print (rev(s))

