import nltk
import random
from nltk.chat.util import Chat, reflections

# 定义聊天机器人的响应规则
pairs = [
    [
        r"My name is (.*)",
        ["Hello %1! What can I help you? ",]
    ],
    [
        r"What's(.*)|What is(.*)",
        ["Sorry, but I don't know. ",]
    ],
    [
        r"Who(.*)",
        ["Sorry, but I don't know. ",]
    ],
    [
        r"Hello|Hi",
        ["Hello! What can I help you? ", "Hi! Nice to meet you! ",]
    ],
    [
        r"Nice to meet you too! ",
        ["So...What can I help you? ",]
    ],
    [
        r"How(.*)",
        ["Sorry, but I don't know. ",]
    ],
    [
        r"Can you(.*)",
        ["Sorry, but I can't. ",]
    ],
    [
        r"What can(.*)",
        ["Sorry, but I don't know. ",]
    ],
    [
        r"I'm(.*)",
        ["Oh! That's good. So, what can I help you? ",]
    ],
    [
        r"emmm(.*)|Uh(.*)",
        ["So...What can I help you? ",]
    ],
    [
        r"It's OK. ",
        ["OK. ",]
    ],
    [
        r"Sorry(.*)",
        ["It's OK. ",]
    ],
    [
        r"Help me to(.*)",
        ["Sorry, but I can't. "]
    ],
    [
        r"None",
        ["That's strange! Are you also a chatbot?",]
    ],
    [
        r"Yes, I am. ",
        ["emmm...",]
    ],
    [
        r"If you(.*)",
        ["OK. ",]
    ],
    [
        r"Surprise! ",
        ["(SCREAMING...)",]
    ],
    [
        r"Please(.*)",
        ["OK. I will have a try...Emmm...Uh......Oh no! I can't do it! ",]
    ],
    [
        r"Sing(.*)",
        ["OK. I will have a try...Emmm...Uh......Oh no! I can't do it! ",]
    ],
    [
        r"Write(.*)",
        ["OK. I will have a try...Emmm...Uh......Oh no! I can't do it! ",]
    ],
    [
        r"Am(.*)|Is(.*)|Are(.*)",
        ["Sorry, but I don't know. ",]
    ],
    [
        r"Call me(.*)",
        ["Sorry, but I can't change your username, except you restart this program and re-enter a new username. ",]
    ],
    [
        r"Chat with(.*)",
        ["Sure, I'd be happy to chat with you! What would you like to talk about? Any particular    interests or topics on your mind today? ",]
    ],
    [
        r"Talk about(.*)",
        ["OK. I will have a try...Emmm...Uh......Oh no! I can't do it! ",]
    ],
    [
        r"What do you think(.*)",
        ["Sorry, but I don't have any opinion on that. ",]
    ],
    [
        r"May(.*)",
        ["Sorry, but I can't handling your request. ",]
    ],
    [
        r"Should(.*)",
        ["Sorry, but I can't handling your request. ",]
    ],
    [
        r"Translate(.*)",
        ["Sorry, but I can't handling your request. ",]
    ],
    [
        r"Introduce(.*)",
        ["Sorry, but I can't handling your request. ",]
    ],
]

# 创建聊天机器人
def chatbot():
    print("   @@@@@@@@@@@@@@@@@    ")
    print("@                                                                        @")
    print("@                                                                        @")
    print("@            @@@@@@@@@@                 @")
    print("@        @                                       @                 @")
    print("@        @                                       @                 @")
    print("@        @                                       @                 @")
    print("@        @                                       @                 @")
    print("@        @                                       @                 @")
    print("@        @                                       @                 @")
    print("@        @                                        @                @")
    print("@         @@@@@@@@@@@@@@@@")
    print("")
    print("Chat Python")
    print("Version 1.0 (2024.08.02) ")
    print("Hello! I'm Chat Python the ChatBot. Enter 'Goodbye! ' to exit. ")
    chat = Chat(pairs, reflections)
    username = input("Please enter your username first: ")
    while True:
        user_input = input(f"{username}: ")  # 使用格式化字符串传递用户名作为提示信息
        if user_input == "Goodbye! ":
            print("Chat Python: Goodbye! ")
            break
        
        response = chat.respond(user_input)
        print("Chat Python: ", response)

if __name__ == "__main__":
    chatbot()
