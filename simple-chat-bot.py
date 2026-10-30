# i am make a simple chat bot in python. i am using if else statement to make a simple chat bot. i am using while loop to keep the chat bot running until the user types "exit" or "quit" or "bye". i am using input() function to take input from the user. i am using print() function to print the output. i am using .lower() method to convert the input to lowercase, so that the bot can recognize the input regardless of case.

print("="*50)
print("Welcome to Chat Bot!".center(50))
print("Author: AMAN PANDEY".center(50))  #the use of 50 is to center the text in a width of 50 characters
print("="*50)

while True:
    
    chat=input("You: ".lower())  #The use of .lower() is to convert the input to lowercase, so that the bot can recognize the input regardless of case.

    if chat=="exit" or chat=="quit" or chat=="bye":
        print("Bot: Goodbye! Have a great day!")
        break
    elif chat=="hi" or chat=="hello":
        print("Bot: Hello! How can I assist you today?")

    elif chat=="how are you":
        print("Bot: I'm just a bot, but I'm functioning as expected! How about you?")
    elif chat=="what is your name":
        print("Bot: I'm a simple chat bot created by AMAN PANDEY.")
    elif chat=="what can you do":
        print("Bot: I can chat with you and answer some basic questions. You can ask me about the weather, time, or just have a casual conversation!")
    else:
        print("Bot: I'm sorry, I didn't understand that. Can you please rephrase or ask something else?")
