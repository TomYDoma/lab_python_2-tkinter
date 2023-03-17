import tkinter as tk
from math import*
from PIL import ImageTk, Image

lab_window = tk.Tk()
lab_window.geometry("1000x600")
lab_window.title("Лабораторная работа № 3, выполнил студент: Дегтярева Е.Н.")
lab_window["bg"] = "#99BFBF"


def mathh():
    try:
        x = float(entryX.get())
        y = float(entryY.get())
        r = float(entryR.get())

        if (x * x + y * y <= r * r and -r <= x <= 0 and 0 <= y <= r) \
                or (y >= -2 * x and 0 <= x <= r/2 and -r <= y <= 0) \
                or (y >= 2 * x - 20 and r/2 <= x <= r and -r <= y <= 0):
            answer["text"] = "Входит"
            answer["text"] = "Входит"
        else:
            answer["text"] = "Не входит"
            answer["text"] = "Не входит"


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


condition_label = tk.Label(frame_left, text="Проверка принадлежности точки\n заданной области на плоскости", bg="#BAFFFF", font=("Times New Roman", 15))
labelX = tk.Label(frame_left, text="Введите X:", bg="#BAFFFF", font=("Times New Roman", 15))
entryX = tk.Entry(frame_left, font=("Times New Roman", 12))

labelY = tk.Label(frame_left, text="Введите Y:", bg="#BAFFFF", font=("Times New Roman", 15))
entryY = tk.Entry(frame_left, font=("Times New Roman", 12))

labelR = tk.Label(frame_left, text="Введите R:", bg="#BAFFFF", font=("Times New Roman", 15))
entryR = tk.Entry(frame_left, font=("Times New Roman", 12))


answer = tk.Label(frame_left, bg="#BAFFFF", font=("Times New Roman", 10))
button_launch = tk.Button(frame_left, text="Запуск", command=mathh, bg="#FFFFFF", font=("Arial", 20))


image_graf = Image.open("img/lab3.png")
frame_left.graf = ImageTk.PhotoImage(image_graf)
image_sprite = tk.Label(frame_left, image=frame_left.graf, bg="#BAFFFF")


condition_label.grid(column=0, row=0, pady=10)
image_sprite.grid(column=0, row=1)
labelX.grid(column=0, row=3, pady=10)
entryX.grid(column=0, row=4, pady=20)
labelY.grid(column=1, row=3, pady=10)
entryY.grid(column=1, row=4, pady=20)
labelR.grid(column=2, row=3, pady=10)
entryR.grid(column=2, row=4, pady=20, padx=60)
answer.grid(column=0, row=6)
button_launch.grid(column=0, row=5)

frame_left.pack(side=tk.LEFT)
frame_right.pack(side=tk.RIGHT)

lab_window.mainloop()