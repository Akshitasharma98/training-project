from select_friend import select_friend
from steganography.steganography import Steganography
from spy_details import friends
from send_message_help import send_message_help
from spy_details import ChatMessage


import re


from termcolor import colored
from colorama import init


init()


def read_message():

    sender = select_friend()

    encrypted_image = raw_input("Provide encrypted image : ")
    pattern_e = '^[a-zA-Z]+\.jpg$'


    try:
        secret_message = Steganography.decode(encrypted_image)
        print "The secret message is ",
        print (colored(secret_message, 'red'))
        words = secret_message.split()


        new = (secret_message.upper()).split()


        friends[sender].count += len(words)

        if "SOS" in new or "SAVE" in new or "HELP" in new or "ACCIDENT" in new:

            print (colored("!", 'grey', 'on_yellow')),
            print (colored("!", 'grey', 'on_yellow')),
            print (colored("!", 'grey', 'on_yellow'))

            print (colored("The friend who sent this message need your help.", 'cyan'))
            print (colored("You can help your friend by sending helping message.", 'cyan'))
            print (colored("Select the friend to send helping message", 'red'))


        send_message_help()


        print (colored("You just sent a message to help your friend.", 'blue'))


        new_chat = ChatMessage(secret_message, False)
        friends[sender].chats.append(new_chat)
        print (colored("Your secret message has been saved.", 'cyan'))


        print "Average words said by : ",
        print (colored(friends[sender].name, 'red')),
        print " is ",
        print (colored(friends[sender].count, 'blue'))


        if(len(words)>100):
            print (colored(friends[sender].name, 'red')),
            print (colored(" removed from friends list. He is chatterbox!.", 'yellow'))

            friends.remove(friends[sender])

    except TypeError:
        print(colored("This image has no secret message. No need to decode. Hehe!"))


        if (re.match(pattern_e, encrypted_image) != None):
            print (colored('All perfect', 'red'))
        else:
            print (colored('Sorry! Invalid entry. We can\'t validate your input and output\n ', 'yellow'))
            print (colored('You have entered wrong data.\n ', 'yellow'))