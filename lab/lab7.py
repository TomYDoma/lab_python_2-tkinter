import tkinter as tk
from math import *
from tkinter.ttk import Treeview
import numpy as np
from PIL import ImageTk, Image

lab_window = tk.Tk()
lab_window.geometry("1000x600")
lab_window.title("Лабораторная работа № 7, выполнил студент: Дегтярева Е.Н.")
lab_window["bg"] = "#99BFBF"

def mathh():
    try:
        A = float(entry_a.get())
        B = float(entry_b.get())
        N = float(entry_n.get())
        E = float(entry_e.get())
        array = []
        move = (B - A) / N
        m = 0
        for x in np.arange(B, A - 0.5, -move):
            count = 0
            for n in range(0, 25):
                t = (pow(-1, n) * pow(x, n)) / factorial(n)
                count += t
                if fabs(t) < E:
                    break
            m += 1
            ab = (m, x, count)
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
        answer_one["text"] = "Неправильные входные данные"

frame_left = tk.Frame(lab_window, width=750, height=600)
frame_left["bg"] = "#BAFFFF"
frame_left.grid_propagate(0)
frame_right = tk.Frame(lab_window, width=250, height=600)
frame_right["bg"] = "#99BFBF"
frame_right.grid_propagate(0)

subject_label = tk.Label(frame_right,
                         text="Дисциплина: \n Интегрированные среды \n разработки программного \n обеспечения",
                         bg="#99BFBF", font=("Times New Roman", 15))
subject_label.grid(column=0, row=1, pady=100)
name_label = tk.Label(frame_right, text="Студент группы: \n 010304-КМСа-о19 \n Дегтярева Е.Н.", bg="#99BFBF",
                      font=("Times New Roman", 20))
name_label.grid(column=0, row=2, pady=10)

condition_label = tk.Label(frame_left, text="Вычисление суммы ряда с заданной точностью", bg="#BAFFFF",
                           font=("Times New Roman", 15))
label_a = tk.Label(frame_left, text="Введите a:", bg="#BAFFFF", font=("Times New Roman", 15))
entry_a = tk.Entry(frame_left, font=("Times New Roman", 12))

label_b = tk.Label(frame_left, text="Введите b:", bg="#BAFFFF", font=("Times New Roman", 15))
entry_b = tk.Entry(frame_left, font=("Times New Roman", 12))

label_n = tk.Label(frame_left, text="Введите n:", bg="#BAFFFF", font=("Times New Roman", 15))
entry_n = tk.Entry(frame_left, font=("Times New Roman", 12))

label_e = tk.Label(frame_left, text="Введите точность:", bg="#BAFFFF", font=("Times New Roman", 15))
entry_e = tk.Entry(frame_left, font=("Times New Roman", 12))

answer_one = tk.Label(frame_left, bg="#BAFFFF", font=("Times New Roman", 10))
button_launch = tk.Button(frame_left, text="Запуск", command=mathh, bg="#FFFFFF", font=("Arial", 20))

image_graf = Image.open("img/lab6.png")
frame_left.graf = ImageTk.PhotoImage(image_graf)
image_sprite = tk.Label(frame_left, image=frame_left.graf, bg="#BAFFFF")

condition_label.grid(column=0, row=0, pady=10)
image_sprite.grid(column=0, row=1)

label_a.grid(column=0, row=3, pady=10)
entry_a.grid(column=0, row=4, pady=20)

label_b.grid(column=0, row=5, pady=10)
entry_b.grid(column=0, row=6, pady=20)

label_n.grid(column=1, row=3, pady=10)
entry_n.grid(column=1, row=4, pady=20)

label_e.grid(column=1, row=5, pady=10)
entry_e.grid(column=1, row=6, pady=20)

answer_one.grid(column=0, row=8)
button_launch.grid(column=0, row=7)

frame_left.pack(side=tk.LEFT)
frame_right.pack(side=tk.RIGHT)

lab_window.mainloop()
