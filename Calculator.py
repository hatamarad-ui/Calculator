from customtkinter import *

root = CTk()
root.title("Calculator")
root.geometry("360x500")
equation = StringVar()
root.configure(background="white")
root.resizable(width=False, height=False)
root.grid_columnconfigure((0,1,2,3,4), weight=1)
root.grid_rowconfigure((0,1,2,3,4,5), weight=1)

# ----------------------------------- Functions -----------------------------------------------------
# Python --> input() | tkinter --> get()
# Python --> print() | tkinter --> set()

def key_press(event):
    key = event.keysym

    if key.isdigit():
        set_number(key)

    elif key in ("plus", "KP_Add"):
        check_sign("+")

    elif key in ("minus", "KP_Subtract"):
        check_sign("-")

    elif key in ("asterisk", "KP_Multiply"):
        check_sign("*")

    elif key in ("slash", "KP_Divide"):
        check_sign("/")

    elif key in ("period", "KP_Decimal"):
        set_number(".")

    elif key in ("Return", "KP_Enter"):
        calc_equal()

    elif key == "Escape":
        equation.set("")


def set_number(num):
    equation.set(equation.get() + num)


def calc_equal():
    text = equation.get()
    if text and text[-1] in "+-*/√xx²":
        text = text[:-1]
    result = eval(text)
    equation.set(result)



def check_sign(new_sign):
    x = equation.get()[-1]
    if x == "+" or x == "-" or x == "*" or x == "/" or x == "x²" or x == "√x":
        equation.set(equation.get()[:-1])
        equation.set(equation.get() + new_sign)
    else:
        equation.set(equation.get() + new_sign)

def plus_minus():
    text = equation.get()
    if text == "":
        return
    num = float(text)
    num *= -1
    if num.is_integer():
        equation.set(str(int(num)))
    else:
        equation.set(str(num))

# ----------------------------------- Create Label -----------------------------------------------------

h = CTkLabel(root,
          textvariable=equation,
          font=("Tahoma", 20, "bold"),
          pady=30, anchor="center")
h.grid(column=0, row=0, columnspan=5, sticky="nsew", padx=10, pady=10)

# ----------------------------------- Create Buttons ---------------------------------------------------

btn1 = CTkButton(root,
              text="1", font=("Arial", 15, "bold"),
              width=80, height=70,
              fg_color="#37323E", hover_color="#B1C9DC",
              command=lambda: set_number("1"))
btn1.grid(column=1, row=4, sticky="nsew")

btn2 = CTkButton(root,
              text="2", font=("Arial", 15, "bold"),
              width=80, height=70,
              fg_color="#37323E", hover_color="#B1C9DC",
              command=lambda: set_number("2"))
btn2.grid(column=2, row=4, sticky="nsew")

btn3 = CTkButton(root,
              text="3", font=("Arial", 15, "bold"),
              width=80, height=70,
              fg_color="#37323E", hover_color="#B1C9DC",
              command=lambda: set_number("3"))
btn3.grid(column=3, row=4, sticky="nsew")

btn_plus = CTkButton(root,
                  text="+", font=("Arial", 15, "bold"),
                  width=100, height=70,
                  fg_color="#37323E", hover_color="#B1C9DC",
                  command=lambda: check_sign("+"))
btn_plus.grid(column=4, row=4, sticky="nsew")

btn4 = CTkButton(root,
              text="4", font=("Arial", 15, "bold"),
              width=80, height=70,
              fg_color="#37323E", hover_color="#B1C9DC",
              command=lambda: set_number("4"))
btn4.grid(column=1, row=3, sticky="nsew")

btn5 = CTkButton(root,
              text="5", font=("Arial", 15, "bold"),
              width=80, height=70,
              fg_color="#37323E", hover_color="#B1C9DC",
              command=lambda: set_number("5"))
btn5.grid(column=2, row=3, sticky="nsew")

btn6 = CTkButton(root,
              text="6", font=("Arial", 15, "bold"),
              width=80, height=70,
              fg_color="#37323E", hover_color="#B1C9DC",
              command=lambda: set_number("6"))
btn6.grid(column=3, row=3, sticky="nsew")

btn_minus = CTkButton(root,
                   text="-", font=("Arial", 15, "bold"),
                   width=100, height=70,
                   fg_color="#37323E", hover_color="#B1C9DC",
                   command=lambda: check_sign("-"))
btn_minus.grid(column=4, row=3, sticky="nsew")

btn7 = CTkButton(root,
              text="7", font=("Arial", 15, "bold"),
              width=80, height=70,
              fg_color="#37323E", hover_color="#B1C9DC",
              command=lambda: set_number("7"))
btn7.grid(column=1, row=2, sticky="nsew")

btn8 = CTkButton(root,
              text="8", font=("Arial", 15, "bold"),
              width=80, height=70,
              fg_color="#37323E", hover_color="#B1C9DC",
              command=lambda: set_number("8"))
btn8.grid(column=2, row=2, sticky="nsew")

btn9 = CTkButton(root,
              text="9", font=("Arial", 15, "bold"),
              width=80, height=70,
              fg_color="#37323E", hover_color="#B1C9DC",
              command=lambda: set_number("9"))
btn9.grid(column=3, row=2, sticky="nsew")

btn_multiply = CTkButton(root,
                      text="x", font=("Arial", 15, "bold"),
                      width=100, height=70,
                      fg_color="#37323E", hover_color="#B1C9DC",
                      command=lambda: check_sign("*"))
btn_multiply.grid(column=4, row=2, sticky="nsew")

btn_plus_minus = CTkButton(root,
                        text="+/-", font=("Arial", 15, "bold"),
                        width=80, height=70,
                        fg_color="#37323E", hover_color="#B1C9DC",
                        command=lambda: plus_minus())
btn_plus_minus.grid(column=1, row=5, sticky="nsew")

btn0 = CTkButton(root,
              text="0", font=("Arial", 15, "bold"),
              width=80, height=70,
              fg_color="#37323E", hover_color="#B1C9DC",
              command=lambda: set_number("0"))
btn0.grid(column=2, row=5, sticky="nsew")

btn_dot = CTkButton(root,
                 text=".", font=("Arial", 15, "bold"),
                 width=80, height=70,
                 fg_color="#37323E", hover_color="#B1C9DC",
                 command=lambda: set_number("."))
btn_dot.grid(column=3, row=5, sticky="nsew")

btn_equal = CTkButton(root,
                   text="=", font=("Arial", 15, "bold"),
                   width=100, height=70,
                   fg_color="#A4C3FF", hover_color="#B1C9DC",
                   text_color="#37323E",
                   command=lambda: calc_equal())
btn_equal.grid(column=4, row=5, sticky="nsew")

btn_square = CTkButton(root,
                    text="x²", font=("Arial", 15, "bold"),
                    width=80, height=70,
                    fg_color="#37323E", hover_color="#B1C9DC",
                    command=lambda: check_sign("**2"))
btn_square.grid(column=1, row=1, sticky="nsew")

btn_square_root = CTkButton(root,
                         text="√x", font=("Arial", 15, "bold"),
                         width=80, height=70,
                         fg_color="#37323E", hover_color="#B1C9DC",
                         command=lambda: check_sign("**0.5"))
btn_square_root.grid(column=2, row=1, sticky="nsew")

btn_divide = CTkButton(root,
                    text="/", font=("Arial", 15, "bold"),
                    width=80, height=70,
                    fg_color="#37323E", hover_color="#B1C9DC",
                    command=lambda: check_sign("/"))
btn_divide.grid(column=3, row=1, sticky="nsew")

btn_clear = CTkButton(root,
                   text="C", font=("Arial", 15, "bold"),
                   width=100, height=70,
                   fg_color="#A4C3FF", hover_color="#B1C9DC",
                   text_color="#37323E",
                   command=lambda: equation.set(""))
btn_clear.grid(column=4, row=1, sticky="nsew")

root.bind("<Key>", key_press)

root.mainloop()
