import os.path
def readFile():
    print("Reading from existing file")
    cond = False
    while (cond == False):
        print("Write the name of the file you would like to me to read from")
        name = raw_input()
        if (os.path.isfile(name)):
            cond = True
        else:
            print("Input Error: There is no file with that name in this context")

    return name

def createFile():
    print("Creating a new file")
    cond = "false"
    while( cond == "false"):
        print("Write a name for the file")
        name = raw_input()
        print(os.path.isfile(name))
        if (os.path.isfile(name) == True):
            print("Input Error: A file with that name already exists in this context")
        else:
            cond = "true"
    writeFile(name)
    print("\n")
    return name

def writeFile(name):
    fd = open(name, "w")
    cond = False;
    while (cond == False):
        print("How many books would you like me to choose from")
        num = unicode(raw_input(), 'utf-8') #isnumeric only works on unicode strings
        if (not num.isnumeric()):
            print("Input Error: The NUMBER of books must be a NUMBER... ")
        else:
            cond = True
    fd.write(str(num) + "\n") #Read format requires first line to be the number of books in the file
    # The program asumes that the user will write different books every line
    for i in xrange(int(num)):
        aux = i+1 # Need this variable because if not it will start at 1
        print("Write book number " + str(aux))
        book = raw_input()
        fd.write(book + "\n")
    fd.close()
