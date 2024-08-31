# Google translator


from tkinter import *
from tkinter import ttk
from googletrans import LANGUAGES
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os

root = Tk()
root.geometry("1500x900")
root["bg"]="light blue"
root.title("Translator")
# to add functionality in  our translator:
def translator():
    translate= Translator()
    translate_text = translate.translate(text=input_box.get(1.0,END),src=input_lang.get(),dest=output_lang.get())
    output_box.delete(1.0,END)
    output_box.insert(END,translate_text.text)
# to add sound/speech in our translator:
def speak():
    b= input_box.get(1.0,END)
    a= gTTS(b,lang="bn") 
    a.save("output.mp3")
    playsound("output.mp3")
    os.remove("output.mp3")
def speak2():
    c= output_box.get(1.0,END)
    d= gTTS(c,lang="bn") 
    d.save("output1.mp3")
    playsound("output1.mp3")
    os.remove("output1.mp3")
# heading of project in window
lbl1 = Label(root, text="Translator",font="arial 30 bold underline",borderwidth=4,relief="sunken",bg="light yellow")
lbl1.pack(pady=10)
#  user Input language block:
frm=Frame(root,width=500,height=500,bg="silver",bd=30,highlightbackground="black",highlightthickness=3)
frm.place(x=100,y=90)
input_label=Label(root, text="Input language",font="arial 15 bold" ,bd=10 ,borderwidth=2,relief="solid",height=2,bg="wheat")
input_label.place(x=150,y=130)
languages= list(LANGUAGES.values())
input_lang=ttk.Combobox(root,values=languages)
input_lang.set("select language:")
input_lang.place(x=400,y=135,height=35)
# user output Language block:
frm=Frame(root,width=500,height=500,bg="silver",bd=30,highlightbackground="black",highlightthickness=3)
frm.place(x=770,y=90)
output_label=Label(root, text="Output language",font="arial 15 bold", bd=10,borderwidth=2,relief="solid",height=2,bg="wheat")
output_label.place(x=820,y=130)
output_lang=ttk.Combobox(root,values=languages)
output_lang.set("select language:")
output_lang.place(x=1090,y=135,height=35)
btn1=Button(root,text="Speak",font="arial 15 bold",bd=7,bg="PeachPuff2",command=speak2)
btn1.place(x=950,y=520,height=40,width=150)
#input box for translation
input_box=Text(root,width=43,height=15,background="light yellow",borderwidth=4,relief="sunken")
input_box.place(x=170,y=235)
# buttons
btn=Button(root,text="Speak",font="arial 15 bold",bd=7,bg="PeachPuff2",command=speak)
btn.place(x=270,y=520,height=40,width=150)
# output box for translation
output_box=Text(root, width=44,height=15,background="light yellow",borderwidth=4,relief="sunken")
output_box.place(x=840,y=235)
# Translate button
btns=Button(root,text="Translate",font="arial 15",bd=10,bg="light green",command=translator)
btns.place(x=580,y=620,height=55,width=220)
mainloop()