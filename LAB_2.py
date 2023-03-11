import tkinter as tk
from math import*

window_lab = tk.Tk()
window_lab.title("Студент: Маноцков Е.С. ЛР №3 ")
window_lab.geometry("400x400")
window_lab.resizable(width=False, height=False)
window_lab["bg"] = "#83DA8B"

def add():
    label_otvet.config(text="")
    try:
        x = float(entry_x.get())

        if x < -10:
            y = -2
            label_otvet["text"] = str(y)
        elif -10 <= x <= -6:
            y = sqrt(4 - pow(x+8, 2)) - 2
            label_otvet["text"] = str(y)
        elif -6 < x <= 2:
            y = 0.5 * x + 1
            label_otvet["text"] = str(y)
        elif 2 < x <= 6:
            y = 0
            label_otvet["text"] = str(y)
        elif x > 6:
            y = pow(x-6, 2)
            label_otvet["text"] = str(y)


    except:
        label_otvet["text"] = "Неправильные входные данные"


frame_for_window = tk.Frame(window_lab)
frame_for_window["bg"] = "#83DA8B"

label_x = tk.Label(frame_for_window, text="Вычисление значения функции в точке X \n Введите X:", bg="#83DA8B", font=("Times New Roman", 15))
entry_x = tk.Entry(frame_for_window, font=("Times New Roman", 15))
btn_run = tk.Button(frame_for_window, text="Запуск", command=add, bg="#FFFFFF", font=("Times New Roman", 20))
label_y = tk.Label(frame_for_window, text="Значение функции будет равно:", bg="#83DA8B", font=("Times New Roman", 15))
label_otvet = tk.Label(frame_for_window, bg="#83DA8B", font=("Times New Roman", 15))

entry_x.grid(column=1, row=3, pady=30)
label_x.grid(column=1, row=2)
btn_run.grid(column=1, row=6)
label_y.grid(column=1, row=7, pady=30)
label_otvet.grid(column=1, row=8)

frame_for_window.pack()
window_lab.mainloop()
