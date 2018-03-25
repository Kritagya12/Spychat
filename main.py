##############################MODULE 1###############################
print('Hello!') #print is a  function in python to print whatever comes after it to the screen.
print('Let\'s get started')
#input("What is your name?") #input is a function to input something from the spy.
spy_name = input("What is your name?") #store the name in a variable called spy_name.
print('Welcome ' + spy_name + '. Glad to have you back with us.') #'+' symbol to join strings together.
spy_salutation = input("What should we call you (Mr. or Ms.)?") #Another variable to store the salutation.
spy_salutation + " " + spy_name #We are joining the two strings together.
spy_name = spy_salutation + " " + spy_name #Variable re-assignment
print('Alright ' + spy_name + '. I\'d like to know a little bit more about you.')


##############################MODULE 2###############################
spy_age = 0#initializing age with 0
spy_rating = 0.0#initializing rating with 0
from spy_details import spy_name, spy_salutation, spy_age, spy_rating#Importing details from spy_details.py

question = "Continue as " + spy_salutation + " " + spy_name + "(Y/N)?" #To know if the spy is default user or not
existing = input(question)
if(existing=="Y"):
    print("Welcome to spychat %s %s Age: %d Your rating:%f" % (spy_salutation, spy_name, spy_age, spy_rating)) #print('Welcome to the spychat ' + spy_salutation + ' ' + spy_name + ' with age ' + str(spy_age) + ' and spy rating as ' + str(spy_rating) + '.')
else:
    spy_name=input("Welcome to spy chat, you must tell me your spy name first: ")#spy creating his own user
    if len(spy_name) > 0:
        spy_salutation = input("Should I call you Mr. or Ms.?: ")

        spy_age = int(input("What is your age?"))
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
        print("Welcome to spychat %s %s Age: %d Your rating:%f" %(spy_salutation,spy_name,spy_age,spy_rating))
       # print('Welcome to the spychat ' + spy_salutation + ' ' + spy_name + ' with age ' + str(spy_age) + ' and spy rating as ' + str(spy_rating) + '.')


def start_chat(spy_name,spy_age, spy_rating): #start_chat is a function
  menu_choices = "What do you want to do? \n 1. Add a status update\n 2. Exit"
  menu_choice = input(menu_choices)

  if (menu_choice == '1'):
    print('Add status')#Add Status Update
  elif(menu_choice=='2'):
      print('Exit')#Exit Application
  else:
      print('Choose another option')





