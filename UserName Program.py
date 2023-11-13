##########
#this program will ask the user for their name and greet them using that name

# userName is expected to be a string
userName = input("What is your name: ")
# Error in case user does not enter anything
while userName == "" :
    print("Error! Blank string inputted!")
    userName = input("What is your name: ")
if len(userName) == 1 :
    userNameLengthChoice = input("Are you sure your name is only 1 character? \nType 'y' for yes, and 'n' if you want to type in a different name: ")
    while (userNameLengthChoice != "y") and (userNameLengthChoice != "n"):
        print("Error! The user inputted something other then 'y' or 'n'")
        userNameLengthChoice = input("Are you sure your name is only 1 character? \nType 'y' for yes, and 'n' if you want to type in a different name: ")
    if userNameLengthChoice == "n" :
        userName = input("What is your name: ")
    # Error in case user does not enter anything
    while userName == "" :
        print("Error! Blank string inputted!")
        userName = input("What is your name: ")
print("Hello " + userName + ", I hope your having a great day today!")
    

      

