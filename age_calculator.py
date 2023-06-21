from datetime import date
today = date.today()
 
def exit():
    window.destroy()
def get_age():
    d= int(e1.get())
    m= int(e2.get())
    y= int(e3.get())
    age =today.year-y-((today.month, today.day)<(m,d))
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    t1.insert(tk.END,age)
    t1.config(state='disabled')
 
import tkinter as tk
from tkinter import *
window = tk.Tk()
window.geometry("400x300")
window.config(bg="#F7DC6F")
window.resizable(width=False,height=False)
window.title('Age Calculator!')

l1 = tk.Label(window,text="The Age Calculator!",font=("arial",20,"bold"))
l2 = tk.Label(window,text=("Enter your Birthday which includes your date,month and year"),font=("arial",12,"bold"))
l3 = tk.Label(window,text=("The Calculated age is:"),font=("arial",12,"bold"))
l_d = tk.Label(window,text="DATE:",font=("arial",12,"bold"))
l_m = tk.Label(window,text="MONTH:",font=("arial",12,"bold"))
l_y = tk.Label(window,text="YEAR:",font=("arial",12,"bold"))
e1 = tk.Entry(window,width=5)
e2 = tk.Entry(window,width=5)
e3 = tk.Entry(window,width=5)
b1 = Button(window,text=("Calculate AGE!"),font=("arial,20,bold"),command=get_age)
b2 = Button(window,text=("EXIT APPLICATION"),font=("arial,20,bold"),command=exit)
t1 = tk.Text(window,width=5,height=0,state="disabled")

l1.place(x=70,y=5)
l2.place(x=10,y=40)
l_d.place(x=100,y=70)
l_m.place(x=100,y=95)
l_y.place(x=100,y=120)
e1.place(x=180,y=70)
e2.place(x=180,y=95)
e3.place(x=180,y=120)
b1.place(x=100,y=150)
l3.place(x=50,y=200)
t1.place(x=240,y=203)
b2.place(x=100,y=230)

window.mainloop()