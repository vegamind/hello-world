
#PYTHON BASICS

#VARIABLES
"""
firstName = 'ashley'
lastName = 'gilliam'
"""


#DATA TYPES

#STRINGS (str)
"""
#print(firstName + " " + lastName)
"""
#STRING MANIPULATION
#strings can be in single/double/triple quotes
    #if you use single quotes, you have to use a \ before any apostrophes

"""
Example of triple quote string.
"""

email = '''Eric,

Hello.

Thank you.
vega'''

"""
Triple quotes = multiline comment.
"""

#b before string = binary version
#r before string = raw string

print(email.split())

#if "Eric".lower() not in email:
    #print("Eric was mentioned in this email.")

#.split turns string into a list
#.join turns list into string

#STRING SPLIT
'''
anything = "Let's make it a sentence."

anything = anything.split(" ")
'''
#STRING JOIN

'''
anything = "Let's make it a sentence."

anything = anything.split(" ")

empty = "-".join(anything)
print(empty)
'''

#STRING STRIP
'''
print("Yo dude.".center(30,"."))
'''
'''
print("were learning how to strip".strip(" "))
'''

#STRING MANIPULATON EXAMPLE 1
"""
# this program says hello and asks for my name

print ('hello world')
print ('what is your name?') #ask for their name
myName = input()
print ('it is good to meet you, ' + myName)
print ('the length of your name is:')
print(len(myName))
print('what is your age?') #ask for their age
myAge = input()
print ('you will be ' + str(int(myAge) +1) + ' in a year')
"""
#STRING MANIPULATON EXAMPLE 2
"""
print ('How many cats do you have?')
numCats = input()
try:
    if int(numCats) > 4:
        print('That is a lot of kitties!!!')
    else:
        print ('Aww, that is great!')
except ValueError:
    print ('You did not enter a valid number.')
"""

#PYPERCLIP
'''
#import pyperclip
#import pyperclip as p
from pyperclip import copy as c

def p(word):
    print(word)

p("work")
c("Goodbye world!")

#a = pyperclip.paste()

#print(a)
'''

#BOOLEAN

#LISTS
"""
newList = ["Sam", "Name", 9, 8.1]
"""

#INTEGERS (int)
#FLOATS

#MATH


#STATEMENTS
#IF/ELIF
"""
name = 'Bob'
age = 3000
if name == 'Alice':
    print ('hi alice')
elif age < 12:
    print ('you are not alice, kiddo')
elif age > 2000:
    print ('you are not alice, you are a vamp')
elif age > 100:
    print ('you are not alice, granny')
"""

#IF/ELSE Example 1
"""
password = 'swordfish'
if password == 'suckerfish':
    print ('Access Granted')
else:
    print ('Wrong password.')
"""
#IF/ELSE Example 2
"""
print ('Enter a name: ')
name = input()
if name:
    print ('Thank you')
else:
    print ('Error')
"""

#IF
"""
name = 'Alice'
if name == 'Alice':
    print ('Hi Alice')
print('Done')
"""


#LOOPS
#FOR LOOP
"""
print ('my name is ')
for i in range (0, 10, 2):
    print('yo ' + str(i))
"""

#WHILE LOOP EXAMPLE 1
"""
newList = ["Sam", "Name", 9, 8.1]
i = 0
while i < len(newList):
    print('poop')
    i += 1
"""
#WHILE LOOP EXAMPLE 2
"""
spam = 0
while spam < 5:
    print ('Hi')
    spam = spam +1
"""
#WHILE LOOP EXAMPLE 3
"""
name = ''
while name != 'your name':
    print ('please type your name')
    name = input()
print ('thank you')
"""


#FUNCTIONS
#LEN FUNCTION
"""
newList = ["Sam", "Name", 9, 8.1]
print(len(newList))
"""

#method is fuction tied to variable







#GENERAL NOTES

#HARD exit
'''
import sys

sys.exit()
'''

#creates breaking point in code
#print("=" * 10)

#line break
"""
print('hello', end = '')
print('world')
"""


#SCOPES - LOCAL vs. global
"""
#variables are either global or local, cannot be both or neither

spam = 42  #global scope/variable begins when program starts and ends when
              #program terminates permanent scope cannot use local variables

def eggs():
    spam = 42  #local scope/variable begins when function is called and ends
                  #when function returns all variables inside are forgotten and
                        #local scope is destroyed temporary scope can use
                             #global variables cannot use variables in other
                                 #functions   you can use same variable names
                                #for different variables if they are in different
                                         #functions if a variable is assigned
                                   #in the funtcion then that variable
    #is a local one, if the variable is not assigned in that function
    #then it is a global variable.

print ('breakfast')
print ('yum')
"""


#READ/WRITE FILES

'''
import os

#TEXT FILES

#testFile = open("test5.txt", "w") #creates text file because of the argument of w, w = create w also overwrites
testFile = open("test5.txt", "a") #a appends to file
testFile.write("\nPeople suck.") #writes data into file created
testFile.close() #closes open file
'''

#METADATA TOOLS
#print(os.path.isdir("C:\\Users\\gilliama\\"))
#print(os.path.exists("C:\\Users\\gilliama\\")) #checks to see if directory exists
#most important tool
#print(os.listdir()) #gives all directories in current working directory
#print(os.path.isabs("12-14-17.py")) #tells you if the path is absolute or not
#print(os.path.getsize("12-14-17.py")) #gets size of file
#print(os.path.abspath("12-14-17.py")) #gives absolute path
#print(os.path.relpath("12-14-17.py", "C:\\ftp\\an")) #gives relative path
#os.makedirs("C:\\Ashley\\Eric\\Love Forever\\pi\\")  #makes a directory/s
#os.chdir('C:/')  #change directory
#print(os.getcwd())  #see the current directory
#./filename #you can pull up a file
#print("../")

#FIRST CLASS SESSION
'''
def Main ():

    Directory = "M:\\network_repository\\_ITC Tools\\_Eric\icpcdc1r013\\"
    DirectoryContents = os.listdir(Directory)
    TextOnly = []
    RackNames = []


    for dir in DirectoryContents:

        if ".txt" in dir:
            TextOnly.append (Directory + dir)
            RackNames.append(dir[0:-4])
            print(RackNames)

    WriteFile = open(Directory + "outputag.log", "w+")


    for file in TextOnly:

        tempFile = open(file, "r")
        tempFileRead = tempFile.readlines()

        i = 0

        while i < len(tempFileRead):

            if "Boot Order Log" in tempFileRead[i]:

                Rackname = file
                RackName = RackName.split("\\")
                RackName = RackName[-1]
                RackName = [0:-4]
                WriteFile.write("======RACK NAME: " + RackName + "======\n")

                for a in range (0, 16):
                    WriteFile.write(tempFileRead[i + a])

    WriteFile.write("\n\n\n\n")

            i += 1


        tempFile.close()
    WriteFile.close()
    return


Main ()
'''
