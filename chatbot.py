from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading
import pyaudio

engine = pp.init()
voices = engine.getProperty('voices')

bot = ChatBot("Chatterbot")

engine.setProperty('voice', voices[0].id)

convo = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "what is your name",
    "My name is Chattebot , I am created by devansh"
]
#
trainer = ListTrainer(bot)

trainer.train(convo)

# print("Talk to bot")
#
# while True:
#     query=input()
#     if query == 'exit':
#         break
#     answer = chatbot.get_response(query)
#     print("bot : ",answer)

root = Tk()
root.geometry("500x673")
root.title("ChatBot")
img = PhotoImage(file="./logo.png")
photoL = Label(root, image=img)
photoL.pack(pady=5)
frame = Frame(root)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()


############################## Functions ***********************
# def takeQuery():
#     sr = s.Recognizer()
#     sr.pause_threshold = 1
#     print("your bot is listening try to speak")
#     with s.Microphone() as m:
#         try:
#             audio = sr.listen(m)
#             query = sr.recognize_google(audio, language='eng-in')
#             print(query)
#             textF.delete(0, END)
#             textF.insert(0, query)
#             ask_from_bot()
#         except EXCEPTION as e:
#             print(e)
#             print("Not recoginzed")


def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


def enter_function(event):
    btn.invoke()


def speak(word):
    engine.say(word)
    engine.runAndWait()


############################## Text Field **********************
textF = Entry(root, font=("Hack", 20))
textF.pack(fill=X, pady=10)

############################ Button ****************************
btn = Button(root, text="Ask from bot", font=("Josefin Sans", 20), command=ask_from_bot)
btn.pack()

root.bind('<Return>', enter_function)


# def repatL():
#     while True:
#         takeQuery()


# t = threading.Thread(target=repatL)
# t.start()
root.mainloop()
