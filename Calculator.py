##Calculator
import tkinter as tk

app = tk.Tk()
app.title("Calculator")
app.geometry('350x330')

#Type Box
box = tk.Variable(app)
tk.Entry(app,textvariable = box, justify = 'right', font=('Arial',18,'bold')).place(x=20, y=10, width = 310, height = 50)

#-----Working Functions
exp = ""
#Operator/Digit Funciton
def operate(e):
    global exp
    exp += str(e)
    box.set(exp)

#Calculating Funciton
def equal(n):
    global exp
    res = str(eval(exp))
    box.set(res)
    exp=""
    

#Clear Funciton
def clear(x):
    global exp
    exp = ""
    box.set('')
    



#Buttons
tk.Button(app,text='Clear', command=lambda:clear('Clear')).place(x=20, y=70, width = 144, height = 40)    
tk.Button(app,text='*', command=lambda:operate('*')).place(x=180, y=70, width = 72, height = 40)
tk.Button(app,text='/', command=lambda:operate('/')).place(x=260, y=70, width = 72, height = 40)
tk.Button(app,text='7', command=lambda:operate('7')).place(x=20, y=120, width = 72, height = 40)    
tk.Button(app,text='8', command=lambda:operate('8')).place(x=100, y=120, width = 72, height = 40)
tk.Button(app,text='9', command=lambda:operate('9')).place(x=180, y=120, width = 72, height = 40)
tk.Button(app,text='-', command=lambda:operate('-')).place(x=260, y=120, width = 72, height = 40)
tk.Button(app,text='4', command=lambda:operate('4')).place(x=20, y=170, width = 72, height = 40)    
tk.Button(app,text='5', command=lambda:operate('5')).place(x=100, y=170, width = 72, height = 40)
tk.Button(app,text='6', command=lambda:operate('6')).place(x=180, y=170, width = 72, height = 40)
tk.Button(app,text='+', command=lambda:operate('+')).place(x=260, y=170, width = 72, height = 40)
tk.Button(app,text='1', command=lambda:operate('1')).place(x=20, y=220, width = 72, height = 40)    
tk.Button(app,text='2', command=lambda:operate('2')).place(x=100, y=220, width = 72, height = 40)
tk.Button(app,text='3', command=lambda:operate('3')).place(x=180, y=220, width = 72, height = 40)
tk.Button(app,text='=', command=lambda:equal('=')).place(x=260, y=220, width = 72, height = 90)
tk.Button(app,text='00', command=lambda:operate('00')).place(x=20, y=270, width = 72, height = 40)
tk.Button(app,text='0', command=lambda:operate('0')).place(x=100, y=270, width = 72, height = 40)
tk.Button(app,text='.', command=lambda:operate('.')).place(x=180, y=270, width = 72, height = 40)

app.mainloop()
