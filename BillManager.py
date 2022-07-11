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
    if str == "h" or str == "help":
        sysPrint("Available commands:\n\t\t help - brings up a list of available commands \n\t\t edit - edit the current billing settings \n\t\t quit - quits the application \n\t\t bill - create a bill to split")
    elif str == "q" or str == "quit":
        sysPrint("Quitting application...")
        global appRunning
        appRunning = False
        return
    elif str == "e" or str == "edit":
        sysPrint("You can edit your name, roommates, non-inclusive roommates, amount of bills, or your bills. Which would you like to edit?")
        editSettings()

def editSettings():
    global numBills
    global username
    global numRoommates
    global numUnavailable
    global bills
    settings = ["SETTINGS DOCUMENT: PLEASE REFRAIN FROM EDITING THIS DOCUMENT. UNAUTHORIZED EDITS TO THIS DOCUMENT MAY CAUSE PROGRAM FAILURES"]
    setting = getInput("SETTING: ")
    if setting == "q" or setting == "quit":
        sysPrint("Quitting application...")
        global appRunning
        appRunning = False
        return
    elif setting == "c" or setting == "cancel":
        sysPrint("Returned to main menu")
        return
    elif setting == "name":
        sysPrint("You are currently registered under the name " + username + ". What would you like this to change to?")
        username = getInput("NAME: ")
    elif setting == "roommates":
        sysPrint("You currently have " + numRoommates.__str__() + " roommates. What would you like this to change to?")
        num = validateNum(getInput("ROOMMATES: "))
        while num < 0:
            sysPrint("invalid input recieved. Please type in an integer value.")
            num = validateNum(getInput("ROOMMATES: "))
        numRoommates = num
    elif setting == "non-inclusive roommates":
        sysPrint("You currently have " + numUnavailable.__str__() + " roommates uncounted for on your next usage cycle. What would you like this to change to?")
        num = validateNum(getInput("NON-INCLUSIVE: "))
        while num < 0:
            sysPrint("invalid input recieved. Please type in an integer value.")
            num = validateNum(getInput("NON-INCLUSIVE: "))
        umUnavailable = num
    elif setting == "amount of bills":
        sysPrint("You currently have " + numBills.__str__() + " bills. What would you like this to change to?")
        num = validateNum(getInput("NUM-BILLS: "))
        while num < 0:
            sysPrint("invalid input recieved. Please type in an integer value.")
            num = validateNum(getInput("NUM-BILLS: "))
        numBills = num
    elif setting == "bills":
        sysPrint("Your current bills are listed below. What would you like to change these to?")
        for b in bills:
            print("\t\t" + b)
        bills = []
        for i in range(numBills):
            str = getInput("NAME OF BILL: ")
            bills.append(str)
    else:
        sysPrint("Invalid input. Please use one of the following: \n\t\t name - your name \n\t\t roommates - number of individuals to split the bill with \n\t\t non-inclusive roommates - number of individals who will not partake in current usage cycle \n\t\t amount of bills - number of bills to pay \n\t\t bills - the bills registered for payment")
        editSettings()
        return

    settings.append(username)
    settings.append(numRoommates)
    settings.append(numUnavailable)
    settings.append(numBills)
    for b in bills:
        settings.append(b)

    with open("settings.txt", 'r') as f:
        lines = f.readlines()
        c = 0
        for l in lines:
            if c > 9:
                settings.append(l[0:len(l) - 1])
            c += 1
    settings.append("billing records:")
    with open("settings.txt", 'w') as f:
        for s in settings:
            temp = s.__str__() + "\n"
            f.write(temp)
    sysPrint("Sucessfully edited settings! Would you like to continue editing settings? (y/n)")
    yOrN = getYorN()
    if yOrN == "y":
        sysPrint("You can edit your name, roommates, non-inclusive roommates, amount of bills, or your bills. Which would you like to edit?")
        editSettings()
        

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
while(appRunning):
    mainLoop()