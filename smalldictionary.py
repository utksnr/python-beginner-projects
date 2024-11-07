englishList = ["car"]
spanishList = ["coche"]

while True:
    print('''
        1) Add item to the dictionary
        2) Translate from English to Spanish
        3) Translate from Spanish to English
        4) Print the dictionary
        5) Delete an item
        6) Quit
    ''')

    choice = input("Choose an option:")

    if choice == "1":
        english = input("Enter the English word: ")
        spanish = input("Enter the Spanish word: ")
        englishList.append(english)
        spanishList.append(spanish)
        print("Word added.")

    elif choice == "2":
        english = input("English: ")
        if english in englishList:
            print("Spanish:", spanishList[englishList.index(english)])
        else:
            print("Word not found")

    elif choice == "3":
        spanish = input("Spanish: ")
        if spanish in spanishList:
            print("English:", englishList[spanishList.index(spanish)])
        else:
            print("Word not found")
    
    elif choice == "4":
        for i in range(len(englishList)):
            print("English:", englishList[i], "| Spanish:", spanishList[i])
    
    elif choice == "5":
        word = input("Enter word to remove: ")
        if word in englishList:
            index = englishList.index(word)
            englishList.pop(index)
            spanishList.pop(index)
            print("Word removed.")
        elif word in spanishList:
            index = spanishList.index(word)
            spanishList.pop(index)
            englishList.pop(index)
            print("Word removed.")
        else: 
            print("Word not found")

    elif choice == "6":
        print("Quitting, Goodbye.")
        break

    else:
        print("Invalid choice. Please choose a valid option.")
