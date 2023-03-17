import tkinter as tk
from math import*
from PIL import ImageTk, Image

lab_window = tk.Tk()
lab_window.title("Лабораторная работа № 1, выполнил студент: Дегтярева Е.Н.")
lab_window.geometry("1000x600")
lab_window["bg"] = "#99BFBF"

def mathh():
    try:
        a = float(entry_a.get())
        z1 = cos(a) + sin(a) + cos(3 * a) + sin(3 * a)
        z2 = 2 * sqrt(2) * cos(a) * sin(pi / 4 + 2 * a)
        answer_one["text"] = "z1 = " + str(round(z1, 3))
        answer_two["text"] = "z2 = " + str(round(z2, 3))
    except:
        answer_one["text"] = "Неправильные входные данные"



frame_left = tk.Frame(lab_window, width=750, height=600)
frame_left["bg"] = "#BAFFFF"
frame_left.grid_propagate(0)
frame_right = tk.Frame(lab_window, width=250, height=600)
frame_right["bg"] = "#99BFBF"
frame_right.grid_propagate(0)
label_subject = tk.Label(frame_right, text="Дисциплина: \n Интегрированные среды \n разработки программного \n обеспечения", bg="#99BFBF", font=("Times New Roman", 15))
label_subject.grid(column=0, row=1, pady=100)
label_name = tk.Label(frame_right, text="Студент группы: \n 010304-КМСа-о19 \n Дегтярева Е.Н.", bg="#99BFBF", font=("Times New Roman", 20))
label_name.grid(column=0, row=2, pady=10)


label_condition = tk.Label(frame_left, text="Вычисление значений z1 и z2", bg="#BAFFFF", font=("Times New Roman", 15))
label_a = tk.Label(frame_left, text="Введите a:", bg="#BAFFFF", font=("Times New Roman", 15))
entry_a = tk.Entry(frame_left, font=("Times New Roman", 15))
answer_one = tk.Label(frame_left, bg="#BAFFFF", font=("Times New Roman", 15))
answer_two = tk.Label(frame_left, bg="#BAFFFF", font=("Times New Roman", 15))
button_launch = tk.Button(frame_left, text="Запуск", command=mathh, bg="#FFFFFF", font=("Arial", 20))


image_one = Image.open("img/lab1_z1.png")
frame_left.image = ImageTk.PhotoImage(image_one)
image_sprite = tk.Label(frame_left, image=frame_left.image, bg="#BAFFFF")


image_two = Image.open("img/lab1_z2.png")
frame_left.image1 = ImageTk.PhotoImage(image_two)
image_sprite1 = tk.Label(frame_left, image=frame_left.image1, bg="#BAFFFF")


label_condition.grid(column=0, row=0, pady=50)
image_sprite.grid(column=0, row=1)
image_sprite1.grid(column=0, row=2)
label_a.grid(column=0, row=3, pady=20)
entry_a.grid(column=0, row=4, pady=20)
answer_one.grid(column=0, row=6)
answer_two.grid(column=0, row=7)
button_launch.grid(column=0, row=5)

frame_left.pack(side=tk.LEFT)
frame_right.pack(side=tk.RIGHT)

lab_window.mainloop()