print('Hello!') #print is a  function in python to print whatever comes after it to the screen.
print('Let\'s get started')

############About spy##############
def enter():
    spy_name = input("Welcome to spy chat, you must tell me your spy name first: ")  # spy creating his own user
    if len(spy_name) > 0:
        print('Welcome'+ spy_name+'.Glad to have u back with us')
        spy_salutation = input("What should we call you (Mr. or Ms.)?")  # Another variable to store the salutation.
        spy_salutation + " " + spy_name  # We are joining the two strings together.
        spy_name = spy_salutation + " " + spy_name  # Variable re-assignment
        print(spy_name)
        print('Alright ' + spy_name + '. I\'d like to know a little bit more about you.')
    else:
        print('A spy needs to have a valid name.Try again please.')

#########Other spy details##############
    spy_age = 0#initializing age with 0    #Details
    spy_rating = 0.0#initializing rating with 0
    spy_is_online = False
    spy_age = int(input("What is your age?"))          # Asking spy age
    if spy_age > 12 and spy_age < 50:
        spy_rating = int(input("What is your spy rating?"))
    else:
        print('Sorry you are not of the correct age to be a spy')

    spy_rating = float(input("What is your spy rating?"))
    if spy_rating > 4.5:
        print('Great ace!')
    elif spy_rating > 3.5 and spy_rating <= 4.5:
        print('You are one of the good ones.')
    elif spy_rating >= 2.5 and spy_rating <= 3.5:
        print('You can always do better')
    else:
        print('We can always use somebody to help in the office.')
    print("Welcome to spychat %s %s Age: %d Your rating:%f" % (spy_salutation, spy_name, spy_age, spy_rating))

 ###########Starting of spychat#############
def start_chat(): #start_chat is a function
    show_menu = True
    current_status_message=None
    while show_menu:
        menu_choices = "What do you want to do? \n 1. Add a status update\n 2. Add a friend\n 3. Exit the application \nInput:-"
        menu_choice = input(menu_choices)
        if (menu_choice == '1'):
            current_status_message=add_status(current_status_message) #Add Status Update
        elif(menu_choice=='2'):
            no=add_friend() #No of friends returned
            print("No. of friends are %d" %no)
        elif( menu_choice=='3'):
            print("Quitting") #Exit from  spychat
            show_menu =  False
        else:
            print("Invalid input.")
            pass

#########Updation of status###########
def add_status(current_status_message):
    if current_status_message is not None:
        print("Your current status is: %s" % current_status_message )
    else:
        print("You don't have any status right now")
    default=input("Do you want to select from the previous statement(Y?N)")
    if default.upper()=='N':
        new_status_message=input("Which status you want to set?")
        if len(new_status_message)>0:
            updated_status_message=new_status_message #Staus updated
            STATUS_MESSAGE.append(updated_status_message) #Adding more to the list of statuses
        else:
            print("Please enter a valid status...") #Status invalid
            updated_status_message=current_status_message  #Assignment of previous status
    elif default.upper()=='Y':
        item_position=1
        for message in STATUS_MESSAGE:
            print("%d.%s"%(item_position,message))
            item_position=item_position+1
        menu_selection=int(input("What is your desired status?"))
        if len(STATUS_MESSAGE)>=menu_selection:
            updated_status_message=STATUS_MESSAGE[menu_selection-1] #Setting desired status
        else:
            print("Invalid  input")
            updated_status_message=current_status_message
    else:
        print("Invalid input")
        pass
    return updated_status_message

############Addition of a new spy friend###############
def add_friend():
    new_name = input("Please add your friend's name:")
    new_salutation = input("Are they Mr. or Ms.?: ")
    new_name = new_salutation + " " + new_name
    new_age = int(input("Age?"))
    new_rating = float(input("Spy rating?"))
    if len(new_name) > 0 and 12 < new_age < 50:
        Friend_name.append(new_name)# Add Friend
        Friend_age.append(new_age)
        Friend_rating.append(new_rating)
        Friend_status.append(True)
    else:
        print('Sorry! Invalid entry. We can\'t add spy with the details you provided')
    return len(Friend_name)

user=input("Do you want to continue with the  default user?(Y/N)")
new_user=0
if user=="Y":
    from spy_details import spy_name
    from spy_details import spy_salutation
    from spy_details import spy_age
    from spy_details import spy_rating
    print("Welcome, %s %s with %d years of age and %d rating.Welcome to spychat" %(spy_salutation,spy_name,spy_age,spy_rating))
else:
    new_user = 1
    enter()
STATUS_MESSAGE=['You are in','How are you?','Let\'s move further']
Friend_name=[]
Friend_age=[]
Friend_rating=[]
Friend_status=[]
start_chat()





