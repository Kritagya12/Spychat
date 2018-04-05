from steganography.steganography import Steganography
from termcolor import colored
from datetime import datetime
from spy_details import spy,friends
from spy_details import Spy, ChatMessage, Spy_friend #Importing classes
import csv


print('Hello!')
print('Welcome to Spychat.\nLet\'s get started')


def load_friends():
    with open('friend.csv', 'rU') as friends_data:
        reader = list(csv.reader(friends_data, dialect='excel'))
        for row in reader[1:]:
            if row:
                Name = row[0]
                Age = (row[1])
                Rating = (row[2])
                spy = Spy(Name, Age, Rating)
                friends.append(spy)

#_______________________________________________________________________________________________________________________________________

def Chatload_friends():
    with open('Chats.csv', 'rU') as chats_data:
        reader = list(csv.reader(chats_data, dialect='excel'))
        for row in reader[1:]:
            if row:
                sender = row[0]
                message_sent_to= row[1]
                text = row[3]
                time = row[4]
                sent_by_me= row[4]
                chatlist = [sender,message_sent_to,text,time,sent_by_me]

#_______________________________________________________________________________________________________________________________________

# List of statuses
STATUS_MESSAGES=['Hello, there!!!!','Busy','Available']

# creating a friends list
load_friends()
Chatload_friends()

#________________________________________________________________________________________________________________________________________
                                                  # Function used to add friends #
#________________________________________________________________________________________________________________________________________
#START
def add_friend():
    new_friend = {
        'name': '',
        'salutation': "",
        'age': 0,
        'ratings': 0.0,
        'online': True,
        'chats': []

    }
    valid_name = True
    valid_salutation = True
    while valid_name:
        new_friend['name'] = raw_input("What is the name of friend ? ")
        if len(new_friend['name']) >= 3:
            while valid_salutation:
                new_friend['salutation'] = raw_input("Mr. or Ms.?")
                if len(new_friend['salutation']) >= 2:
                    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']
                    valid_name = False
                    valid_salutation = False
                else:
                    print 'Invalid salutaion'
        else:
            print "Please enter valid name"
    valid_age = True
    while valid_age:
        new_friend['age'] = raw_input("Age of friend")
        if len(new_friend['age']) > 0:
            valid_age = False
        else:
            print 'Invalid age'
    valid_rating = True
    while valid_rating:
        new_friend['rating'] = raw_input("Rating of  a friend")
        if len(new_friend['rating']) > 0:
            valid_rating = False
        else:
            print 'Invalid ratings'
        new_friend['online'] = True
        # conditon to add a friend
        if len(new_friend['name']) >= 3 and 55 >= int(new_friend['age']) >= 12 and new_friend['rating'] >= spy.rating:
            friends.append(new_friend['name'])
            with open('friend.csv', 'a') as friends_data:
                writer = csv.writer(friends_data)
                writer.writerow([new_friend['name'], new_friend['rating'], new_friend['age'], new_friend['online']])
        else:
            print "friend cannot be added "
    return len(friends)

#END
#_______________________________________________________________________________________________________________________________________
                                         # Function used to select one friend from the friend list #
#_______________________________________________________________________________________________________________________________________
#START
def select_a_friend():
  item_number = 0
  for friend in friends:
      print (str(item_number+1)+ " " + friend.name)
      item_number = item_number + 1
  friend_choice = int(raw_input("Choose from your friends"))
  friend_index = friend_choice - 1
  return friend_index

#END
#________________________________________________________________________________________________________________________________________
                                            # Function used for Sending message to a friend #
#________________________________________________________________________________________________________________________________________
#  START
def send_message():
    friend_choice=select_a_friend()
    original_image = raw_input("What is the name of the image?")
    output_path = 'output.jpg'
    text = raw_input("What do you want to say?")
    Steganography.encode(original_image, output_path, text)
    print "your secret message is ready! "
    new_chat = {
        "sender": spy.name,
        "message_sent_to": friends[friend_choice].name,
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }
    friends[friend_choice].chats.append(new_chat)
    with open('Chats.csv', 'a') as chats_data:
        writer = csv.writer(chats_data)
        writer.writerow([new_chat['sender'], new_chat['message_sent_to'], new_chat['message'], new_chat['time'],
                         new_chat['sent_by_me']])

#END
#________________________________________________________________________________________________________________________________________
                                                    # Function for reading a message #
#________________________________________________________________________________________________________________________________________
#START
def read_message():
    sender = select_a_friend()
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    new_chat = {
        "sender": spy.name,
        "message_sent_to": friends[sender].name,
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": True
    }
    friends[sender].chats.append(new_chat)
    print colored("The secret message send by your friend is "+secret_text,"red")


#END
#_________________________________________________________________________________________________________________________________________
                                                       # Function to read chats #
#_________________________________________________________________________________________________________________________________________
#START
def ReadChatload_friends(choice):
    name_friend = friends[choice].name
    with open('Chats.csv', 'rU') as chats_data:
        reader = list(csv.reader(chats_data, dialect='excel'))
        check = False
        for row in reader[1:]:
            if row:
                    if (row[1]==name_friend):
                        check =True
                        print  colored(row[2],"red")
                        print  colored(row[3],"blue")

#END
#__________________________________________________________________________________________________________________________________________
                                                    # Function for updating of status #
#__________________________________________________________________________________________________________________________________________
#  START
def add_status(current_status_message):
    if current_status_message != None:
      print ("Your current status message is " + current_status_message + "\n")
    else:
      print ('You don\'t have any status message currently \n')

    status = raw_input("Do you want to select from the older status (Y/N)? ")
    if len(status)>=1:
        if status.upper() == 'Y':
            item_position = 1
            for message in STATUS_MESSAGES:
                print(str(item_position) + ". " + message)
                item_position = item_position + 1
            message_selection = int(raw_input("\nChoose from the above messages "))
            if len(STATUS_MESSAGES) >= message_selection:
                new_status = STATUS_MESSAGES[message_selection - 1]
            else:
                print "Invalid Selection"
            return new_status

        elif status.upper() == "N":
            new_status = raw_input("What status message do you want to set?")
            if len(new_status) > 1:
                STATUS_MESSAGES.append(new_status)
            else:
                print("Please enter something")
            return(new_status)
        else:
            print("Invalid Entry")
    else:
        set_status="No status"
        return set_status


# END
#__________________________________________________________________________________________________________________________________________
                         # Function to show the menu to the user so that user can select a desired function #
#__________________________________________________________________________________________________________________________________________
# START
def start_chat(spy_name, spy_age, spy_rating):
    current_status_message = None
    show_menu = True

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
            print "select a friend whom you want to see the chat"
            choice = select_a_friend()
            ReadChatload_friends(choice)

        elif menu_choice == 6:
            show_menu = False
            print("You have successfully logged out")

#END
#_______________________________________________________________________________________________________________________

user=raw_input("Do you want to continue as  " + spy.name + " (Y/N)?") #Default user

if (user.upper()=="Y"):
        print("Welcome, %s with %d years of age and %f rating." %(spy.name,spy.age,spy.rating))
        start_chat(spy.name, spy.age, spy.rating)

#_______________________________________________________________________________________________________________________

elif(user.upper()=="N"):

    spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")  # spy creating his own user
    if len(spy.name) >= 3:
        print('Welcome ' + spy.name + '.Glad to have u back with us')
        spy.salutation = raw_input("What should we call you Mr. or Ms.?")
        if len(spy.salutation)>0:
            spy.name=spy.salutation + " " + spy.name
            print "Alright " + spy.name + ", I'd like to know more about you.."
            spy.age = int(raw_input("What is your age? "))
            if spy.age > 12 and spy.age < 50:
                print "You are eligible to be a spy"
            else:
                print "You are not eligible for spy"
            spy.rating = float(raw_input("What is your spy rating "))
            if (spy.rating) > 4.5:
                print 'You are an Expert spy'
            elif (spy.rating) > 3.5 and (spy.rating) <= 4.5:
                print('You are one of the good ones')
            elif (spy.rating) >= 2.5 and (spy.rating) <= 3.5:
                print('You can always do better')
            else:
                print('Wrong entry')
            print "Welcome to spychat %s Age: %d with rating is %.2f " % (spy.name, spy.age, spy.rating)
        else:
            print "not valid"
    else:
        print "enter a 3 character name"
else:
    print "invalid"

start_chat(spy.name, spy.age, spy.rating)