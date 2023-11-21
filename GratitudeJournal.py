print("This program takes journal entries entered by a user and stores them and allows the user to look at previous entries")
print("GratitudeJournal v1.00 by Austin Minute")
EntryNumber = 0
entryList = []
entry = ""
file = open("Journal.txt")
while True:
    userChoice = input("Would you like to enter or view a journal entry or exit? ")
    if userChoice == "enter" or userChoice == "Enter":
        if input("Would you like to go back? (yes/no) ") == "yes":
            continue
        userEntry = input("What would you like to enter? ")
        print(userEntry, file=open('Journal.txt', 'a'))
        print("EndOfEntry", file=open('Journal.txt', 'a'))
    elif userChoice == "view" or userChoice == "View":
        for line in file:
            wordList = line.split()
            for item in wordList:
                if item == "EndOfEntry":
                    EntryNumber += 1
                    if entry != "":
                        entryList.append(entry)
                    entry = ""
                else:
                    entry += item + " "
        while True:
            if input("Would you like to go back? (yes/no) ") == "yes":
                break
            whichToView = int(input("What entry would you like to see? (" + str(EntryNumber) + " possible entries) "))
            if whichToView <= EntryNumber and whichToView > 0:
                print("This is entry number " + str(whichToView) + " : " + entryList[whichToView-1])
            else:
                print("That numbered entry does not exist at the moment.")
    elif userChoice == "Exit" or userChoice == "exit":
        break


