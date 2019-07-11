from tkinter import *

#=====================Settings===============

root = Tk()
root.title('Calculator')
root.geometry('313x324')
root.resizable(width=False, height=False)


#==================Functions================

def btn_click(item):
    global expression
    expression = expression+str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression=""
    input_text.set("")

def btn_equals():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression=""

expression=""

input_text = StringVar()



#======================crate a frame for the input field===============
inputf = Frame(root, width = 312, height=50, bd=0, highlightbackground="black", highlightcolor='black', highlightthickness=1)
inputf.pack(side = TOP)


#==========================create a entry inside a input field frame=========


inputfield=Entry(inputf, font=('arial',18, 'bold'), textvariable = input_text, width = 50, bg="#eee", bd=0, justify=RIGHT)
inputfield.grid(row=0, column=0)
inputfield.pack(ipady=10)


#============create frame for the button========

btnsframe = Frame(root, width=312, height=272.5, bg='grey')
btnsframe.pack()

#============ 1st ROW ==========================================

clear = Button(btnsframe, text = "C", fg="black", width=32, height=3, bd=0, bg="#eee",  activebackground="#444", activeforeground="white", cursor="hand2", command= lambda: btn_clear()).grid(row=0, columnspan=3, padx=1, pady=1)
divide = Button(btnsframe, text = '/',fg="black", width=10, height=3, bd=0, bg="#eee",  activebackground="#444", activeforeground="white", cursor="hand2",
                command= lambda:btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

#==============second row=====================

seven = Button(btnsframe,text="7",     fg="black", width=10, height=3, bd=0, bg="#fff",  activebackground="#444", activeforeground="white", cursor="hand2", command=lambda: btn_click(7)).grid(row=1, column = 0, padx = 1, pady = 1)
eight = Button(btnsframe, text="8",    fg="black", width=10, height=3, bd=0, bg="#fff",  activebackground="#444", activeforeground="white", cursor="hand2", command=lambda :btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
nine = Button(btnsframe, text="9",     fg="black", width=10, height=3, bd=0, bg="#fff",  activebackground="#444", activeforeground="white", cursor="hand2", command=lambda :btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btnsframe, text="*", fg="black", width=10, height=3, bd=0, bg="#fff",  activebackground="#444", activeforeground="white", cursor="hand2", command=lambda :btn_click("*")).grid(row=1, column=3, padx=1, pady=1)


#==============Third row=====================

four = Button(btnsframe,    text="4", fg="black", width=10, height=3, bd=0, bg="#fff",  activebackground="#444", activeforeground="white", cursor="hand2", command=lambda: btn_click(4)).grid(row=2, column = 0, padx = 1, pady = 1)
five = Button(btnsframe,    text="5", fg="black", width=10, height=3, bd=0, bg="#fff",  activebackground="#444", activeforeground="white", cursor="hand2", command=lambda :btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
six = Button(btnsframe,     text="6", fg="black", width=10, height=3, bd=0, bg="#fff",  activebackground="#444", activeforeground="white", cursor="hand2", command=lambda :btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
minus = Button(btnsframe,   text="-", fg="black", width=10, height=3, bd=0, bg="#fff",  activebackground="#444", activeforeground="white", cursor="hand2", command=lambda :btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

#==============Fourth row=====================

one = Button(btnsframe,     text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",  activebackground="#444", activeforeground="white", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btnsframe,     text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",  activebackground="#444", activeforeground="white", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btnsframe,   text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",  activebackground="#444", activeforeground="white", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(btnsframe,    text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee",  activebackground="#444", activeforeground="white", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

#================fifth row=================
zero = Button(btnsframe, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff",  activebackground="#444", activeforeground="white", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(btnsframe, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee",  activebackground="#444", activeforeground="white", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(btnsframe, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee",  activebackground="#444", activeforeground="white", cursor = "hand2", command = lambda: btn_equals()).grid(row = 4, column = 3, padx = 1, pady = 1)








root.mainloop()