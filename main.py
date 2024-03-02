import speech_recognition as sr
from tkinter import*
import tkinter
import customtkinter
from tkinter import Tk
root= Tk()
root.configure (bg ='black')
photo= PhotoImage(file =r"C:/Users/HP/OneDrive/Pictures/text-to-speech (1).png")
root.iconphoto (False ,photo)
root.geometry("600x400")
root.title ("Speech to Text")
l1=customtkinter.CTkLabel(master=root,text="please say something....",width=120,height=25 ,corner_radius=8)
l1.place(relx=0.5,rely=0.1,anchor=tkinter.CENTER)
def Wait():
    var=IntVar()
    root.after(1000,var.set, 1)
    root.wait_variable(var)
def english():
    l3=customtkinter.CTkLabel(master=root ,text ="you have said:\n"+r.recognize_google(audio))
    l3.place(relx=0.5,rely=0.5, anchor= tkinter.CENTER)
def tamil():
    l4=customtkinter.CTkLabel(master=root,text='நீங்கள் கூறியது :\n'+r.recognize_google(audio,language='ta IN'))
    l4.place(relx=0.5,rely=0.6,anchor=tkinter.CENTER)
Wait()
r=sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    audio=r.listen(source,phrase_time_limit=(None))
    l2=customtkinter.CTkLabel(master=root,text ="Click English for English text converion n Click Tamil for Tamil text converion" ,corner_radius=8)
    l2.place(relx=0.5,rely=0.2, anchor=tkinter.CENTER)
    bt1=customtkinter.CTkButton(master=root, text='English', command=english ,corner_radius=8)
    bt1.place(relx=0.4, rely=0.3, anchor=tkinter.E)
    bt2=customtkinter.CTkButton( master=root, text= 'தமிழ்',command= tamil, corner_radius=8)
    bt2.place(relx=0.6,rely=0.3,anchor=tkinter.W)
root.mainloop()
