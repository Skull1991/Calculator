from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('355x475')
root.config(bg="#333333")
root.resizable(False, False)
root.iconbitmap("calculator.ico")
skull = Frame(root, bg='#333333')
skull.pack()

expression = ''


# Creating Function
def click(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equal():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = ''
    except:
        equation.set('ERROR')
        expression = ''


def clear():
    global expression
    expression = ''
    equation.set('0')


def off():
    root.destroy()


# Creating Entry
equation = StringVar()
equation.set('0')
e = Entry(skull, textvariable=equation, bg="#9999ff", justify='right', font=('arial', 20, 'bold'))
e.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=25, pady=15)
# Button
b1 = Button(skull, text="1", font=('arial', 12), relief="ridge", borderwidth=1, bg="#b61aff", width=8, height=3,
            command=lambda: click(1))
b2 = Button(skull, text="2", font=('arial', 12), relief="ridge", borderwidth=1, bg="#b61aff", width=8, height=3,
            command=lambda: click(2))
b3 = Button(skull, text="3", font=('arial', 12), relief="ridge", borderwidth=1, bg="#b61aff", width=8, height=3,
            command=lambda: click(3))
b4 = Button(skull, text="4", font=('arial', 12), relief="ridge", borderwidth=1, bg="#b61aff", width=8, height=3,
            command=lambda: click(4))
b5 = Button(skull, text="5", font=('arial', 12), relief="ridge", borderwidth=1, bg="#b61aff", width=8, height=3,
            command=lambda: click(5))
b6 = Button(skull, text="6", font=('arial', 12), relief="ridge", borderwidth=1, bg="#b61aff", width=8, height=3,
            command=lambda: click(6))
b7 = Button(skull, text="7", font=('arial', 12), relief="ridge", borderwidth=1, bg="#b61aff", width=8, height=3,
            command=lambda: click(7))
b8 = Button(skull, text="8", font=('arial', 12), relief="ridge", borderwidth=1, bg="#b61aff", width=8, height=3,
            command=lambda: click(8))
b9 = Button(skull, text="9", font=('arial', 12), relief="ridge", borderwidth=1, bg="#b61aff", width=8, height=3,
            command=lambda: click(9))
b0 = Button(skull, text="0", font=('arial', 12), relief="ridge", borderwidth=1, bg="#b61aff", width=8, height=3,
            command=lambda: click(0))
b_add = Button(skull, text="+", font=('arial', 12), relief="ridge", borderwidth=1, bg="#4db8ff", width=8, height=3,
               command=lambda: click("+"))
b_sub = Button(skull, text="-", font=('arial', 12), relief="ridge", borderwidth=1, bg="#ffad33", width=8, height=3,
               command=lambda: click("-"))
b_mult = Button(skull, text="*", font=('arial', 12), relief="ridge", borderwidth=1, bg="#ffff33", width=8, height=3,
                command=lambda: click("*"))
b_div = Button(skull, text="/", font=('arial', 12), relief="ridge", borderwidth=1, bg="#00e6b8", width=8, height=3,
               command=lambda: click("/"))
b_dot = Button(skull, text=".", font=('arial', 12), relief="ridge", borderwidth=1, bg="#b61aff", width=8, height=3,
               command=lambda: click("."))
b_equal = Button(skull, text="=", font=('arial', 12), relief="ridge", borderwidth=1, bg="#00e600", width=8, height=3,
                 command=lambda: equal())
b_clear = Button(skull, text="C", font=('arial', 12), relief="ridge", borderwidth=1, bg="#ff3333", width=8,
                 height=3, command=lambda: clear())
b_off = Button(skull, text="OFF", font=('arial', 12), relief="ridge", borderwidth=1, bg="#ff3333", width=8,
               height=3, command=lambda: off())
# Grid
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
b3.grid(row=2, column=2)
b_add.grid(row=3, column=3)

b4.grid(row=3, column=0)
b5.grid(row=3, column=1)
b6.grid(row=3, column=2)
b_sub.grid(row=2, column=3)

b7.grid(row=4, column=0)
b8.grid(row=4, column=1)
b9.grid(row=4, column=2)
b_mult.grid(row=1, column=2)

b0.grid(row=5, column=0, columnspan=2, sticky="nsew")
b_dot.grid(row=5, column=2)
b_clear.grid(row=1, column=3)
b_div.grid(row=1, column=1)

b_equal.grid(row=4, column=3, rowspan=2, sticky='nsew')
b_off.grid(row=1, column=0)
root.mainloop()
