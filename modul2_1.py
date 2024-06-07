import matplotlib
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

matplotlib.use('TkAgg')

colormap = [[6, 1, 31], [12, 0, 40], [14, 0, 51], [16, 1, 60],
            [17, 1, 76], [23, 0, 90], [26, 1, 105], [28, 0, 119], [28, 0, 136],
            [34, 0, 151], [36, 1, 165], [37, 0, 176], [37, 1, 187], [36, 0, 194],
            [37, 0, 202], [34, 0, 209], [31, 0, 217], [28, 1, 220], [25, 0, 224],
            [18, 1, 227], [16, 0, 229], [14, 0, 233], [10, 0, 237], [9, 0, 237],
            [7, 0, 240], [3, 0, 242], [0, 0, 244], [0, 0, 244], [2, 5, 244],
            [1, 8, 244], [0, 13, 242], [0, 18, 242], [2, 22, 239],
            [0, 28, 236], [0, 33, 236], [0, 37, 232], [0, 44, 229], [2, 49, 227],
            [0, 55, 220], [0, 60, 218], [0, 66, 214], [1, 73, 209], [0, 77, 205],
            [0, 84, 200], [0, 91, 194], [0, 96, 193], [0, 101, 189], [0, 106, 182],
            [0, 111, 177], [1, 118, 172], [0, 120, 165], [0, 122, 159],
            [0, 128, 153], [1, 131, 147], [1, 132, 140], [1, 135, 134],
            [0, 140, 131], [0, 145, 126], [0, 148, 124], [0, 152, 122],
            [0, 158, 118], [1, 162, 118], [1, 168, 116], [0, 172, 114],
            [0, 178, 113], [0, 182, 112], [0, 186, 111], [1, 188, 109],
            [2, 191, 107], [0, 194, 107], [1, 195, 108], [0, 198, 101],
            [1, 200, 99], [0, 204, 96], [1, 209, 97], [2, 211, 94], [1, 217, 90],
            [0, 220, 88], [0, 225, 81], [1, 228, 77], [1, 231, 71], [1, 232, 68],
            [0, 230, 60], [0, 230, 52], [0, 230, 43], [0, 230, 33], [0, 228, 21],
            [0, 228, 11], [2, 229, 0], [16, 229, 0], [28, 229, 0], [40, 230, 0],
            [56, 232, 0], [72, 232, 2], [84, 230, 1],
            [98, 231, 0], [111, 230, 0], [124, 230, 0], [137, 230, 1], [151, 228, 0],
            [162, 227, 0], [173, 229, 0], [186, 227, 0], [198, 224, 1],
            [211, 226, 0], [221, 221, 0], [227, 216, 0], [230, 210, 1],
            [237, 201, 1], [240, 193, 1], [242, 184, 0], [245, 173, 0],
            [248, 165, 1], [250, 155, 0], [251, 145, 0], [252, 136, 1],
            [254, 126, 1], [255, 115, 0], [255, 104, 3], [254, 95, 1], [255, 83, 1],
            [255, 72, 2], [255, 61, 0], [253, 49, 0], [255, 39, 2],
            [253, 28, 0], [255, 17, 4], [255, 8, 1], [254, 2, 1], [254, 0, 10],
            [255, 0, 14], [255, 0, 18], [251, 0, 24], [250, 0, 30], [250, 0, 30],
            [248, 0, 35], [246, 0, 41], [246, 0, 41], [242, 0, 40], [242, 0, 40],
            [240, 0, 45], [237, 0, 46], [233, 0, 45], [230, 1, 44], [226, 0, 42],
            [222, 0, 41], [218, 0, 39], [214, 0, 38], [206, 0, 36], [200, 1, 34],
            [195, 0, 32], [189, 0, 30], [185, 0, 31], [177, 0, 28], [169, 0, 26],
            [162, 0, 24], [152, 0, 23], [144, 1, 21], [136, 1, 18], [128, 1, 20],
            [121, 0, 19], [111, 0, 16], [104, 0, 14], [96, 0, 12], [88, 1, 10],
            [83, 0, 12], [73, 0, 9], [67, 0, 9], [62, 1, 9], [57, 0, 7], [51, 0, 7],
            [46, 0, 5], [42, 0, 4], [39, 0, 5], [33, 1, 4], [30, 0, 4], [25, 0, 3],
            [25, 0, 3], [22, 0, 2], [21, 0, 1], [16, 0, 0], [15, 1, 1], [14, 0, 0],
            [12, 0, 0], [9, 0, 1], [9, 0, 1], [8, 0, 0]]


screen_width = 0.05  # Width of the screen in meters
screen_resolution = 1000  # Number of points on the screen


def do_plot_2(N, slit_width, slit_period, distance, wavelength_center, wavelength_width):

    x, intensity, rgb = intensity_pattern(N, slit_width, slit_period, distance, wavelength_center, wavelength_width,
                                          screen_width, screen_resolution)
    ax[0].clear()
    ax[1].clear()

    ax[0].imshow(rgb[np.newaxis, :, :], aspect='auto', extent=[x.min(), x.max(), 0, 1])
    ax[0].set_title('Цветное распределение интенсивности')
    ax[0].axis('off')

    ax[1].plot(x, intensity, color='black', label='Ток')
    ax[1].set_title('Интенсивность на экране')
    ax[1].set_xlabel('Координата x ')
    ax[1].set_ylabel('Интенсивность')
    ax[1].grid(True)

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
button.place(x=0, y=360, width=350, height=60)

figure = plt.figure(figsize=(5, 5))
fig, ax = plt.subplots(2)
fig.tight_layout()
canvas = FigureCanvasTkAgg(fig, table)
canvas.get_tk_widget().place(x=0, y=0, width=700, height=700)

Label(frame3, text="N :", font="Times 15", anchor="nw", width=30, ).pack()
Label(frame3, text="Ширина:", font="Times 15", anchor="nw", width=30, ).pack()
Label(frame3, text="Растояние между щелями:", font="Times 15", anchor="nw", width=30, ).pack()
Label(frame3, text="Растояние :", font="Times 15", anchor="nw", width=30, ).pack()
Label(frame3, text="Длина спектора :", font="Times 15", anchor="nw", width=30, ).pack()
Label(frame3, text="Ширина спектора :", font="Times 15", anchor="nw", width=30, ).pack()


def checkFloat(value):
    try:
        float(value)
        return True
    except:
        return False

def check(*args):
    otv = ""
    if checkFloat(input_N.get()) == False:
        otv += f"Неправелтное значения для N X: {input_N.get()}\n"
    if checkFloat(input_width.get()) == False:
        otv += f"Неправелтное значения для Ширины Y: {input_width.get()}\n"
    if checkFloat(input_period.get()) == False:
        otv += f"Неправелтное значения для Растояния между щелями : {input_period.get()}\n"
    if checkFloat(input_distance.get()) == False:
        otv += f"Неправелтное значения для Растояния: {input_distance.get()}\n"
    if checkFloat(input_wavelength.get()) == False:
        otv += f"Неправелтное значения для Длины спектора: {input_wavelength.get()}\n"
    if checkFloat(input_wavelength_width.get()) == False:
        otv += f"Неправелтное значения для Ширины спектора: {input_wavelength_width.get()}\n"
    result.set(otv)


result = StringVar()
input_N = StringVar(value="5")
input_width = StringVar(value="0.00001")
input_period = StringVar(value="0.0005")
input_distance = StringVar(value="1")
input_wavelength = StringVar(value="500")
input_wavelength_width = StringVar(value="100")

check_label = Label(frame6, textvariable=result, foreground="red", )
check_label.pack(padx=5, pady=5, anchor=NW)

input_N.trace_add("write", check)
input_width.trace_add("write", check)
input_period.trace_add("write", check)
input_distance.trace_add("write", check)
input_wavelength.trace_add("write", check)
input_wavelength_width.trace_add("write", check)

data_N = Entry(frame4, width=5, font='Times 15', textvariable=input_N)
data_width = Entry(frame4, width=10, font='Times 15', textvariable=input_width)
data_period = Entry(frame4, width=10, font='Times 15', textvariable=input_period)
data_distance = Entry(frame4, width=5, font='Times 15', textvariable=input_distance)
data_wavelength = Entry(frame4, width=5, font='Times 15', textvariable=input_wavelength)
data_wavelength_width = Entry(frame4, width=5, font='Times 15', textvariable=input_wavelength_width)

padx = 1
pady = 1
data_N.pack(padx=padx, pady=pady)
data_width.pack(padx=padx, pady=pady)
data_period.pack(padx=padx, pady=pady)
data_distance.pack(padx=padx, pady=pady)
data_wavelength.pack(padx=padx, pady=pady)
data_wavelength_width.pack(padx=padx, pady=pady)


def printInput():
    do_plot_2(
        int(data_N.get()),
        float(data_width.get()),
        float(data_period.get()),
        float(data_distance.get()),
        float(data_wavelength.get()) * 10**(-9),
        float(data_wavelength_width.get()) * 10**(-9)
    )


printButton = Button(button, text="Расчет", font='Times 40', command=printInput, )
printButton.pack(padx=45, pady=pady)


def wavelength_to_rgb(wavelength):
    a = np.linspace(400, 700, len(colormap))
    colorindex = min(range(len(a)), key=lambda i: abs(a[i] - wavelength))
    col = colormap[colorindex]
    return np.asarray(col)



def intensity_for_wavelength(wavelength, N, slit_width, slit_period, distance):

    x = np.linspace(-screen_width / 2, screen_width / 2, screen_resolution)
    k = 2 * np.pi / wavelength
    beta = k * slit_width / 2 * np.sin(np.arctan(x / distance))
    beta = np.where(beta == 0, 1e-10, beta)  # чтобы избежать деления на 0
    single_slit = (np.sin(beta) / beta) ** 2  # интенсивность для одной щели
    total_field = np.zeros_like(x, dtype=complex)
    for n in range(N):  # рассчет суммарного поля от N щелей (интерференция)
        alpha = k * (n - (N - 1) / 2) * slit_period * np.sin(np.arctan(x / distance))
        total_field += single_slit * np.exp(1j * alpha)
    intensity = np.abs(total_field) ** 2
    return intensity / np.max(intensity)
def intensity_pattern(N, slit_width, slit_period, distance, wavelength_center, wavelength_width, screen_width,
                      screen_resolution):
    x = np.linspace(-screen_width / 2, screen_width / 2, screen_resolution)

    wavelengths = np.linspace(wavelength_center - wavelength_width / 2, wavelength_center + wavelength_width / 2, 100)
    intensities = np.array([intensity_for_wavelength(wl,N, slit_width, slit_period, distance) for wl in wavelengths])
    intensity = np.mean(intensities, axis=0)
    intensity /= np.max(intensity)

    colors = np.zeros((screen_resolution, 3))
    for i, wl in enumerate(wavelengths):
        rgb = np.array(wavelength_to_rgb(wl * 1e9)) / 255
        colors += np.outer(intensity_for_wavelength(wl,N, slit_width, slit_period, distance), rgb)
    colors /= len(wavelengths)

    return x, intensity, colors


root.mainloop()
