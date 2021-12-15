from tkinter import *
from plot import graf
from table import opentable
from to_json import ruhjson
from to_json import zasobyjson

root = Tk()
root.title('Панель')
root.geometry('320x220')
root.resizable(False, False)
root.configure(bg = 'gray')

def Plot():
    graf()

def Table():
    opentable()
   
def Zasobyjson():
    zasobyjson()

def Ruhjson(): 
     ruhjson()   

btn1 = Button(root)
btn1.configure(bg = 'black', fg = 'yellow', text = 'відкрити графік', command = Plot)
btn1.place(x = -10, y = 0, width = 320, height = 55)
btn2 = Button(root)
btn2.configure(bg = 'black', fg = 'yellow', text = 'відкрити таблицю', command = Table)
btn2.place(x = -10, y = 55, width = 320, height = 55)
btn3 = Button(root)
btn3.configure(bg = 'black', fg = 'yellow', text = 'сформувати файл руху json', command = Zasobyjson)
btn3.place(x = -10, y = 165, width = 320, height = 55)
btn4 = Button(root)
btn4.configure(bg = 'black', fg = 'yellow', text = 'сформувати файл засобів json', command = Ruhjson)
btn4.place(x = -10, y = 110, width = 320, height = 55)
root.mainloop() 
