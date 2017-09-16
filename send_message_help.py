from select_friend import select_friend
from spy_details import ChatMessage, friends


def send_message_help():

    friends_choice = select_friend()


    text = "Hey my dear, I'm coming to save you. Don't worry. "


    new_chat = ChatMessage(text, True)


    friends[friends_choice].chats.append(new_chat)
