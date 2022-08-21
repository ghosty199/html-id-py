from tkinter import *
import random
from PIL import Image, ImageTk
from tkinter import filedialog
import os
import webbrowser
from tkinter.filedialog import askopenfilename
root=Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.title("html ID")
root.config(bg="white")
save1=ImageTk.PhotoImage(Image.open("save.png"))
open1=ImageTk.PhotoImage(Image.open("open.png"))
play1=(Image.open("play.png"))
play2=play1.resize((30,30))
play3=ImageTk.PhotoImage(play2)




label5=Label(root,text="File name", bg="white", fg="black")
label5.place(relx=0.4, rely=0.1, anchor=CENTER)

inputbox=Entry(root,)
inputbox.place(relx=0.6, rely=0.1, anchor=CENTER)

my_text=Text(root,height=35, width=80)
my_text.place(relx=0.5, rely=0.55, anchor=CENTER)


name=""
def openfile():
    global name
    my_text.delete(1.0, END)
    inputbox.delete(0, END)
    textfile=filedialog.askopenfilename(title="openhtmlfile",filetypes=(("htmlfiles","*.html"),))
    
    print(textfile)
    name=os.path.basename(textfile)
    formattedname=name.split('.')[0]
    inputbox.insert(END,formattedname)
    root.title(formattedname)
    textfile=open(name,'r')
    paragraph=textfile.read()
    my_text.insert(END, paragraph)
    textfile.close()
    
def save():
    inputname=inputbox.get()
    file=open(inputname+".html","w")
    data=my_text.get("1.0",END)
    file.write(data)
    my_text.delete(1.0, END)
    inputbox.delete(0, END)
     
    
def window():
    global name
    webbrowser.open(name)


button1=Button(root,image=save1, command=save)
button1.place(relx=0.1, rely=0.1, anchor=CENTER)

button2=Button(root,image=open1, command=openfile)
button2.place(relx=0.2, rely=0.1, anchor=CENTER)

button3=Button(root,image=play3, command=window)
button3.place(relx=0.3, rely=0.1, anchor=CENTER)







root.mainloop()