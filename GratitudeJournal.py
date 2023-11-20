print("This program takes journal entries entered by a user and stores them and allows the user to look at previous entries")
print("GratitudeJournal v1.00 by Austin Minute")
EntryNumber = 0
entryList = []
entry = ""
file = open("Journal.txt")
while True:
    userChoice = input("Would you like to enter or view a journal entry or exit? ")
    if userChoice == "enter" or userChoice == "Enter":
        userEntry = input("What would you like to enter? ")
        print("Entry", file=open('Journal.txt', 'a'))
        print(userEntry, file=open('Journal.txt', 'a'))
    elif userChoice == "view" or userChoice == "View":
        for line in file:
            wordList = line.split()
            for item in wordList:
                if item == "Entry":
                    EntryNumber += 1
                else:
                    entry += item + " "
        whichToView = int(input("What entry would you like to see? " + str(EntryNumber) + " possible entries"))
        print(entryList[whichToView])
    elif userChoice == "Exit" or userChoice == "exit":
        break


