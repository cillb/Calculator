"""
This program creates a simple calculator app. It performs simple arithmetic, 
and uses a simple GUI created with tkinter.
"""
from tkinter import *
# here an expression is initialised as a string, this will be used as the information for the display
expression = ""
# a function is defined to all a button to be pressed on the calculator, the button adds corresponding information to the display
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
# a function defines the operation of the equals button
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""
# a function is defined to clear the display
def clear():
    global expression
    expression = ""
    equation.set(expression)
# a function is defined to perform the delete operation
def delete():
    global expression
    deleting = [*expression]
    deleting.pback
    expression = "".join(deleting)
    equation.set(expression)
# here the GUI is created and ran
if __name__ == "__main__":
    root = Tk()
    root.configure(background="#dddddd")
    root.wm_title("Calculator")
    root.geometry("190x230")
    # the display is created, and an expression is initialised that will be used to make calculations
    equation = StringVar()
    display = Entry(root, textvariable=equation).grid(columnspan=5, ipadx=20)
    # the number buttons are created
    button1 = Button(root, text="1", bg="white", activebackground="#66a3ff", command=lambda: press(1), height=2, width=4).grid(row=4, column=0)
    button2 = Button(root, text="2", bg="white", activebackground="#66a3ff", command=lambda: press(2), height=2, width=4).grid(row=4, column=1)
    button3 = Button(root, text="3", bg="white", activebackground="#66a3ff", command=lambda: press(3), height=2, width=4).grid(row=4, column=2)
    button4 = Button(root, text="4", bg="white", activebackground="#66a3ff", command=lambda: press(4), height=2, width=4).grid(row=3, column=0)
    button5 = Button(root, text="5", bg="white", activebackground="#66a3ff", command=lambda: press(5), height=2, width=4).grid(row=3, column=1)
    button6 = Button(root, text="6", bg="white", activebackground="#66a3ff", command=lambda: press(6), height=2, width=4).grid(row=3, column=2)
    button7 = Button(root, text="7", bg="white", activebackground="#66a3ff", command=lambda: press(7), height=2, width=4).grid(row=2, column=0)
    button8 = Button(root, text="8", bg="white", activebackground="#66a3ff", command=lambda: press(8), height=2, width=4).grid(row=2, column=1)
    button9 = Button(root, text="9", bg="white", activebackground="#66a3ff", command=lambda: press(9), height=2, width=4).grid(row=2, column=2)
    button0 = Button(root, text="0", bg="white", activebackground="#66a3ff", command=lambda: press(0), height=2, width=9).grid(row=5, column=0, columnspan=2)
    # the operation buttons are created
    decimal_button = Button(root, text=".", bg="white", activebackground="#66a3ff", command=lambda: press("."), height=2, width=4).grid(row=5, column=2)
    plus_button = Button(root, text="+", bg="white", activebackground="#66a3ff", command=lambda: press("+"), height=2, width=4).grid(row=3, column=3)
    minus_button = Button(root, text="-", bg="white", activebackground="#66a3ff", command=lambda: press("-"), height=2, width=4).grid(row=2, column=3)
    multiply_button = Button(root, text="*", bg="white", activebackground="#66a3ff", command=lambda: press("*"), height=2, width=4).grid(row=3, column=4)
    divide_button = Button(root, text="/", bg="white", activebackground="#66a3ff", command=lambda: press("/"), height=2, width=4).grid(row=2, column=4)
    exponent_button = Button(root, text="^", bg="white", activebackground="#66a3ff", command=lambda: press("**"), height=2, width=4).grid(row=1, column=4)
    left_bracket_button = Button(root, text="(", bg="white", activebackground="#66a3ff", command=lambda: press("("), height=2, width=4).grid(row=1, column=2)
    right_bracket_button = Button(root, text=")", bg="white", activebackground="#66a3ff", command=lambda: press(")"), height=2, width=4).grid(row=1, column=3)
    ten_factor_button = Button(root, text="x10^X", bg="white", activebackground="#66a3ff", command=lambda: press("*10**"), height=2, width=4).grid(row=4, column=4)
    # the last function buttons are created
    equals_button = Button(root, text="=", bg="white", activebackground="#66a3ff", command=equalpress, height=5, width=4).grid(row=4, rowspan=2, column=3)
    clear_button = Button(root, text="AC", bg="white", activebackground="#66a3ff", command=clear, height=2, width=4).grid(row=1, column=0)
    delete_button = Button(root, text="del", bg="white", activebackground="#66a3ff", command=delete, height=2, width=4).grid(row=1, column=1)

    root.mainloop()