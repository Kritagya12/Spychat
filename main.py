from steganography.steganography import Steganography
from datetime import datetime
from spy_details import spy_name,spy_salutation,spy_age,spy_rating

print('Hello!') #print is a function in python to print whatever comes after it to the screen.
print('Let\'s get started')

############About spy##############
def enter():
    spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")# spy creating his own user
    if len(spy_name) > 0:
        print('Welcome'+ spy_name+'.Glad to have u back with us')
        spy_salutation = raw_input("What should we call you (Mr. or Ms.)?")  # Another variable to store the salutation.
        spy_salutation + " " + spy_name  # We are joining the two strings together.
        spy_name = spy_salutation + " " + spy_name  # Variable re-assignment
        print(spy_name)
        print('Alright ' + spy_name + '. I\'d like to know a little bit more about you.')
    else:
        print('A spy needs to have a valid name.Try again please.')

#########Other spy details##############
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

 ###########Starting of spychat#############
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

      elif menu_choice == 6:
          show_menu = False
          print("Quitting")

#########Updation of status###########
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

STATUS_MESSAGES=['Hello, there!!!!','Busy','Available'] #List of statuses

###########################Addition of a new spy friend###################
def add_friend():
    friend={}
    new_name = raw_input("Please add your friend's name:")
    new_salutation = raw_input("Are they Mr. or Ms.?: ")
    friend["age"] = int(raw_input("What's the friend's age?"))
    friend["rating"] = float(raw_input("Enter the friend's rating."))
    friend["name"] = new_salutation + "." + new_name
    friend["chats"] = []
    if len(friend["name"]) > 0 and 12 < friend["age"] < 50:
        Friend_name.append(friend)  # Add Friend
        #Friend_age.append(new_age)
        #Friend_rating.append(new_rating)
        #Friend_status.append(True)
    else:
        print('Sorry! Invalid entry. We can\'t add spy with the details you provided')
    return len(Friend_name)

###########################Friend selection###############################
def select_a_friend():
  item_number = 0
  for friend_name in Friend_name:
      print ('%d. %s' % (item_number + 1, friend_name['name']))
      item_number = item_number + 1
  friend_choice = int(raw_input("Choose from your friends"))
  friend_choice_position = friend_choice - 1

  return friend_choice_position

#######################Sending a message to a friend#######################
def send_message():
    friend_choice=select_a_friend()
    original_image = raw_input("What is the name of the image?")
    output_path = 'output4.jpg'
    text = raw_input("What do you want to say?")
    Steganography.encode(original_image, output_path, text)
    new_chat = {"Message": text, "Time": datetime.now(), "Sent by me": True}
    Friend_name[friend_choice]["chats"]=new_chat
    print "Your secret message is ready. \n"

#############################Reading a message#############################
def read_message():
    sender = select_a_friend()
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    present_time = datetime.now()
    print "Your secret message is ready:\n"
    print secret_text, "\n"
    new_chat = {"Message": secret_text, "Time": present_time, "Sent by me": False}
    Friend_name[sender]['chats']=new_chat

user=raw_input("Do you want to continue to Mr.Bond?(Y/N)") #Default user
new_user=0
if user=="Y":
    from spy_details import spy_name
    from spy_details import spy_salutation
    from spy_details import spy_age
    from spy_details import spy_rating
    print("Welcome, %s %s with %d years of age and %f rating.Welcome to spychat" %(spy_salutation,spy_name,spy_age,spy_rating))
else:
    new_user = 1
    enter()

Friend_name=[]
Friend_age=[]
Friend_rating=[]
Friend_status=[]
start_chat()









