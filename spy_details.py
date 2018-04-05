from datetime import datetime

#Creating a Spy class
class Spy:

  def __init__(self, name, age, rating):
    self.name = name
    self.age = age
    self.rating = rating
    self.is_online = True
    self.chats = []
    self.current_status_message = None

#Creating a Spy_friend class
class Spy_friend:

    def __init__(self,name, age, rating,chat):
        self.name = name
        self.age =age
        self.rating = rating
        self.is_online = True
        self.chats = chat
        self.current_status_message = None

# Defining name,age and rating of default user
spy = Spy('Ms. Kritagya', 22, 4.7)

#Details of existing friends
friend_one = Spy_friend('Mr. Gopal', 25, 3.8,[])
friend_two = Spy_friend('Ms. Kirti', 29, 4.69,[])
friend_three = Spy_friend('Mr. Nikhil', 45, 3,[])

#List of friends
friends = [friend_one, friend_two, friend_three]

#Creating a ChatMessage class
class ChatMessage:

  def __init__(self, message, sent_by_me):
    self.message = message
    self.time = datetime.now()
    self.sent_by_me = sent_by_me




