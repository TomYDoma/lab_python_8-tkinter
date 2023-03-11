import tkinter as tk
from math import*

window_lab = tk.Tk()
window_lab.title("Студент: Маноцков Е.С. ЛР №3 ")
window_lab.geometry("400x400")
window_lab["bg"] = "#83DA8B"

def add():
    label_z1.config(text="")
    label_z2.config(text="")
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())

        z1 = pow(cos(x), 4) + pow(sin(y), 2) + 1/4 * pow(sin(2 * x), 2) - 1
        z2 = sin(y+x) * cos(y-x)
        label_z1["text"] = "z1 = " + str(round(z1, 3))
        label_z2["text"] = "z2 = " + str(round(z2, 3))

    except:
        label_z1["text"] = "Неправильные входные данные"


frame_for_window = tk.Frame(window_lab)
frame_for_window["bg"] = "#83DA8B"

label_x = tk.Label(frame_for_window, text="Вычисление значений z1 и z2 \n Введите X:", bg="#83DA8B", font=("Times New Roman", 15))
entry_x = tk.Entry(frame_for_window, font=("Times New Roman", 15))
label_y = tk.Label(frame_for_window, text="Введите Y:", bg="#83DA8B", font=("Times New Roman", 15))
entry_y = tk.Entry(frame_for_window, font=("Times New Roman", 15))
btn_run = tk.Button(frame_for_window, text="Запуск", command=add, bg="#FFFFFF", font=("Times New Roman", 20))
label_z1 = tk.Label(frame_for_window, bg="#83DA8B", font=("Times New Roman", 15))
label_z2 = tk.Label(frame_for_window, bg="#83DA8B", font=("Times New Roman", 15))

entry_x.grid(column=1, row=3, pady=30)
label_x.grid(column=1, row=2)
label_y.grid(column=1, row=4)
entry_y.grid(column=1, row=5, pady=30)
btn_run.grid(column=1, row=6)
label_z1.grid(column=1, row=7)
label_z2.grid(column=1, row=8)

frame_for_window.pack()
window_lab.mainloop()
