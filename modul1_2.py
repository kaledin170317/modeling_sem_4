import matplotlib
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

matplotlib.use('TkAgg')

mu_o = 4*np.pi*1e-7
def induction(l, N, S):
    return mu_o*N**2*S / l

def magnetic_induction(l, N, I):
    return mu_o*I*N / l

def do_plot_2(L,d,D):

    N = L // (np.pi * D)
    S = np.pi * (D / 2) ** 2
    l = np.linspace(d * N, 10 * d * N, 100)

    ax[0].clear()
    ax[1].clear()

    ax[0].plot(l, magnetic_induction(l, N, 1))
    ax[0].set_xlabel("длина катушки")
    ax[0].set_ylabel("Магнитная индукция")
    ax[0].grid()

    ax[1].plot(l, induction(l, N, S))
    ax[1].set_xlabel("длина катушки")
    ax[1].set_ylabel("Индуктивность катушки ")
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


Label(frame3, text="Длина провода :", font="Times 15", anchor="nw", width=30, ).pack()
Label(frame3, text="Диаметр провода", font="Times 15", anchor="nw", width=30, ).pack()
Label(frame3, text="Диаметр катушки", font="Times 15", anchor="nw", width=30, ).pack()


def checkFloat(value):
    try:
        float(value)
        return True
    except:
        return False

def check(*args):
    otv = ""
    if checkFloat(input_L.get()) == False:
        otv += f"Неправелтное значения для D: {input_L.get()}\n"
    if checkFloat(input_d.get()) == False:
        otv += f"Неправелтное значения для N: {input_d.get()}\n"
    if checkFloat(input_D.get()) == False:
        otv += f"Неправелтное значения для Ra: {input_D.get()}\n"
    result.set(otv)

result = StringVar()
input_L = StringVar(value="10")
input_d = StringVar(value="0.001")
input_D = StringVar(value="0.1")


check_label = Label(frame6,textvariable=result, foreground="red",)
check_label.pack(padx=5, pady=5, anchor=NW)

input_L.trace_add("write", check)
input_d.trace_add("write", check)
input_D.trace_add("write", check)

data_L = Entry(frame4, width=5, font='Times 15', textvariable=input_L)
data_d = Entry(frame4, width=5, font='Times 15', textvariable=input_d)
data_D = Entry(frame4, width=5, font='Times 15', textvariable=input_D)


padx = 1
pady = 1
data_L.pack(padx=padx, pady=pady)
data_d.pack(padx=padx, pady=pady)
data_D.pack(padx=padx, pady=pady)


def printInput():
    do_plot_2(
        float(data_L.get()),
        float(data_d.get()),
        float(data_D.get())
    )

printButton = Button(button, text="Построить графики", font='Times 20', command=printInput, )
printButton.pack(padx=45, pady=pady)


root.mainloop()

