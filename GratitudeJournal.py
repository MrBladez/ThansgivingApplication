"""
This program gets entries for a gratitude journal from a user and stores the entries for later viewing
"""

print("This program takes journal entries entered by a user and stores them and allows the user to look at previous entries")
print("GratitudeJournal v1.56 by Austin Minute")
EntryNumber = 0
entryList = []
entry = ""
file = open("Journal.txt")
while True:
    # This gets input from the user on what he would like to do
    userChoice = input("Would you like to enter or view a journal entry or exit? ")
    while userChoice != "enter" and userChoice != "view" and userChoice != "exit" and userChoice != "Enter" and userChoice != "View" and userChoice != "Exit":
        print("Wrong entry, please enter something again in the following prompt")
        userChoice = input("Do you want to enter,view or exit? ")
    if userChoice == "enter" or userChoice == "Enter":
        if input("Would you like to go back from enter? (yes/no) ") == "yes":
            continue
        # This gets an entry from the user for the journal and enters it into the journal and enters a break between each entry
        userEntry = input("What would you like to enter? ")
        print(userEntry, file=open('Journal.txt', 'a'))
        print("EndOfEntry", file=open('Journal.txt', 'a'))
    elif userChoice == "view" or userChoice == "View":
        # this loops through the lines in the journal
        for line in file:
            wordList = line.split()
            for item in wordList:
                # when the loop comes across the word 'EndOfEntry' it adds all the words before EndOfEntry to the entryList
                if item == "EndOfEntry":
                    EntryNumber += 1
                    if entry != "":
                        entryList.append(entry)
                    entry = ""
                else:
                    entry += item + " "
        while True:
            # This allows the user to view any entry in the journal and also checks for the user entering the wrong thing.
            if input("Would you like to go back from viewing? (yes/no) ") == "yes":
                break
            whichToView = int(input("What entry would you like to see? (" + str(EntryNumber) + " possible entries) "))
            if whichToView <= EntryNumber and whichToView > 0:
                print("This is entry number " + str(whichToView) + " : " + entryList[whichToView-1])
            else:
                print("That numbered entry does not exist at the moment.")
    elif userChoice == "Exit" or userChoice == "exit":
        break


