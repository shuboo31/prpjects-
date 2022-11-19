from tkinter import *
import random

root=Tk()
root.title("project colour")
root.geometry("500x500")

dictionary = {"colour":["purple","blue","red","white",]}

def bg():
    random_number=random.randint(0,3)
    print(dictionary["colour"][random_number])
    root.configure(background=dictionary["colour"][random_number])
    
    
    btn=Button(root,text = "click me", command = bg)
    btn.place(relx = 0.5, rely =0.6, anchor = CENTER)
    
    
    
    
    
    
    
root.mainloop()













