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

# Defining name,age and rating of default user
spy1 = Spy('Kritagya','Ms.' ,22, 4.7)

#List of friends
friends = []

#Creating a ChatMessage class
class ChatMessage:
  def __init__(self, spy_name, friend_name, time, message):
    self.spy_name = spy_name
    self.friend_name = friend_name
    self.time = time
    self.message = message

#List of chats
chats=[]




