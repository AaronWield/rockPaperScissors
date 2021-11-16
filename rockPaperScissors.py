from tkinter import *
import random

root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('DataFlair-Rock,Paper,Scissors')
root.config(bg = 'seashell3')

user_take = StringVar()
Label(root, text='Rock, Paper, Scissors', font='arial 20 bold', bg='seashell2').pack()
Entry(root, font='arial 15', textvariable= user_take, bg='antiquewhite2').place(x=90, y=130)

comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock',
elif comp_pick == 2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'

result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick.lower() == comp_pick:
        result.set('tie, you both selected the same')
    elif user_pick.lower() == 'rock' and comp_pick == 'paper':
        result.set('you lose, computer selected paper')
    elif user_pick.lower() == 'rock' and comp_pick == 'scissors':
        result.set('you win, computer selected scissors')
    elif user_pick.lower() == 'paper' and comp_pick == 'scissors':
        result.set('you lose, computer selected scissors')
    elif user_pick.lower() == 'paper' and comp_pick == 'rock':
        result.set('you win, computer selected rock')
    elif user_pick.lower() == 'scissors' and comp_pick == 'rock':
        result.set('you lose, computer selected rock')
    elif user_pick.lower() == 'scissors' and comp_pick == 'paper':
        result.set('you win, computer selected paper')
    else:
        result.set('invalid: choose only one of -- rock, paper, scissors')

def reset():
    result.set("")
    user_take.set("")

def exit():
    root.destroy()

Entry(root, font = 'arial 10 bold', textvariable = result, bg ='antiquewhite2',width = 50,).place(x=25, y=250)
Button(root, font = 'arial 13 bold', text = 'PLAY', padx =5, bg ='seashell4' ,command = play).place(x=150,y=190)
Button(root, font = 'arial 13 bold', text = 'RESET', padx =5, bg ='seashell4' ,command = reset).place(x=70,y=310)
Button(root, font = 'arial 13 bold', text = 'EXIT', padx =5, bg ='seashell4' ,command = exit).place(x=230,y=310)

root.mainloop()
