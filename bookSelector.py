
import random
from fileManager import readFile, createFile

def readBook(name):
    bookList = open(name, "r")
    maxBooks = int(bookList.readline())

    bookNumber = random.randint(1, maxBooks)
    acum = 1;
    for line in bookList: #Since we already read the first line, it starts from the second
        if (acum == bookNumber):
            print "Book Selected: "
            print line
            break
        acum+=1

    bookList.close()


print("Hello, I am the book wizard")

cond = "false";
while (cond == "false"):
    print("Do you want me to select a book from an existing file? (y/n)")
    userInp = raw_input()
    if (userInp == "y" or userInp == "Y"):
        cond = "true"
        name= readFile()
    else:
        if (userInp == "n" or userInp == "N"):
            cond = "true"
            name = createFile()
        else:
            print("Invalid input, try again!")
readBook(name)
