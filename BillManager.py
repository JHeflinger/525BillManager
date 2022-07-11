from os.path import exists

global username
global numRoommates
global numUnavailable
global numBills
global bills

username = ""
numRoommates = 0
numUnavailable = 0
numBills = 0
bills = []

def setUp():
    global username
    global numRoommates
    global numUnavailable
    global numBills
    global bills
    if exists("settings.txt"):
        with open("settings.txt", 'r') as f:
            lines = f.readlines()
            username = lines[1][0:len(lines[1]) - 1]
            numRoommates = int(lines[2])
            numUnavailable = int(lines[3])
            numBills = int(lines[4][0:len(lines[4]) - 1])
            for i in range(numBills):
                bills.append(lines[5 + i][0:len(lines[5 + i]) - 1])
        sysPrint("Welcome to 525BillManager! Use the command \"h\" or \"help\" for a list of commands.")
    else:
        sysPrint("Welcome to 525BillManager! It appears this is your first time using 525BillManager. In order to continue, you must create a settings file. Would you like to make one now? (y/n)")
        yOrN = getYorN()
        if yOrN == "n":
            global appRunning
            appRunning = False
            sysPrint("Thank you for using 525BillManager. Shutting system down now...")
            return
        else:
            settings = ["SETTINGS DOCUMENT: PLEASE REFRAIN FROM EDITING THIS DOCUMENT. UNAUTHORIZED EDITS TO THIS DOCUMENT MAY CAUSE PROGRAM FAILURES"]
            sysPrint("Creating new settings document...")

            sysPrint("What is your name?")
            username = getInput("NAME: ")
            settings.append(username)

            sysPrint("How many individuals will be splitting the bill?")
            num = validateNum(getInput("ROOMMATES: "))
            while num < 0:
                sysPrint("invalid input recieved. Please type in an integer value.")
                num = validateNum(getInput("ROOMMATES: "))
            numRoommates = num
            settings.append(num)

            sysPrint("How many individuals should not be included in the next usage billing cycle?")
            num = validateNum(getInput("NON-INCLUSIVE: "))
            while num < 0:
                sysPrint("invalid input recieved. Please type in an integer value.")
                num = validateNum(getInput("NON-INCLUSIVE: "))
            numUnavailable = num
            settings.append(num)

            sysPrint("How many bills are there?")
            num = validateNum(getInput("NUM-BILLS: "))
            while num < 0:
                sysPrint("invalid input recieved. Please type in an integer value.")
                num = validateNum(getInput("NUM-BILLS: "))
            numBills = num
            settings.append(num)

            sysPrint("What bills are there?")
            for i in range(num):
                str = getInput("NAME OF BILL: ")
                bills.append(str)
                settings.append(str)

            settings.append("billing records:")
            sysPrint("GENERATING SETTINGS FILE...")
            with open("settings.txt", 'w') as f:
                for s in settings:
                    temp = s.__str__() + "\n"
                    f.write(temp)
            sysPrint("Finished set-up! You can now use 525BillManager with your current settings. If you wish to modify these settings later, use the command \"e\" or \"edit\" to edit them.")
            sysPrint("Welcome to 525BillManager! Use the command \"h\" or \"help\" for a list of commands.")

def mainLoop():
    str = getInput()
    sysPrint(str)

def validateNum(str):
    num = -1
    try:
        num = int(str)
        if num >= 0:
            return num
        else:
            return -1
    except:
        return -1

def getYorN():
    yOrN = getInput()
    while yOrN != "y" and yOrN != "n":
        sysPrint("invalid input recieved. Please type in \"y\" or \"n\".")
        yOrN = getInput()
    return yOrN

def sysPrint(output):
    print("SYSTEM >> " + output)

def getInput(str=""):
    print("USER << " + str, end="")
    return input()

appRunning = True
setUp()
print(username)
print(numRoommates)
print(numUnavailable)
print(numBills)
print(bills)
while(appRunning):
    mainLoop()