import tkinter as tk
from math import*
from PIL import ImageTk, Image

lab_window = tk.Tk()
lab_window.geometry("1000x600")
lab_window.title("Лабораторная работа № 2, выполнил студент: Дегтярева Е.Н.")
lab_window["bg"] = "#99BFBF"


def mathh():
    try:
        x = float(entryX.get())
        if x < -8:
            y = -3
            answer["text"] = str(y)
        elif -8 <= x <= -3:
            y = 0.6 * x + 1.8
            answer["text"] = str(round(y, 3))
        elif -3 < x < 3:
            y = -sqrt(pow(3, 2) - pow(x, 2))
            answer["text"] = str(round(y, 3))
        elif 3 <= x < 5:
            y = x - 3
            answer["text"] = str(y)
        elif x >= 5:
            y = 3
            answer["text"] = str(y)


    except:
        answer["text"] = "Ввод некоректен"



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


condition_label = tk.Label(frame_left, text="Вычисление значения функции, \n заданной ее графиком", bg="#BAFFFF", font=("Times New Roman", 15))
labelX = tk.Label(frame_left, text="Введите X:", bg="#BAFFFF", font=("Times New Roman", 15))
entryX = tk.Entry(frame_left, font=("Times New Roman", 15))


answer = tk.Label(frame_left, bg="#BAFFFF", font=("Times New Roman", 15))
button_launch = tk.Button(frame_left, text="Запуск", command=mathh, bg="#FFFFFF", font=("Arial", 20))


image_graf = Image.open("img/lab2.png")
frame_left.graf = ImageTk.PhotoImage(image_graf)
image_sprite = tk.Label(frame_left, image=frame_left.graf, bg="#BAFFFF")


condition_label.grid(column=0, row=0, pady=50)
image_sprite.grid(column=0, row=1)
labelX.grid(column=0, row=3, pady=20)
entryX.grid(column=0, row=4, pady=20)
answer.grid(column=0, row=6)
button_launch.grid(column=0, row=5)

frame_left.pack(side=tk.LEFT)
frame_right.pack(side=tk.RIGHT)

lab_window.mainloop()