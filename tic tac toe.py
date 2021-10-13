#Modules imported for Tic Tac Toe
from tkinter import *
from tkinter import messagebox

#Screen variables
turn =1
screen_height= 370
screen_width = 300
root= Tk()
root.configure(bg="grey")
root.resizable(0,0)
root.title('Tic-Tac-Toe')
root.geometry(f'{screen_width}x{screen_height}')

#Creating functions

def result():
#X winning conditions
    if b1.cget('text')=='X' and b2.cget('text')=='X' and b3.cget('text')=='X':
        messagebox.showinfo("Result",f"{X.get()} has won!!")
        turn_check.set(f"{X.get()} has won!!")
    elif b4.cget('text')=='X' and b5.cget('text')=='X' and b6.cget('text')=='X':
        messagebox.showinfo("Result",f"{X.get()} has won!!")
        turn_check.set(f"{X.get()} has won!!")
    elif b7.cget('text')=='X' and b8.cget('text')=='X' and b9.cget('text')=='X':
        messagebox.showinfo("Result",f"{X.get()} has won!!")
        turn_check.set(f"{X.get()} has won!!")
    elif b1.cget('text')=='X' and b4.cget('text')=='X' and b7.cget('text')=='X':
        messagebox.showinfo("Result",f"{X.get()} has won!!")
        turn_check.set(f"{X.get()} has won!!")
    elif b2.cget('text')=='X' and b5.cget('text')=='X' and b8.cget('text')=='X':
        messagebox.showinfo("Result",f"{X.get()} has won!!")
        turn_check.set(f"{X.get()} has won!!")
    elif b3.cget('text')=='X' and b6.cget('text')=='X' and b9.cget('text')=='X':
        messagebox.showinfo("Result",f"{X.get()} has won!!")
        turn_check.set(f"{X.get()} has won!!")
    elif b1.cget('text')=='X' and b5.cget('text')=='X' and b9.cget('text')=='X':
        messagebox.showinfo("Result",f"{X.get()} has won!!")
        turn_check.set(f"{X.get()} has won!!")
    elif b7.cget('text')=='X' and b5.cget('text')=='X' and b3.cget('text')=='X':
        messagebox.showinfo("Result",f"{X.get()} has won!!")
        turn_check.set(f"{X.get()} has won!!")
    
#Y winning conditions
    elif b1.cget('text')=='O' and b2.cget('text')=='O' and b3.cget('text')=='O':
        messagebox.showinfo("Result",f"{O.get()} has won!!")
        turn_check.set(f"{O.get()} has won!!")
    elif b4.cget('text')=='O' and b5.cget('text')=='O' and b6.cget('text')=='O':
        messagebox.showinfo("Result",f"{O.get()} has won!!")
        turn_check.set(f"{O.get()} has won!!")
    elif b7.cget('text')=='O' and b8.cget('text')=='O' and b9.cget('text')=='O':
        messagebox.showinfo("Result",f"{O.get()} has won!!")
        turn_check.set(f"{O.get()} has won!!")
    elif b1.cget('text')=='O' and b4.cget('text')=='O' and b7.cget('text')=='O':
        messagebox.showinfo("Result",f"{O.get()} has won!!")
        turn_check.set(f"{O.get()} has won!!")
    elif b2.cget('text')=='O' and b5.cget('text')=='O' and b8.cget('text')=='O':
        messagebox.showinfo("Result",f"{O.get()} has won!!")
        turn_check.set(f"{O.get()} has won!!")
    elif b3.cget('text')=='O' and b6.cget('text')=='O' and b9.cget('text')=='O':
        messagebox.showinfo("Result",f"{O.get()} has won!!")
        turn_check.set(f"{O.get()} has won!!")
    elif b1.cget('text')=='O' and b5.cget('text')=='O' and b9.cget('text')=='O':
        messagebox.showinfo("Result",f"{O.get()} has won!!")
        turn_check.set(f"{O.get()} has won!!")
    elif b7.cget('text')=='O' and b5.cget('text')=='O' and b3.cget('text')=='O':
        messagebox.showinfo("Result",f"{O.get()} has won!!")
        turn_check.set(f"{O.get()} has won!!")
    
#Draw conditions
    elif b1['text']!='' and b2['text']!='' and b3['text']!='' and b4['text']!='' and b5['text']!='' and b6['text']!='' and b7['text']!='' and b8['text']!='' and b9['text']!='' :
        messagebox.showinfo("Result","The game has ended in a draw!")
        turn_check.set("Game Draw!!")

#Button functions
#Buttons functions for entering O
def zerob1(event):
    global turn
    if turn==0 and str(event.widget.cget('text'))== "":
        if str(event.widget.cget('text'))== "":
            b1['text']= 'O'
        turn=1
        turn_check.set("X turn")
        result()
def zerob2(event):
    global turn
    if turn==0:
        if str(event.widget.cget('text'))== "":
            b2['text']= 'O'
        turn=1
        turn_check.set("X turn")
        result()
def zerob3(event):
    global turn
    if turn==0:
        if str(event.widget.cget('text'))== "":
            b3['text']= 'O'
        turn=1
        turn_check.set("X turn")
        result()
def zerob4(event):
    global turn
    if turn==0:
        if str(event.widget.cget('text'))== "":
            b4['text']= 'O'
        turn=1
        turn_check.set("X turn")
        result()
def zerob5(event):
    global turn
    if turn==0:
        if str(event.widget.cget('text'))== "":
            b5['text']= 'O'
        turn=1
        turn_check.set("X turn")
        result()
def zerob6(event):
    global turn
    if turn==0:
        if str(event.widget.cget('text'))== "":
            b6['text']= 'O'
        turn=1
        turn_check.set("X turn")
        result()
def zerob7(event):
    global turn
    if turn==0:
        if str(event.widget.cget('text'))== "":
            b7['text']= 'O'
        turn=1
        turn_check.set("X turn")
        result()
def zerob8(event):
    global turn
    if turn==0:
        if str(event.widget.cget('text'))== "":
            b8['text']= 'O'
        turn=1
        turn_check.set("X turn")
        result()
def zerob9(event):
    global turn
    if turn==0:
        if str(event.widget.cget('text'))== "":
            b9['text']= 'O'
        turn=1
        turn_check.set("X turn")
        result()
#Button functions for entering 1
def crossb1():
    global turn
    if turn==1:
        if b1.cget('text')== "":
            b1['text']= 'X'
        turn=0
        turn_check.set("O Turn")
        result()
def crossb2():
    global turn
    if turn==1:
        if b2.cget('text')== "":
            b2['text']= 'X'
        turn=0
        turn_check.set("O Turn")
        result()
def crossb3():
    global turn
    if turn==1:
        if b3.cget('text')== "":
            b3['text']= 'X'
        turn=0
        turn_check.set("O Turn")
        result()
def crossb4():
    global turn
    if turn==1:
        if b4.cget('text')== "":
            b4['text']= 'X'
        turn=0
        turn_check.set("O Turn")
        result()
def crossb5():
    global turn
    if turn==1:
        if b5.cget('text')== "":
            b5['text']= 'X'
        turn=0
        turn_check.set("O Turn")
        result()
def crossb6():
    global turn
    if turn==1:
        if b6.cget('text')== "":
            b6['text']= 'X'
        turn=0
        turn_check.set("O Turn")
        result()
def crossb7():
    global turn
    if turn==1:
        if b7.cget('text')== "":
                b7['text']= 'X'
        turn=0
        turn_check.set("O Turn")
        result()
def crossb8():
    global turn
    if turn==1:
        if b8.cget('text')== "":
                b8['text']= 'X'
        turn=0
        turn_check.set("O Turn")
        result()
def crossb9():
    global turn
    if turn==1:
        if b9.cget('text')== "":
                b9['text']= 'X'
        turn=0
        turn_check.set("O Turn")
        result()

# General functions
def help():
    messagebox.showinfo("Help","First enter Player X and Player O names\nUse LMB for X and RMB for O.")
def reset():
    global turn
    b1['text']= ''
    b2['text']= ''
    b3['text']= ''
    b4['text']= ''
    b5['text']= ''
    b6['text']= ''
    b7['text']= ''
    b8['text']= ''
    b9['text']= ''
    turn_check.set('X turn')
    turn=1


    


#Creating buttons

#Column 1
b1= Button(root,background="grey",padx=43,pady=20,command=crossb1,fg="red")
b1.place(x=1,y=0)
b1.bind('<Button-3>',zerob1)
b2= Button(root,background="grey",padx=43,pady=20,command=crossb2,fg="red")
b2.place(x=1,y=67)
b2.bind('<Button-3>',zerob2)
b3= Button(root,background="grey",padx=43,pady=20,command=crossb3,fg="red")
b3.place(x=1,y=133)
b3.bind('<Button-3>',zerob3)

#Column 2 
b4= Button(root,background="grey",padx=43,pady=20,command=crossb4,fg="red")
b4.place(x=99,y=0)
b4.bind('<Button-3>',zerob4)
b5= Button(root,background="grey",padx=43,pady=20,command=crossb5,fg="red")
b5.place(x=99,y=67)
b5.bind('<Button-3>',zerob5)
b6= Button(root,background="grey",padx=43,pady=20,command=crossb6,fg="red")
b6.place(x=99,y=133)
b6.bind('<Button-3>',zerob6)

#Column 3 
b7= Button(root,background="grey",padx=43,pady=20,command=crossb7,fg="red")
b7.place(x=200,y=0)
b7.bind('<Button-3>',zerob7)
b8= Button(root,background="grey",padx=43,pady=20,command=crossb8,fg="red")
b8.place(x=200,y=67)
b8.bind('<Button-3>',zerob8)
b9= Button(root,background="grey",padx=43,pady=20,command=crossb9,fg="red")
b9.place(x=200,y=133)
b9.bind('<Button-3>',zerob9)



#Player names entry
X= StringVar()
O= StringVar()
turn_check= StringVar()
turn_check.set("X turn")
name_x= Label(root,text="Player X Name:-").place(x=10,y=210)
name_o= Label(root,text="Player O Name:-").place(x=10,y=240)

player_x = Entry(root,textvariable=X).place(x=130,y=210)
player_o = Entry(root,textvariable=O).place(x=130,y=240)


#Turn Checker and other useful buttons

play_help= Button(root,text="How to play",bg="yellow",command=help).place(x=50,y=280)
reset_button= Button(root,text="Reset Choices",bg="yellow",command=reset).place(x=150,y=280)
Status = Label(root,text="Turn: ",font="Algerian 13 bold").place(x=10,y=320)
Stat_check= Entry(root,textvariable=turn_check,font="Algerian 11")
Stat_check.place(x=100,y=320)
root.mainloop()
