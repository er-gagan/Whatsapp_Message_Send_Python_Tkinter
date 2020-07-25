from tkinter import *

import time
import webbrowser as web
import pyautogui as pg

root=Tk()
root.geometry('600x500')
root.resizable(0,0)
root.title("Send Whatsapp Message")
photo = PhotoImage(file = "./icon.png")
root.iconphoto(False,photo)

filename = PhotoImage(file = "./background.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

ph=StringVar()
msg=StringVar()

def Send():
    Phone="+91"+e1.get()
    Message=t1.get('1.0',END)
    web.open('https://web.whatsapp.com/send?phone='+Phone+'&text='+Message)
    time.sleep(30)
    pg.press('enter')
    
def Clear():
    ph.set("")
    t1.delete('1.0',END)

Label(root,text="Phone: +91",font=('Calibri',20),bg="#1EBEA5").place(x=50,y=60)
e1=Entry(root,font=('Calibri',20),bd=5,width=25,textvariable=ph)
e1.place(x=180,y=60)

Label(root,text="Message:",font=('Calibri',20),bg="#1EBEA5").place(x=50,y=125)
t1=Text(root,height=5,width=25,bd=5,font=('Calibri',20))
t1.place(x=180,y=125)

Button(root,text="Send",font=('Calibri',25),width=6,bd=5,command=Send).place(x=130,y=320)
Button(root,text="Clear",font=('Calibri',25),width=6,bd=5,command=Clear).place(x=320,y=320)

Label(root,text="Message will be sent on after 30 second",font=('Calibri',15),bg="#1EBEA5").place(x=120,y=420)

root.mainloop()