from tkinter import *
from PIL import Image,ImageTk
def Interface():
    root=Tk() # for window opening tag
    root.geometry('+%d+%d'%(1250,10))

    header = Frame(root,width=800,height=175,bg="white")
    header.grid(columnspan=3,rowspan=2,row=0)

    logo = Image.open('logo.PNG')
    logo= logo.resize((int(logo.size[0]/3),int(logo.size[1]/3)))
    logo= ImageTk.PhotoImage(logo)
    logo_label = Label(image=logo , bg="white" )
    logo_label.image = logo
    logo_label.grid(column=0,row=0,rowspan=2,sticky=NW,padx=20,pady=40)

    instruction = Label(root,text="Enter The Grammer : ",font="Raleway",bg="white")
    instruction.grid(columnspan=2,column=0,row=0,rowspan=2)

    text = Entry(text="enter the text : ")
    text.grid(column=1,row=0,rowspan=2)

    button = Button(root,text='CLICK ',command=lambda:clickfunction(text),font=("shanti,5"),height=1,width=20,bg="#c8c8c8")
    button.grid(columnspan=3,column=0,row=1,rowspan=2)

    save_img= Frame(root,width=800,height=175,bg="#c8c8c8")
    save_img.grid(columnspan=3,rowspan=1,row=4)


    root.mainloop() # for window closing tag
def clickfunction(text):
    input = text.get()
    print(input)
Interface()