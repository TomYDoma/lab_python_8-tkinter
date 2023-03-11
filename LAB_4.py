import tkinter as tk
from math import*
from tkinter.ttk import Treeview
import np as np

window_lab = tk.Tk()
window_lab.title("Студент: Маноцков Е.С. ЛР №4 ")
window_lab.geometry("400x400")
window_lab.resizable(width=False, height=False)
window_lab["bg"] = "#83DA8B"

def add():
    label_otvet.config(text="")
    try:
        number = []
        a = float(entry_a.get())
        b = float(entry_b.get())
        n = float(entry_n.get())

        k = (b - a) / n
        m = 0

        for x in np.arange(b, a - 0.5, -k):
            m += 1
            if x < -10:
                y = -2
                xy = (m, x, y)
                number.append(xy)
            elif -10 <= x <= -6:
                y = sqrt(4 - pow(x + 8, 2)) - 2
                xy = (m, x, y)
                number.append(xy)
            elif -6 < x <= 2:
                y = 0.5 * x + 1
                xy = (m, x, y)
                number.append(xy)
            elif 2 < x <= 6:
                y = 0
                xy = (m, x, y)
                number.append(xy)
            elif x > 6:
                y = pow(x - 6, 2)
                xy = (m, x, y)
                number.append(xy)

        newWindow = tk.Toplevel(window_lab)
        # определяем столбцы
        columns = ("N", "X", "Y")

        tree = Treeview(newWindow, columns=columns, show="headings")
        tree.grid(column=1, row=2)

        # определяем заголовки
        tree.heading("N", text="N")
        tree.heading("X", text="X")
        tree.heading("Y", text="Y")

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

label_a = tk.Label(frame_for_window, text="Вывод таблицы значений \n Введите a:", bg="#83DA8B", font=("Times New Roman", 15))
entry_a = tk.Entry(frame_for_window, font=("Times New Roman", 15))
label_b = tk.Label(frame_for_window, text="Введите b:", bg="#83DA8B", font=("Times New Roman", 15))
entry_b = tk.Entry(frame_for_window, font=("Times New Roman", 15))
label_n = tk.Label(frame_for_window, text="Введите n:", bg="#83DA8B", font=("Times New Roman", 15))
entry_n = tk.Entry(frame_for_window, font=("Times New Roman", 15))
btn_run = tk.Button(frame_for_window, text="Запуск", command=add, bg="#FFFFFF", font=("Times New Roman", 20))
label_otvet = tk.Label(frame_for_window, bg="#83DA8B", font=("Times New Roman", 15))

label_a.grid(column=1, row=0)
entry_a.grid(column=1, row=1, pady=10)
label_b.grid(column=1, row=2)
entry_b.grid(column=1, row=3, pady=10)
label_n.grid(column=1, row=4)
entry_n.grid(column=1, row=5, pady=10)
btn_run.grid(column=1, row=6)
label_otvet.grid(column=1, row=8, pady=10)

frame_for_window.pack()
window_lab.mainloop()
