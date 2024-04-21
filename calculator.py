import tkinter
from tkinter import *

root = Tk()
root.title("Dhana's Calculator") 
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="#FFC0CB")  

equation = ""

def show(value):
    global equation
    equation += value
    label_result.config(text=equation)
    
def clear():
    global equation
    equation = ""
    label_result.config(text=equation)
        
def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
            equation = str(result)  
        except:
            result = "Error"
        label_result.config(text=result)

label_result = Label(root, width=25, height=2, text="", font=("Helvetica", 45), fg="#fff", bg="#FFC0CB")  
label_result.pack()

Button(root, text="C", width=5, height=1, font=("Helvetica", 45, "bold"), bd=1, fg="#fff", bg="#4a90e2", command=lambda: clear()).place(x=10, y=100)
Button(root, text="/", width=5, height=1, font=("Helvetica", 45, "bold"), bd=1, fg="#fff", bg="#474747", command=lambda: show("/")).place(x=120, y=100)
Button(root, text="%", width=5, height=1, font=("Helvetica", 45, "bold"), bd=1, fg="#fff", bg="#474747", command=lambda: show("%")).place(x=230, y=100)  
Button(root, text="*", width=5, height=1, font=("Helvetica", 45, "bold"), bd=1, fg="#fff", bg="#474747", command=lambda: show("*")).place(x=340, y=100)

Button(root, text="7", width=5, height=1, font=("Helvetica", 45, "bold"), bd=1, fg="#fff", bg="#474747", command=lambda: show("7")).place(x=10, y=200)
Button(root, text="8", width=5, height=1, font=("Helvetica", 45, "bold"), bd=1, fg="#fff", bg="#474747", command=lambda: show("8")).place(x=120, y=200)
Button(root, text="9", width=5, height=1, font=("Helvetica", 45, "bold"), bd=1, fg="#fff", bg="#474747", command=lambda: show("9")).place(x=230, y=200)
Button(root, text="-", width=5, height=1, font=("Helvetica", 45, "bold"), bd=1, fg="#fff", bg="#474747", command=lambda: show("-")).place(x=340, y=200)

Button(root, text="4", width=5, height=1, font=("Helvetica", 45, "bold"), bd=1, fg="#fff", bg="#474747", command=lambda: show("4")).place(x=10, y=300)
Button(root, text="5", width=5, height=1, font=("Helvetica", 45, "bold"), bd=1, fg="#fff", bg="#474747", command=lambda: show("5")).place(x=120, y=300)
Button(root, text="6", width=5, height=1, font=("Helvetica", 45, "bold"), bd=1, fg="#fff", bg="#474747", command=lambda: show("6")).place(x=230, y=300)
Button(root, text="+", width=5, height=1, font=("Helvetica", 45, "bold"), bd=1, fg="#fff", bg="#474747", command=lambda: show("+")).place(x=340, y=300)

Button(root, text="1", width=5, height=1, font=("Helvetica", 45, "bold"), bd=1, fg="#fff", bg="#474747", command=lambda: show("1")).place(x=10, y=400)
Button(root, text="2", width=5, height=1, font=("Helvetica", 45, "bold"), bd=1, fg="#fff", bg="#474747", command=lambda: show("2")).place(x=120, y=400)
Button(root, text="3", width=5, height=1, font=("Helvetica", 45, "bold"), bd=1, fg="#fff", bg="#474747", command=lambda: show("3")).place(x=230, y=400)
Button(root, text="0", width=11, height=1, font=("Helvetica", 45, "bold"), bd=1, fg="#fff", bg="#474747", command=lambda: show("0")).place(x=10, y=500)

Button(root, text=".", width=7, height=1, font=("Helvetica", 45, "bold"), bd=1, fg="#fff", bg="#474747", command=lambda: show(".")).place(x=230, y=500)
Button(root, text="=", width=5, height=3, font=("Helvetica", 45, "bold"), bd=1, fg="#fff", bg="#f57c00", command=lambda: calculate()).place(x=340, y=400)

root.mainloop()
