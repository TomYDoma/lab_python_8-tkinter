import tkinter as tk
from math import fabs, pi
from tkinter.ttk import Treeview
import numpy as np

window_lab = tk.Tk()
window_lab.title("Студент: Маноцков Е.С. ЛР №7 ")
window_lab.geometry("400x400")
window_lab.resizable(width=False, height=False)
window_lab["bg"] = "#83DA8B"

def add():
    label_otvet.config(text="")

    try:
        number = []
        a = float(entry_a.get())
        b = float(entry_b.get())
        nn = float(entry_n.get())
        e = float(entry_e.get())

        k = (b - a) / nn
        m = 0
        for x in np.arange(b, a - 0.5, -k):
            count = 0
            t = 0
            for n in range(0, 25):
                t = pow(-1, n + 1) / ((2 * n + 1) * pow(x, 2 * n + 1))
                count += t
                if fabs(t) < e:
                    break
            m += 1
            count += pi / 2
            ab = (m, x, count)
            number.append(ab)

        newWindow = tk.Toplevel(window_lab)
        # определяем столбцы
        columns = ("n", "x", "y")

        tree = Treeview(newWindow, columns=columns, show="headings")
        tree.grid(column=1, row=2)

        # определяем заголовки
        tree.heading("n", text="N")
        tree.heading("x", text="X")
        tree.heading("y", text="Y")

        tree.column("#1", width=70)
        tree.column("#2", width=70)
        tree.column("#3", width=70)

        # добавляем данные
        for i in number:
            tree.insert(parent='', index='end', values=i)

    except:
        label_otvet["text"] = "Неправильные входные данные"



frame_for_window = tk.Frame(window_lab)
frame_for_window["bg"] = "#83DA8B"

label_a = tk.Label(frame_for_window, text="Вычисление суммы ряда Тейлора \n Введите a:", bg="#83DA8B", font=("Times New Roman", 15))
entry_a = tk.Entry(frame_for_window, font=("Times New Roman", 15))
label_b = tk.Label(frame_for_window, text="Введите b:", bg="#83DA8B", font=("Times New Roman", 15))
entry_b = tk.Entry(frame_for_window, font=("Times New Roman", 15))
label_e = tk.Label(frame_for_window, text="Введите точность e:", bg="#83DA8B", font=("Times New Roman", 15))
entry_e = tk.Entry(frame_for_window, font=("Times New Roman", 15))
label_n = tk.Label(frame_for_window, text="Введите n:", bg="#83DA8B", font=("Times New Roman", 15))
entry_n = tk.Entry(frame_for_window, font=("Times New Roman", 15))
btn_run = tk.Button(frame_for_window, text="Запуск", command=add, bg="#FFFFFF", font=("Times New Roman", 20))
label_otvet = tk.Label(frame_for_window, bg="#83DA8B", font=("Times New Roman", 15))


label_a.grid(column=1, row=0)
entry_a.grid(column=1, row=1, pady=5)

label_b.grid(column=1, row=2)
entry_b.grid(column=1, row=3, pady=5)

label_e.grid(column=1, row=4)
entry_e.grid(column=1, row=5, pady=5)

label_n.grid(column=1, row=6)
entry_n.grid(column=1, row=7, pady=5)
btn_run.grid(column=1, row=8)
label_otvet.grid(column=1, row=9, pady=10)


frame_for_window.pack()
window_lab.mainloop()
