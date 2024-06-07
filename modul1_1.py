import math
import matplotlib
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

matplotlib.use('TkAgg')

mu_0 = 4 * np.pi * 10**-7
q = -1.602 * 10**-19
m = 9.109 * 10**-31

def magnetic_field(Ic, n):
   return mu_0 * n * Ic

def lorentz_force(v, Ic, n):
   B = magnetic_field(Ic,n)
   return q * v * B

def solve_current(Ra, Rk, U1, U2, n):
   R = (Ra - Rk)/2
   v = np.sqrt((2 *-1 *q * (U2 - U1)) / m)
   Ic = (2*m*v) / (q * R * n * mu_0)
   return Ic

def solenoid_current(U, Ra, Rk, n, mu_0):
   if U < 0 or (Ra - Rk) * n * mu_0 <= 0 or Ra <= Rk:
       return np.nan
   else:
       return -1* 2 * np.sqrt((2 * -q * U * m)) / ((Ra - Rk) * q * mu_0 * n)

def do_plot_2(Ra, Rk, U1, U2, n):

    ax[1].clear()
    ax[0].clear()

    U_values = np.linspace(0, U2, 100)

    Ic_values = [solenoid_current(U, Ra, Rk, n, mu_0) for U in U_values]
    Ic_circle = np.sqrt(2 * U_values / (Ra - Rk))

    Ic = solve_current(Ra, Rk, U1, U2, n)
    print("Current in solenoid (Ic):", Ic, "A")
    t = np.linspace(0, 2 * np.pi, 1000)
    v = np.sqrt((q * (U2 - U1)) / m)
    R = Ra - Rk
    x = R * np.cos(t)
    y = R * np.sin(t)
    ax[0].plot(x, y, label='Траектория')
    ax[0].set_xlabel('X (m)')
    ax[0].set_ylabel('Y (m)')
    ax[0].set_title('Траектория электрона в магнитном поле')
    ax[0].axis('equal')
    ax[0].legend()
    ax[0].grid()

    ax[1].plot(U_values, Ic_values, label='Ток через диод')
    ax[1].set_xlabel('Напряжение U')
    ax[1].fill_between(U_values, 0, Ic_values, color='lightblue', alpha=0.5)
    ax[1].set_ylabel('Ток через диод Ic')
    ax[1].set_title('Диаграмма зависимости тока через диод от напряжения')
    ax[1].legend()
    ax[1].grid()
    fig.tight_layout()

    canvas.draw()


root = Tk()
root.geometry('1250x700+10+10')

table = Frame(root)
table.place(x=0, y=0, width=700, height=700)

input = Frame(root)
input.place(x=700, y=5, width=350, height=700)

frame3 = Frame(input)
frame3.place(x=5, y=0, width=250, height=200)

frame4 = Frame(input)
frame4.place(x=250, y=0, width=100, height=200)

frame6 = Frame(input)
frame6.place(x=5, y=200, width=350, height=200)

button = Frame(input)
button.place(x=0, y=360, width=350, height=200)

figure = plt.figure(figsize=(5, 5))
fig, ax = plt.subplots(2)
fig.tight_layout()
canvas = FigureCanvasTkAgg(fig, table)
canvas.get_tk_widget().place(x=0, y=0, width=700, height=700)


Label(frame3, text="D :", font="Times 15", anchor="nw", width=30, ).pack()
Label(frame3, text="n:", font="Times 15", anchor="nw", width=30, ).pack()
Label(frame3, text="Ra:", font="Times 15", anchor="nw", width=30, ).pack()
Label(frame3, text="Rk :", font="Times 15", anchor="nw", width=30, ).pack()
Label(frame3, text="U1 :", font="Times 15", anchor="nw", width=30, ).pack()
Label(frame3, text="U2 :", font="Times 15", anchor="nw", width=30, ).pack()

def checkFloat(value):
    try:
        float(value)
        return True
    except:
        return False

def check(*args):
    otv = ""
    if checkFloat(input_D.get()) == False:
        otv += f"Неправелтное значения для D: {input_D.get()}\n"
    if checkFloat(input_n.get()) == False:
        otv += f"Неправелтное значения для N: {input_n.get()}\n"
    if checkFloat(input_Ra.get()) == False:
        otv += f"Неправелтное значения для Ra: {input_Ra.get()}\n"
    if checkFloat(input_Rk.get()) == False:
        otv += f"Неправелтное значения для Rk: {input_Rk.get()}\n"
    if checkFloat(input_U1.get()) == False:
        otv += f"Неправелтное значения для U1: {input_U1.get()}\n"
    if checkFloat(input_U2.get()) == False:
        otv += f"Неправелтное значения для U2: {input_U2.get()}\n"
    result.set(otv)

result = StringVar()
input_D = StringVar(value="0.01")
input_n = StringVar(value="100")
input_Ra = StringVar(value="0.005")
input_Rk = StringVar(value="0.004")
input_U1 = StringVar(value="1000")
input_U2 = StringVar(value="2000")

check_label = Label(frame6,textvariable=result, foreground="red",)
check_label.pack(padx=5, pady=5, anchor=NW)

input_D.trace_add("write", check)
input_n.trace_add("write", check)
input_Ra.trace_add("write", check)
input_Rk.trace_add("write", check)
input_U1.trace_add("write", check)
input_U2.trace_add("write", check)

data_D = Entry(frame4, width=5, font='Times 15', textvariable=input_D)
data_n = Entry(frame4, width=5, font='Times 15', textvariable=input_n)
data_Ra = Entry(frame4, width=5, font='Times 15', textvariable=input_Ra)
data_Rk = Entry(frame4, width=5, font='Times 15', textvariable=input_Rk)
data_U1 = Entry(frame4, width=5, font='Times 15', textvariable=input_U1)
data_U2 = Entry(frame4, width=5, font='Times 15', textvariable=input_U2)

padx = 1
pady = 1
data_D.pack(padx=padx, pady=pady)
data_n.pack(padx=padx, pady=pady)
data_Ra.pack(padx=padx, pady=pady)
data_Rk.pack(padx=padx, pady=pady)
data_U1.pack(padx=padx, pady=pady)
data_U2.pack(padx=padx, pady=pady)


def printInput():
    do_plot_2(
        float(data_Ra.get()),
        float(data_Rk.get()),
        float(data_U1.get()),
        float(data_U2.get()),
        float(data_n.get())
    )

printButton = Button(button, text="Построить графики", font='Times 20', command=printInput, )
printButton.pack(padx=45, pady=pady)


root.mainloop()

