#from Node import *

def removeSpaces(s):
    newS = ''
    for c in s:
        if c !=" ":
            newS += c
    return newS

myString = "Hello world"
myString = removeSpaces(myString)
print(myString) #Should print "Helloworld"

def removeSpaces2(L):
    newL = []
    for c in L:
        if c!=" ":
            newL += [c]
    L = newL
    return L
        
myList = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
myString = removeSpaces2(myList)
print(myList) #Should print [’H’, ’e’, ’l’, ’l’, ’o’, ’w’, ’o’, ’r’, ’l’, ’d’]

class Person:
    def __init__(self,F,N):
        self.firstName = F
        self.lastName = N
    def __repr__(self):
        return self.firstName + ' ' + self.lastName

p = Person("Kermit", "Ruffins")
print(p)
