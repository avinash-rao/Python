dict = {}
while True:
    print("----------Birthday App-----------")
    print("1. Show Birthday")
    print("2. Add a Birthday")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(dict.keys()) == 0:
            print("Nothing to show")
        else:
            name = input("Enter name to look for birthday: ").lower()
            birthday = dict.get(name, "No data found")
            print(birthday)
    elif choice == 2:
        name = input("Enter friend's name: ").lower()
        date = input("Birthdate: ")
        dict[name] = date
        print("Birthday added")
    elif choice == 3:
        break
    else:
        print("Enter a valid choice")
