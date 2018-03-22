print('Hello!') #print is a  function in python to print whatever comes after it to the screen.
print('Let\'s get started')
#input("What is your name?") #input is a function to input something from the spy.
spy_name = input("What is your name?") #store the name in a variable called spy_name.
print('Welcome ' + spy_name + '. Glad to have you back with us.') #'+' symbol to join strings together.
spy_salutation = input("What should we call you (Mr. or Ms.)?") #Another variable to store the salutation.
spy_salutation + " " + spy_name #We are joining the two strings together.
spy_name = spy_salutation + " " + spy_name #Variable re-assignment
print('Alright ' + spy_name + '. I\'d like to know a little bit more about you.')

spy_name = input("Welcome to spy chat, you must tell me your spy name first: ")

##############################MODULE 2###############################
if len(spy_name) > 0: #if is used for condition
    # Start writing from here now. See how this is under the if statement?

    print('Welcome ' + spy_name + '. Glad to have you back with us.')

    spy_salutation = input("Should I call you Mister or Miss?: ")

    spy_name = spy_salutation + " " + spy_name

    print("Alright  " + spy_name + ". I'd like to know a little bit more ")
else:

    print("A spy needs to have a valid name. Try again please.")

spy_age = 0#initializing age with 0
spy_rating = 0.0#initializing rating with 0

spy_age = int(input("What is your age?"))
if spy_age > 12 and spy_age < 50:
    spy_rating = int(input("What is your spy rating?"))
else:
    print('Sorry you are not of the correct age to be a spy')

spy_rating = int(input("What is your spy rating?"))
if spy_rating > 4.5:
    print('Great ace!')
elif spy_rating > 3.5 and spy_rating <= 4.5:
    print('You are one of the good ones.')
elif spy_rating >= 2.5 and spy_rating <= 3.5:
    print('You can always do better')
else:
    print('We can always use somebody to help in the office.')

print('Welcome to the spychat '+spy_salutation +' ' + spy_name + ' with age '+str(spy_age)+' and spy rating as '+str(spy_rating)+'.')


