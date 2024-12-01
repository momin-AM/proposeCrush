from tkinter import *
import tkinter.messagebox as tmsg

def main_loop():
    while True:
        ans=tmsg.askquestion('love','do you love me?')
        if ans=='yes':
            tmsg.showinfo('happy','oh my girl i am so happy lab u 2')
            break
        else:
            continue


root=Tk()
root.title('GF')
root.geometry('666x444')
Label(root,text='HEY girl welcome here').pack()
button0=Button(root,text='tap me',command=main_loop,borderwidth=8)
button0.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
