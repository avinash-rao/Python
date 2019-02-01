# take input from user
thoughts = []
choice = 'y'
print("Write your thoughts here:")
while choice == 'y':
    thought = input("\n\n~ ")
    thoughts.append(thought)
    choice = input("Would you like to enter more thoughts? (y/n)")

# append the user input to file
with open("thoughts.txt", mode='a', encoding='utf-8') as f:
    for thought in thoughts:
        f.write(thought + "\n\n")

