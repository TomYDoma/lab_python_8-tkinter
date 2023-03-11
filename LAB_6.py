import tkinter as tk
from math import fabs, pi


window_lab = tk.Tk()
window_lab.title("Студент: Маноцков Е.С. ЛР №6 ")
window_lab.geometry("400x400")
window_lab.resizable(width=False, height=False)
window_lab["bg"] = "#83DA8B"

def add():
    label_otvet.config(text="")

    try:
        x = float(entry_x.get())
        e = float(entry_e.get())
        m = 0
        for n in range(0, 25):
            t = pow(-1, n + 1) / ((2 * n + 1) * pow(x, 2 * n + 1))
            if fabs(t) < e:
                break
            else:
                m += t
        label_otvet["text"] = "Сумма ряда Тейлора равна: " + str(m + pi / 2)

    except:
        label_otvet["text"] = "Неправильные входные данные"



frame_for_window = tk.Frame(window_lab)
frame_for_window["bg"] = "#83DA8B"

label_x = tk.Label(frame_for_window, text="Вычисление суммы ряда Тейлора \n Введите X:", bg="#83DA8B", font=("Times New Roman", 15))
entry_x = tk.Entry(frame_for_window, font=("Times New Roman", 15))
label_e = tk.Label(frame_for_window, text="Введите точность e:", bg="#83DA8B", font=("Times New Roman", 15))
entry_e = tk.Entry(frame_for_window, font=("Times New Roman", 15))
btn_run = tk.Button(frame_for_window, text="Запуск", command=add, bg="#FFFFFF", font=("Times New Roman", 20))
label_otvet = tk.Label(frame_for_window, bg="#83DA8B", font=("Times New Roman", 15))


label_x.grid(column=1, row=0)
entry_x.grid(column=1, row=1, pady=10)
label_e.grid(column=1, row=2)
entry_e.grid(column=1, row=3, pady=10)
btn_run.grid(column=1, row=6)
label_otvet.grid(column=1, row=7, pady=10)


frame_for_window.pack()
window_lab.mainloop()
