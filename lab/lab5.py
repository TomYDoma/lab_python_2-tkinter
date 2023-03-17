import random
import tkinter as tk
from math import*
from PIL import ImageTk, Image

lab_window = tk.Tk()
lab_window.geometry("1000x600")
lab_window.title("Лабораторная работа № 5, выполнил студент: Дегтярева Е.Н.")
lab_window["bg"] = "#99BFBF"


def mathh():
    try:
        amount = int(entry_parameter.get())
        r = int(entryR.get())
        hit = 0
        miss = 0
        for i in range(amount):
            x = random.randrange(-r, r)
            y = random.randrange(-r, r)
            if (x * x + y * y <= r * r and -r <= x <= 0 and 0 <= y <= r) \
                    or (y >= -2 * x and 0 <= x <= r / 2 and -r <= y <= 0) \
                    or (y >= 2 * x - 20 and r / 2 <= x <= r and -r <= y <= 0):
                hit += 1
            else:
                miss += 1
        answer_one["text"] = "Количество попаданий: {} раз".format(hit)
        answer_two["text"] = "Количество промахов: {} раз".format(miss)

    except:
        answer_one["text"] = "Неправильные входные данные"

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


condition_label = tk.Label(frame_left, text="Проверка серии «выстрелов по мишени»", bg="#BAFFFF", font=("Times New Roman", 15))
label_parameter = tk.Label(frame_left, text="Введите количество выстрелов:", bg="#BAFFFF", font=("Times New Roman", 15))
entry_parameter = tk.Entry(frame_left, font=("Times New Roman", 12))

labelR = tk.Label(frame_left, text="Введите R:", bg="#BAFFFF", font=("Times New Roman", 15))
entryR = tk.Entry(frame_left, font=("Times New Roman", 12))

answer_one = tk.Label(frame_left, bg="#BAFFFF", font=("Times New Roman", 10))
answer_two = tk.Label(frame_left, bg="#BAFFFF", font=("Times New Roman", 10))
button_launch = tk.Button(frame_left, text="Запуск", command=mathh, bg="#FFFFFF", font=("Arial", 20))


image_graf = Image.open("img/lab3.png")
frame_left.graf = ImageTk.PhotoImage(image_graf)
image_sprite = tk.Label(frame_left, image=frame_left.graf, bg="#BAFFFF")


condition_label.grid(column=0, row=0, pady=10)
image_sprite.grid(column=0, row=1)
label_parameter.grid(column=0, row=3, pady=10)
entry_parameter.grid(column=0, row=4, pady=20)
labelR.grid(column=1, row=3, pady=10)
entryR.grid(column=1, row=4, pady=20)
answer_one.grid(column=0, row=6)
answer_two.grid(column=0, row=7)
button_launch.grid(column=0, row=5)
frame_left.pack(side=tk.LEFT)
frame_right.pack(side=tk.RIGHT)

lab_window.mainloop()