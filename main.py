from nodes import * 
from queues import * 
from recursions import * 
from stack import * 
from loops import *
from palindromes import *


def main():
    santaClaus()
    getpalindromes()
    numbers()

def santaClaus():
    #Question 1
    s = node("S",None)
    s.addNodeAfter('A')
    s.addNodeAfter('T')
    s.addNodeAfter('N')
    s.addNodeAfter('A')

    #Question 2
    c = node("C",None)
    c.addNodeAfter("S")
    c.addNodeAfter("U")
    c.addNodeAfter("A")
    c.addNodeAfter("L")

    #Question 3 
    selection = s 

    #Question 4
    selection = selection.getLink()
    selection = selection.getLink()
    selection = selection.getLink()
    selection = selection.getLink() 

    #Question 5 
    selection.setLink(c)


def getpalindromes():
    pali = stack()
    notpali = stack()

    words = list(map(str,input("Enter ten words seperated by a space: ").split()))

    i = 0
    for i in range(len(words)):
        if (palindrome.isPalindrome(words[i])):
            pali.push(words[i])
        else:
            notpali.push(words[i])
    i += 1
    
    number1 = pali.size()
    print("These words are palindrome: ",end=" ")
    while (number1 > 0):
        print(node.listPosition(pali.getHead(),number1).get_data(),end=" ")
        number1 -= 1
    print()

    number2 = notpali.size()
    print("These words are palindrome: ",end=" ")
    while (number2 > 0):
        print(node.listPosition(notpali.getHead(),number2).get_data(),end=" ")
        number2 -= 1
    print()



def numbers():
    print("LOOP")
    loop.evens(-10,10)
    print()
    print("RECURSION")
    recursion.evens(-10,10)


if __name__ == "__main__":
    main()