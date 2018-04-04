from steganography.steganography import Steganography
from datetime import datetime
from spy_details import spy
from spy_details import friends
from spy_details import Spy,friends, Chat #Importong classes

# List of statuses
STATUS_MESSAGES=['Hello, there!!!!','Busy','Available']

#-----------------------------------------------------------------------------------------------------------------------
#START Function used to add friends
def add_friend():
    new_friend = Spy(" ", " ", 0, 0.0)

    # ask user for name
    new_friend.name = raw_input("Please add your friend's name: ")

    # validation of user name.
    if len(new_friend.name) > 0:
        if len(new_friend.name) > 20:
            print("Your name length is big.")
    else:
        print("Name should be not empty or length is less then 20 char.")
        return add_friend()

    new_friend.salutation = raw_input("What to call Mr. or Ms.?: ")

    # user salutation validation
    if len(new_friend.salutation) > 0:
        if len(new_friend.salutation) > 5:
            print("Your salutation is too big.")
    else:
        print("Salutation empty or check length")
        return add_friend()

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = int(raw_input("Age: "))

    if 12 < new_friend.age < 50:
        True
    else:
        print("Age should be in between 12 to 50")
        return add_friend()

    # ask for rating of friend, using float
    new_friend.rating = float(raw_input("Spy rating? "))

    if new_friend.rating > 0.0:
        True
    else:
        print("Rating should be more than 0.0")
        return add_friend()

    friends.append(new_friend)
    print('Friend Added!')

    #Total number of friends in the list
    return len(friends)

#END Function used to add friends
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
#START Function used to select one friend from the friend list
def select_a_friend():
  item_number = 0
  for friend in friends:
      print ('%d. %s age:%s with rating %f is online' % (item_number+1, friend.name,friend.age,friend.rating))
      item_number = item_number + 1
  friend_choice = int(raw_input("Choose from your friends"))
  friend_choice_position = friend_choice - 1
  return friend_choice_position

#END Function used to select one friend from the friend list
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
# START Function used for Sending message to a friend
def send_message():
    friend_choice=select_a_friend()
    original_image = raw_input("What is the name of the image?")
    output_path = 'output.jpg'
    text = raw_input("What do you want to say?")
    Steganography.encode(original_image, output_path, text)
    new_chat = {"Message": text, "Time": datetime.now(), "Sent by me": True}
    friends[friend_choice].chats.append(new_chat)
    print "Your secret message is ready. \n"

# END Function used for Sending message to a friend
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
#START Function for reading a message
def read_message():
    sender = select_a_friend()
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    present_time = datetime.now()
    print "Your secret message is ready:\n"
    print secret_text, "\n"
    new_chat = {"Message": secret_text, "Time":datetime.now() , "Sent by me": False}
    friends[sender].chats.append(new_chat)
    print("Your secret message is "+secret_text)

#END Function for reading a message
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
# START Function use for updation of status
def add_status(current_status_message):
    if current_status_message != None:
      print ("Your current status message is " + current_status_message + "\n")
    else:
      print ('You don\'t have any status message currently \n')

    default = raw_input("Do you want to select from the older status (y/n)? ")
    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set?")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message)
    elif default.upper() == 'Y':
        item_position = 1
        for message in STATUS_MESSAGES:
            print(str(item_position) + ". " + message)
            item_position = item_position + 1
        message_selection = int(raw_input("\nChoose from the above messages "))
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]
    return updated_status_message

# END Function use for updating the status
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
#START Function to show the menu to the user so that user can select a desired function
def start_chat():
  show_menu = True
  current_status_message=None
  while show_menu==True:
      menu_choices = ("What do you want to do? \n1. Add a status update \n2. Add a friend \n3. Send a secret message \n4. Read a secret message \n5. Read chats from a 'User' \n6. Close Application \n")
      menu_choice = int(raw_input(menu_choices))


      if menu_choice == 1:
          print ('You chose to update the status')
          current_status_message = add_status(current_status_message)

      elif menu_choice == 2:
          number_of_friend = add_friend()
          print("You have %d friends"%(number_of_friend))

      elif menu_choice == 3:
          send_message()

      elif menu_choice == 4:
          read_message()

      elif menu_choice == 5:
          print("reading chat from user")

      elif menu_choice == 6:
          show_menu = False
          print("Quitting")

#END Function to show the menu to the user so that user can select a desired function
#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------
#START Function consists details of spy
def enter():
    spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")# spy creating his own user
    if len(spy_name) > 0:
        print('Welcome '+ spy_name+'.Glad to have u back with us')
        spy_salutation = raw_input("What should we call you (Mr. or Ms.)?")  # Another variable to store the salutation.
        spy_salutation + " " + spy_name  # We are joining the two strings together.
        spy_name = spy_salutation + " " + spy_name  # Variable re-assignment
        print(spy_name)
        print('Alright ' + spy_name + '. I\'d like to know a little bit more about you.')
    else:
        print('A spy needs to have a valid name.Try again please.')
    #Other spy details
    spy_age = 0 #initializing age with 0    #Details
    spy_rating = 0.0 #initializing rating with 0
    spy_is_online = False
    spy_age = int(raw_input("What is your age?"))          # Asking spy age
    if spy_age > 12 and spy_age < 50:
        spy_rating = float(raw_input("What is your spy rating?"))
    else:
        print('Sorry you are not of the correct age to be a spy')

    spy_rating = float(raw_input("What is your spy rating?"))
    if spy_rating > 4.5:
        print('Great ace!')
    elif spy_rating > 3.5 and spy_rating <= 4.5:
        print('You are one of the good ones.')
    elif spy_rating >= 2.5 and spy_rating <= 3.5:
        print('You can always do better')
    else:
        print('We can always use somebody to help in the office.')
    print("Welcome to spychat %s %s Age: %d Your rating:%f" % (spy_salutation, spy_name, spy_age, spy_rating))


# END Function consists details of spy##############
#-----------------------------------------------------------------------------------------------------------------------

print('Hello!') #print is a function in python to print whatever comes after it to the screen.
print('Let\'s get started')
user=raw_input("Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)?") #Default user
new_user=0
if user=="Y":
        print("Welcome, %s %s with %d years of age and %f rating.Welcome to spychat" %(spy.salutation,spy.name,spy.age,spy.rating))
else:
    new_user = 1
    enter()

start_chat()
