from datetime import datetime

#Creating a Spy class
class Spy:

  def __init__(self, name, salutation, age, rating):
    self.name = name
    self.salutation = salutation
    self.age = age
    self.rating = rating
    self.is_online = True
    self.chats = []
    self.current_status_message = None

#Creating a ChatMessage class
class ChatMessage:

  def __init__(self, message, sent_by_me):
    self.message = message
    self.time = datetime.now()
    self.sent_by_me = sent_by_me

# Defining name,age and rating of default user
spy = Spy('bond', 'Mr.', 24, 4.7)

#Details of existing friends
friend_one = Spy('Navdha', 'Ms.', 21, 3.9)
friend_two = Spy('Mohak', 'Ms.', 22, 4.39)
friend_three = Spy('Kailash', 'Dr.', 37, 4.95)

#List of friends
friends = [friend_one, friend_two, friend_three]

