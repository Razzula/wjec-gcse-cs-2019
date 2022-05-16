#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Setup

import os #Library used to specify search directory for searching, SEE LINES 159 AND 183, as well as clearing the console, SEE LINE 387. Imported globally as it is used in multiple functions.
import hashlib #Library used to encrypt passwords, SEE LINES 32 AND 341. Imported globally as it is used in multiple functions.
import getpass #Library used to hide input, used to hide passwords, SEE LINES 24, 307, 312, 313 AND 320. Imported globally as it is used in multiple functions.

salt="4bc30abe44af481894d14eef620a2aee" #Used for LINE 32 AND 341. Declared globally as used in both the authentication() and addUser() functions. Just an alphanumeric randomly generated.

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def authentication(): #Makes sure only people who are meant to access the system can, by making them use a username and password

    global username #Allows addUser() to access username for verification, SEE LINE 329

    breaker()

    #User Inputs Details
    username=input("User: ")
    while (username == ""): #PRESENCE CHECK, this loop will clear the console to make it seem like the input has been ignored
        cls()
        print("Username cannot be blank")
        breaker()
        username=input("User: ")
    password=getpass.getpass()
    while (password==""): #PRESENCE CHECK
        cls()
        print("Password cannot be blank")
        breaker()
        print("User: "+username)
        password=input("Password: ")
    username=username.upper()
    password=hashlib.sha512((password+salt).encode('utf-8')).hexdigest() #Encrypts the user's input in the same way the passwords are encrypted, so that the comparison will work (SEE LINE 44)

    cls()

    #Check if users inputs are correct
    try: #Will attempt to open and read from the file "user.txt". If the file cannot be found, rather than display an error message, the except branch will be called
        f=open("logins/"+username+".txt", "r")
        pwd=f.read() #Searches for the entered password, in a file, under the name of the entered username
        f.close()
    except: #(Invalid Username)
        print("Invalid Username or Password")
        authentication() #RECURSION as LOOP, prevents user from advancing without correct logins
    if (password!=pwd): #(Invalid Password)
        print("Invalid Username or Password")
        authentication() #RECURSION as LOOP
    print("Valid User")
    menu() #BREAKS RECURSION, allowing user to continue

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def menu(): #Allows the user to choose what function they want to call

    #Displays GUI
    breaker()
    print("A) Search for a text \nB) Add a new text \nC) Add a new user \nD) Exit \n")
    print("What would you like to do?")
    choice=input("")
    choice=choice.upper() #Capitalises the input, so that the case the user uses doesn't matter, making it easier for user to input

    #Enforces the user's choice
    if (choice=="A"):
        cls()
        print("Search")
        searchMenu()

    elif (choice=="B"):
        breaker()
        print("Are you sure you would like to add a new text to the system? (Y/N)")
        verify() #Verfies this isn't an accident, to prevent texts being made by accident
        cls()
        print("Add Text")
        addText()

    elif (choice=="C"):
        breaker()
        print("Are you sure you would like to add a new user to the system? (Y/N)")
        verify() #Verfies this isn't an accident, to prevent accounts being made by accident
        cls()
        print("Add User")
        addUser()
    elif (choice=="D"):
        exit() #Terminates program
    else:
        cls()
        print("Command not recognised. Please try again with 'A', 'B', 'C' or 'D'.")
        menu() #RECURSION used as LOOP

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def searchMenu(): #Allows user to chose their search method

    #Displays GUI
    breaker()
    print("A) Name \nB) Keywords \nC) Reading Age \nD) Display All Texts \n")
    print("How would you like to search?")
    choice=input("")
    choice=choice.upper() #Capitalises the input, so that the case the user uses doesn't matter, making it easier for them to input

    #Enforces the user's choice
    if (choice=="A"):
        breaker()
        print("Search for a file by name")
        search()
        
    elif (choice=="B"):
        search_type="KEYWORD:" #Sets search_type so that in the searchData() function it will only search for keywords (SEE LINE 163)
        searchData(choice, search_type)

    elif (choice=="C"):
        search_type="AGE:" #Sets search_type to only search for age
        searchData(choice, search_type)

    elif (choice=="D"):
        searchAll()
        
    else:
         cls()
         print("Command not recognised. Please try again with 'A', 'B', 'C' or 'D'.")
         searchMenu() #RECURSION used as LOOP

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def search(): #Searches for a file by name
    
    search=input("File Name: ")
    search=search.upper() #Capitalises to remove case sensitivity

    cls()

    #Searches for the file (search.txt) and displays it
    try:
        f=open("texts/"+search+".txt", "r")
        data=f.readlines() #Saves text as array, each line is a different item in the array
        f.close()
        print(search.title())
        print(data[0])
    except:
        print("No Results Found")
    menu()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def searchData(choice, search_type): #Search for files that contain either the keyword or age, and display their names to the user
   
    breaker()

    searchfor=input("Search for "+search_type.title()+" ")
    while (searchfor==""):
        cls()
        print("Search")
        breaker()
        print("A) Name \nB) Keywords \nC) Reading Age \nD) Display All Texts \n\nHow would you like to search? \n"+choice)
        breaker()
        print("Search cannot be blank.")
        breaker()
        searchfor=input("Search: ")
    searchfor=searchfor.upper()
    found=False #Used on LINE 167
    print("")

    #Searches every file in the set directory if it contains the keyword/age
    for file in os.listdir("./texts"): #Repeats process for every file in the directory, OS is used to specify directory
        if file.endswith(".txt"): #Only continues if the file in question is a .txt
            f=open("texts/"+file)
            text=f.read()
            if (search_type+searchfor in text): #Checks if file contains "KEYWORD:keyword" or "AGE:age"
                print("Text Found: "+file.title())
                found=True

    if (found==True):
        print("")

        breaker()
        search() #Allows the user to then search for the file they want (the names of the valid files are hsown to help the user)
    else:
        cls()
        print("No Results Found")
        searchMenu()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def searchAll(): #Displays all of the texts stored by the program

    cls()
    
    #Searches and prtints every file in the system. SEE searchData().
    for file in os.listdir("./texts"): #LOOPS for every file
        if file.endswith(".txt"): #Ignores non .txt files
            f=open("texts/"+file)
            text=f.readlines()
            print(file.title()+":") #Prints Title of text
            print(text[0]) #Prints the text itself
    menu()
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
def addText(): #Allows the user to add a new entry into the system

    import math #Library used for math.ceil(), to round upwards, SEE LINE 226. Imported locally as it is onlt used in this function.
    breaker()
    
    #Sets Arrays to blank
    keywords=[]
    data=[]

    #Input
    title=input("Name of Text: ")
    keywords.append("KEYWORD:"+title.upper()) #Adds title as a keyword (so that if 0 keywords are enetered there will still be one)
    print("")
    print("Please enter the text itself")
    print("WARNING: Make sure that it is correct, with no mistakes such as typos, missing capital letters or full stops, as this WILL effect the reading age.")
    print("")
    text=input("Text: ")

    #Counts Words, Sentences and Characters, and calculates ARI
    words=int(text.count(" ")+1) #Amount of spaces +1, as every word has a space before it, bar the first word
    sentences=int(text.count(".") + text.count("!") + text.count("?")) #Amount of full stops, exclamation marks and question marks, as every sentence ends in one of them

    if (words<100): #CHECK
        breaker()
        print("Error: Text must be over 100 words for ARI to equation to function. Please Try again.")
        addText()
        #This is true, I researched the ARI formula and the text must be over 100 words in order to function.

    while (words==0 or sentences==0): #PRESENCE CHECK, as if words is equal to 0, the ARI calculation would fail. (Cannot divide by 0).
        breaker()
        print("Error: No words, or sentences, have been detected. Please try again.")
        addText()

    characters=int(len(text)-text.count(" ")-sentences-text.count(",")-text.count("-")-text.count("(")-text.count(")")-text.count("'")-text.count("&")) #Length of text, minus the spaces and punctuation 
    age=4.71*(characters/words)+0.5*(words/sentences)-21.43
    
    if (age<0): #CHECKS if age is a negative value
        print("ERROR: Cannot calculate reading age, as it is too low. Please try again.")
        menu()
    age=math.ceil(age)

    print("")

    #More Input
    loop=True
    while (loop==True):
        try: #Test if input is an integer, as requried
            est_age=int(input("Estimated Reading Age: "))
            while (est_age<5 or est_age>18): #RANGE CHECK to make sure no values are too high OR low
                breaker()
                print("Invalid Age. The range is 5 to 18. Please try again.")
                breaker()
                est_age=int(input("Estimated Reading Age: "))
            loop=False
        except:
            breaker()
            print("Value must be a number.")
            breaker()
    print("Actual Reading Age: %d" %age)
    print("")

    #Sets Keywords and Age ready to be stored
    print("Keywords will make this text easier to find.")
    print("")
    while (loop==False): #Same process as on SEE 234, but inverted, meaning that the same variable can be used
        try:
            keywords_value=int(input("Number of Keywords: ")) #TYPE CHECK, to ensure a number is entered
            while (keywords_value<0 or keywords_value>10):
                breaker()
                print("Invalid Value. The range is 0 to 10. Please try again.")
                breaker()
                keywords_value=int(input("Number of Keywords: ")) #TYPE CHECK, to ensure a number is entered
            loop=True
        except:
            breaker()
            print("Invalid value. The number of keywords must be a number.")
            breaker()
    count=0
    while (count!=keywords_value): #LOOP, adds keywords into the array (this method means one variable can be used, rather than having keyword1, keyword2, keyword 3, etc)
        count=count+1
        keyword=input("Keyword %d: " % count)
        keyword=keyword.upper()
        keywords.append("KEYWORD:"+keyword)
    while (count!=10): #Adds a blank entry to the remaining spaces in the array, otherwise LINE 282 would crash
        count=count+1
        keywords.append(" ")
    age=str("AGE:%d" %age)

    #Stores data
    f=open("texts/"+title.upper()+".txt", "w+")
    f.write(text+"\n"+age+"\n"+keywords[0]+"\n"+keywords[1]+"\n"+keywords[2]+"\n"+keywords[3]+"\n"+keywords[4]+"\n"+keywords[5]+"\n"+keywords[6]+"\n"+keywords[7]+"\n"+keywords[8]+"\n"+keywords[9]+"\n"+keywords[10]) #Stores the text, age and keywords into a file named after the title
    f.close()
    cls()
    print("Text Stored Successfully")
    menu()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def addUser(): #Allows the user to add a new user to the system, that can be used in the authentication process.

    breaker()

    global salt
    
    #Input
    print("Please enter the new users login details: (Passwords will be hidden) \nIf you would like to change your password, just use your current username instead of a new one.\n")

    new_username=input("User: ")
    while (new_username==""): #PRESENCE CHECK
        cls()
        print("Add User")
        breaker()
        print("Please enter the new users login details: (Passwords will be hidden) \nIf you would like to change your password, just use your current username instead of a new one. \n")
        new_username=input("User: ")
    
    new_password1=getpass.getpass()
    while (new_password1==""): #PRESENCE CHECK
        cls()
        print("Add User")
        breaker()
        print("Please enter the new users login details: (Passwords will be hidden) \nIf you would like to change your password, just use your current username instead of a new one. \n\nUser: "+new_username)
        new_password1=getpass.getpass()
        
    new_password2=getpass.getpass()
    while (new_password2==""): #PRESENCE CHECK
        cls()
        print("Add User")
        breaker()
        print("Please enter the new users login details: (Passwords will be hidden) \nIf you would like to change your password, just use your current username instead of a new one. \n\nUser: "+new_username+"\nPassword: ")
        new_password2=getpass.getpass()
        
    new_username=new_username.upper()
    breaker()

    #Checks user doesn't already exist, and if it does, that the user (or admin) is signed in
    try:
        f=open("logins/"+new_username+".txt", "r")
        f.read()
        if (username!=new_username and username!="ADMIN"): #If user is not authenticated, will be booted to menu
            cls()
            if (new_username=="ADMIN"): #This if statement exists to prevent the output on LINE 334 from being "... ADMIN or ADMIN"
                print("User Already Exists: To change their password, you mudt be signed in as ADMIN")
            else:
                print("User Already Exists: To change their password, you mudt be signed in as ADMIN or "+new_username) #Adds the username of account in question
            menu()
            exit() #Sometimes after exiting in the menu, the program would continue here. This terminates it.
    except:
        print("")

    #Stores Data
    if (new_password1==new_password2): #CHECK to verify that the correct data has been submitted
        
        password=hashlib.sha512((new_password1+salt).encode('utf-8')).hexdigest() #Encodes password using a hash system, as well as adding salt to mak eit harder to decrypt

        cls()
        
        f=open("logins/"+new_username+".txt", "w+")
        f.write(password) #Stores details in logins folder
        #CHEKCS that data has been stored successfully
        f=open("logins/"+new_username+".txt", "r")
        if (f.read()==password): #Compares files's password with user's input
            print("User Added Successfully")
        else:
            cls()
            print("ERROR: Unable to create new login. Please see an administrator for help.")
        f.close()
        menu()
    else:
        breaker()
        cls()
        print("Passwords do not match, please try again...")
        addUser()#RECURSION used as LOOP
         
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def verify(): #Verifies that the user is proceeding on purpose
    
    choice=input("")
    choice=choice.upper() #Capitalises the input, so that the case the user uses doesn't matter, making it easier for them to input
    if (choice=="N"):
        cls()
        print("Cancelled...")
        menu()
    elif choice=="Y":
        breaker()
    else:
        breaker()
        print("Command not recognised. Please try again with 'Y' or 'N'")
        verify() #RECURSION used as LOOP (forces user to either go to menu or continue)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def breaker(): #Genereates a breaker to seperate the outputs
    
    print("="*119) #119 will fit cmd terminal perfectly, if in font size 16

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def cls(): #Clears the console
    
    os.system('cls') #Uses OS library
    breaker()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Main

breaker()
print("Login (Password will be hidden)")

authentication() #Calls the authentication function, starting the program

exit() #Terminates the program, shouldn't be used unless the program breaks, and it is no longer contained within the functions, as it should be

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
