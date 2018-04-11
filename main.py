#_______________________________________________________________________________________________________________________
                                                  #  Spy chat  #
#_______________________________________________________________________________________________________________________

from spy_details import Spy, ChatMessage #Importing classes
from spy_details import spy1,friends,chats #Importing lists
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored
import csv

print('Hello!')
print('Welcome to Spychat.\nLet\'s get started')


#_______________________________________________________________________________________________________________________

# list of default status
STATUS_MESSAGES = ['Hey everyone!', 'My name is Kritagya', 'Available']

#_______________________________________________________________________________________________________________________
                                             # Function used to add friends #
# ______________________________________________________________________________________________________________________
#START
def add_friend():
    # Using class Spy
    new_friend = Spy(" ", " ", 0, 0.0)

    # Asking for new friend's name
    new_friend.name = raw_input("Please add your friend's name: ")

    # Validating new friend's name
    if len(new_friend.name) > 0:
        if len(new_friend.name) > 20:
            print("Your name length is big.")
    else:
        print("Name should be not empty or length is less then 20 char.")
        return add_friend()

    new_friend.salutation = raw_input("What to call Mr. or Ms.?: ")

    # Validating new friend's salutation
    if len(new_friend.salutation) > 0:
        if len(new_friend.salutation) > 5:
            print("Your salutation is too big.")
    else:
        print("Salutation empty or check length")
        return add_friend()

    new_friend.name = new_friend.salutation + " " + new_friend.name

    # Inputing new friend's age
    new_friend.age = int(raw_input("Age: "))

    if 12 < new_friend.age < 50:
        True
    else:
        print colored("Age should be in between 12 to 50","red")
        return add_friend()

    # Inputing new friend's rating
    new_friend.rating = float(raw_input("Spy rating? "))

    if new_friend.rating > 0.0:
        True
    else:
        print("Rating should be more than 0.0")
        return add_friend()

    # Adding new friend to the friend list
    friends.append(new_friend)
    print('Friend Added!')
    with open("friends.csv", "a") as friends_data:
        writer = csv.writer(friends_data)
        writer.writerow([new_friend.name, new_friend.salutation, new_friend.age, new_friend.rating, new_friend.is_online])

    # Giving total no of friends after adding
    return len(friends)
 #END
#_______________________________________________________________________________________________________________________
                                    # Function used to select a single friend #
#_______________________________________________________________________________________________________________________
#START
def select_a_friend():
    item_position = 1
    # showing the all friends from friends list
    for friend in friends:
        print("%d. %s age: %s with ratting %f is online" %(item_position,friend.name,friend.age,friend.rating))
        item_position=item_position+1
    friend_choice=int(raw_input("choose your friend"))
    friend_choice_position=friend_choice-1
    return friend_choice_position
#END
#_______________________________________________________________________________________________________________________
                                            # Function used to send message #
#_______________________________________________________________________________________________________________________
#START
def send_a_message():
    friend_choice = friends[select_a_friend()].name

    original_image = raw_input("What is the name of the image?")
    output_path = 'output.jpg'
    text = raw_input("What do you want to say?")

    #encoding the message
    Steganography.encode(original_image, output_path, text)

    # Using ChatMessage class
    new_chat = ChatMessage(spy_name=spy1.name, friend_name=friend_choice, time=datetime.now().strftime("%d %B %Y"), message=text)

    chats.append(new_chat)
    print colored("Your secret message is ready.","blue")
    # Adding chats to Chats.csv file
    with open('Chats.csv', 'a') as chats_data:
        writer = csv.writer(chats_data)
        writer.writerow([new_chat.spy_name, new_chat.friend_name, new_chat.time, new_chat.message])
#END
#_______________________________________________________________________________________________________________________
                                        # Function used to read a message #
#_______________________________________________________________________________________________________________________
#START
def read_a_message():
    sender = select_a_friend()
    # Inputing the name of the concealed image
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    print(secret_text)

    # Add the chat to sender
    chat = ChatMessage(spy_name=spy1.name, friend_name=sender, time=datetime.now().strftime("%d %B %Y"), message=secret_text)
    friends[sender].chats.append(chat)
    print colored("Your secret message has been saved.","blue")
    # Adding chats in chats.csv
    with open("Chats.csv", 'a') as chat_data1:
        writer = csv.writer(chat_data1)
        writer.writerow([chat.spy_name, chat.friend_name, chat.time, chat.message])
    new_text = (secret_text.upper()).split()
    if 'SOS' in new_text or 'ALERT' in new_text or 'HELP' in new_text:
        print colored("EMERGENCY!!", "red")


#END
#_______________________________________________________________________________________________________________________
                                     # Function used to read chats of a user #
#_______________________________________________________________________________________________________________________
# START
def read_chat(choice):
    name_friend = friends[choice].name
    with open('Chats.csv', 'rU') as chats_data:
        reader = csv.reader(chats_data)
        for row in reader:
            try:
                ch = ChatMessage(spy_name=row[0], friend_name=row[1], time=row[2], message=row[3])
                # Checking the chats of the current spy with selected friend
                if ch.spy_name == spy1.name and ch.friend_name == name_friend:
                    print colored("Your message sent to Spy name: %s "%name_friend,"blue")
                    print colored("On Time: [%s]"%ch.time,"blue")
                    print("Message: %s"% ch.message)
                    return 1
            except IndexError:
                pass
            continue

#END
#_______________________________________________________________________________________________________________________
                                             # Function used to add status #
#_______________________________________________________________________________________________________________________
#START
def add_status(current_status_message):
    if current_status_message !=None:
        print("Your current status is:"+current_status_message)
    else:
        print colored("You don't have any current messeage","red")
    question=raw_input("Do you want to select status from old status? Y/N")
    if question.upper()=="N":
        new_status=raw_input("enter your new status ")
        if len(new_status)>0:
            STATUS_MESSAGES.append(new_status)
            return(new_status)
        else:
            print colored("invalid new status need to be enter ","red")

    elif question.upper()=="Y":

        for i in range(len(STATUS_MESSAGES)):
            print(str(i)+"."+STATUS_MESSAGES[i])
        message_selection=int(raw_input("\n Choose from above status"))

        if len(STATUS_MESSAGES)>message_selection:
            update_status_message=STATUS_MESSAGES[message_selection]
        else:
            print colored("selected message is not in older status ", "red")
        return update_status_message
#END
#_______________________________________________________________________________________________________________________
                                # Function used to show the menu to the user #
# ______________________________________________________________________________________________________________________
# START
def start_chat(spy_name1, spy_age, spy_rating):
    current_status_messesge = None
    print("Your current status is " + str(current_status_messesge))

    #Function which loads all the friends stored in friends.csv
    def load_friends():
        with open('friends.csv', 'rU') as friends_data:
            reader = csv.reader(friends_data)
            for row in reader:
                try:
                    friends.append(Spy(name=row[0], salutation=(row[1]), age=int(row[2]), rating=float(row[3])))
                except IndexError:
                    pass
                continue

    # Function which loads all the chats of spies stored in chats.csv
    def load_chats():
        with open("Chats.csv", 'rU') as chat_data:
            reader = csv.reader(chat_data)
            for row in reader:
                try:
                    chats.append(ChatMessage(spy_name=row[0], friend_name=row[1], time=row[2], message=row[3]))
                except IndexError:
                    pass
                continue


    # Both functions are called
    load_friends()
    load_chats()

    continue_option = "Y"

    while (continue_option == 'Y' or continue_option == 'y'):

        menu_choice = int(raw_input(
            "What would you like to do \n 1. Add a status update \n 2. Add a friend \n 3. Send a message \n 4. Read a secret message \n 5. Read chats from a user \n 6. Close the application"))

        # Displaying menu
        while (menu_choice<=6):
            if menu_choice == 1:
                print("You choose update the status ")

                current_status_messesge = str(add_status(current_status_messesge))

                print colored("Your selected status is:" +current_status_messesge,"blue") #Displays the status chosen by the spy
                break
            elif menu_choice == 2:
                print colored("Initiating your adding friend process-","yellow")

                number_of_friends = add_friend()
                print('You have %d friends' % number_of_friends)
                break
            elif menu_choice == 3:
                print colored("Initiating your sending message process-","yellow")
                send_a_message()
                break
            elif menu_choice == 4:
                print colored("Initiating your reading message process-","yellow")
                read_a_message()
                break
            elif menu_choice == 5:
                print colored("Initiating your reading chats process-","yellow")
                print "select a friend whose chat you want to see"
                choice = select_a_friend()
                read_chat(choice)
                break
            elif menu_choice ==6:
                print colored("You have successfully logged out","yellow")
                exit()
        continue_option = raw_input("Would you like to perform more operations (Y/N)")
    print("Thank you for your time")
# ______________________________________________________________________________________________________________________

spy_is_online = False  # Status of the spy
question = raw_input(
    "Would you like to continue as "+spy1.salutation+" "+spy1.name +" or create your own(Y/N)")
#_______________________________________________________________________________________________________________________
                                          # For creating a new user #
#_______________________________________________________________________________________________________________________
if question == 'N':
    spy_name1 = raw_input("Welcome to SpyChat, you must tell me your Spyname first:")
    if len(spy_name1) > 0:
        print('Welcome ' + spy_name1 + ' Glad to have you with us.')
        spy_salutation = raw_input("What should I call you Mr. or Ms. ?")
        print(
            'Alright ' + spy_salutation + '.' + spy_name1 + ' I\'d like to know a little bit more about you before we proceed')
    else:
        print('A spy needs to have a valid name. Please try again.')
    spy_age = int(raw_input('What is your age? '))  # age of the spy
    if spy_age > 12 and spy_age < 50:
        spy_rating = float(raw_input('What is your spy rating? '))
        if spy_rating > 4.5:
            print('Great Ace!')
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print('You are one of the good ones.')
        elif spy_rating >= 2.5 and spy_rating <= 3.5:
            print('You can always do better')
        else:
            print('We can always use somebody to help in the office. ')
    else:
        print('Sorry you are not of the correct age to become a spy.')
    print(
        'Authentication Complete. We are glad to have you with us. Welcome ' + spy_salutation + '.' + spy_name1 + ", Your spy rating is " + str(
            spy_rating))
    spy_is_online = True
    print('Changing the status of spy from offline to online ' + str(
        spy_is_online))
    start_chat(spy_name1, spy_age, spy_rating)  # Calling menu choice
#_______________________________________________________________________________________________________________________
                                       # for continuing as a default user #
#_______________________________________________________________________________________________________________________
elif question == 'Y':

    print colored(
        'Authentication Complete. We are glad to have you with us. Welcome ' + spy1.salutation + '.' + spy1.name + ", Your spy rating is " + str(spy1.rating),"blue")  # float value to string value
    spy_is_online = True

    start_chat(spy1.name, spy1.age, spy1.rating)  # Calling menu choice
else:
    print colored("Please select default user or create a new one.","red")
#_______________________________________________________________________________________________________________________