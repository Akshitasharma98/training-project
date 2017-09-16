# importing spy details and start chat
from spy_details import spy
from start_chat import  start_chat

from termcolor import colored

print (colored("Hi!,","blue"))
print "Let's get started!\n"


question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N): "
existing = raw_input(colored(question,"red"))


if (existing.upper() == "Y") :

    spy_name = spy.salutation + " " + spy.name

    start_chat(spy.name, spy.age, spy.rating, spy.is_online)
elif (existing.upper() == "N"):

    spy.name = raw_input("What is your name :")

    if len(spy.name) > 0:
        spy.salutation = raw_input("What should we call you ? : ")


        while True:
            try:
                spy.age = int(raw_input("Enter your age: ")) # converting users input to integer (typecasting)
                break
            except ValueError:
                print "Invalid age. Try again"


        spy.name = spy.salutation + " " + spy.name

        spy.rating = float(raw_input("What is your spy rating?")) # converting users input to float (typecasting)
        spy.is_online = True

        start_chat(spy.name, spy.age, spy.rating, spy.is_online)
    else:
        print "Invalid name. Try again."
else:
    print "Wrong choice. Try again."
