
from spy_details import Spy, friends

import re


from termcolor import colored


def add_friend():
    new_friend = Spy(" ", " ", 0, 0.0)

    new_friend.name = raw_input("Please add your friend's name: ")


    new_friend.salutation= raw_input("What to call Mr. or Ms.?: ")


    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = int(raw_input("Age? "))

    new_friend.rating = float(raw_input("Spy rating? "))

    if len(new_friend.name) > 0 and new_friend.name.isdigit() == False and re.match(pattern_n,new_friend.name)!=None and re.match(pattern_s,new_friend.salutation)!=None and new_friend.age > 12 and new_friend.rating < 50 and re.match(pattern_a,new_friend.age)!=None and new_friend.salutation.isalpha() ==  True and new_friend.rating >= 0 and re.match(pattern_r,new_friend.rating)!=None:

        friends.append(new_friend)
        print (colored('Friend Added!', 'blue'))
    else:
        print (colored('Sorry! Invalid entry. We can\'t add spy with the details you provided\n ', 'blue'))
    print (colored('Please enter the right data, don\'t make mistakes.', 'blue'))



    return len(friends)