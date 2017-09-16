# importing datetime to show time and date of chat.
from datetime import datetime


class Spy:
    def __init__(self, name, salutation, age, rating):
        # initializing the values
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


        self.count = 0


class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


spy = Spy('Akshita', 'Ms.', 19, 4.7)

friend_one = Spy('Dipanshi, ', 'Ms.', 19, 4.8)
friend_two = Spy('Mohit, ', 'Mr.', 20, 4.6)
friend_three = Spy('Karan, ', 'Mr.',21, 4.7)
friend_four = Spy('Kanchan, ', 'Ms.',20, 4.7)

friends = [friend_one, friend_two, friend_three, friend_four]

