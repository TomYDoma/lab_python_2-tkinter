import tkinter as tk
from math import*
import numpy as np
from tkinter.ttk import Treeview

from PIL import ImageTk, Image

lab_window = tk.Tk()
lab_window.geometry("1000x600")
lab_window.title("Лабораторная работа № 4, выполнил студент: Дегтярева Е.Н.")
lab_window["bg"] = "#99BFBF"


def mathh():
    try:
        a = int(entryA.get())
        b = int(entryB.get())
        N = int(entryN.get())
        array = []
        move = (b - a) / N
        m = 0
        for x in np.arange(b, a - 0.5, -move):
            m += 1
            if x < -8:
                y = -3
                ab = (m, x, y)
                array.append(ab)
            elif -8 <= x < -3:
                y = 0.6 * x + 1.8
                ab = (m, x, y)
                array.append(ab)
            elif x == -3:
                y = 0
                ab = (m, x, y)
                array.append(ab)
            elif -3 < x < 3:
                y = -sqrt(pow(3, 2) - pow(x, 2))
                ab = (m, x, y)
                array.append(ab)
            elif 3 <= x < 5:
                y = x - 3
                ab = (m, x, y)
                array.append(ab)
            elif x >= 5:
                y = 3
                ab = (m, x, y)
                array.append(ab)

        WindowTREE = tk.Toplevel(lab_window)
        columns = ("n", "x", "y")

        treeAB = Treeview(WindowTREE, columns=columns, show="headings")
        treeAB.grid(column=1, row=2)

        treeAB.heading("n", text="N")
        treeAB.heading("x", text="X")
        treeAB.heading("y", text="Y")

        treeAB.column("#1", width=70)
        treeAB.column("#2", width=70)
        treeAB.column("#3", width=70)

        for i in array:
            treeAB.insert(parent='', index='end', values=i)

    except:
        answer["text"] = "Неправильные входные данные"

frame_left = tk.Frame(lab_window, width=750, height=600)
frame_left["bg"] = "#BAFFFF"
frame_left.grid_propagate(0)
frame_right = tk.Frame(lab_window, width=250, height=600)
frame_right["bg"] = "#99BFBF"
frame_right.grid_propagate(0)

subject_label = tk.Label(frame_right, text="Дисциплина: \n Интегрированные среды \n разработки программного \n обеспечения", bg="#99BFBF", font=("Times New Roman", 15))
subject_label.grid(column=0, row=1, pady=100)
name_label = tk.Label(frame_right, text="Студент группы: \n 010304-КМСа-о19 \n Дегтярева Е.Н.", bg="#99BFBF", font=("Times New Roman", 20))
name_label.grid(column=0, row=2, pady=10)

condition_label = tk.Label(frame_left, text="Вывод таблицы значений функции, \n заданной её графиком", bg="#BAFFFF", font=("Times New Roman", 15))
labelA = tk.Label(frame_left, text="Введите a:", bg="#BAFFFF", font=("Times New Roman", 15))
entryA = tk.Entry(frame_left, font=("Times New Roman", 12))

labelB = tk.Label(frame_left, text="Введите b:", bg="#BAFFFF", font=("Times New Roman", 15))
entryB = tk.Entry(frame_left, font=("Times New Roman", 12))

labelN = tk.Label(frame_left, text="Введите N:", bg="#BAFFFF", font=("Times New Roman", 15))
entryN = tk.Entry(frame_left, font=("Times New Roman", 12))

answer = tk.Label(frame_left, bg="#BAFFFF", font=("Times New Roman", 10))
button_launch = tk.Button(frame_left, text="Запуск", command=mathh, bg="#FFFFFF", font=("Arial", 20))

image_graf = Image.open("img/lab2.png")
image_graf = image_graf.resize((300, 120))
frame_left.graf = ImageTk.PhotoImage(image_graf)
image_sprite = tk.Label(frame_left, image=frame_left.graf, bg="#BAFFFF")


condition_label.grid(column=0, row=0, pady=10)
image_sprite.grid(column=0, row=1)
labelA.grid(column=0, row=3, pady=10)
entryA.grid(column=0, row=4, pady=20)
labelB.grid(column=1, row=3, pady=10)
entryB.grid(column=1, row=4, pady=20)
labelN.grid(column=2, row=3, pady=10)
entryN.grid(column=2, row=4, pady=20, padx=60)
answer.grid(column=0, row=6)
button_launch.grid(column=0, row=5)

frame_left.pack(side=tk.LEFT)
frame_right.pack(side=tk.RIGHT)

lab_window.mainloop()