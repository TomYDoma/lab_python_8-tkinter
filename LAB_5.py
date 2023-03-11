import random
import tkinter as tk
from tkinter.ttk import Treeview

window_lab = tk.Tk()
window_lab.title("Студент: Маноцков Е.С. ЛР №5 ")
window_lab.geometry("400x400")
window_lab.resizable(width=False, height=False)
window_lab["bg"] = "#83DA8B"

def add():
    label_otvet_1.config(text="")
    label_otvet_2.config(text="")
    try:
        truth_data = []
        lie_data = []
        digit = int(entry_digit.get())
        r = int(entry_r.get())
        truth = 0
        lie = 0
        for i in range(digit):
            x = random.randrange(-r, r)
            y = random.randrange(-r, r)

            if (x * x + y * y <= r * r and 0 <= x <= r and -r <= y <= r) \
                    or (-x >= y and -r <= x <= 0 and 0 <= y <= r) \
                    or (y <= x and -r <= x <= 0 and -r <= y <= 0):
                truth += 1
                xy = (truth, x, y)
                truth_data.append(xy)
            else:
                lie += 1
                xy = (lie, x, y)
                lie_data.append(xy)

        label_otvet_1["text"] = "Вы попали: {} раз".format(truth)
        label_otvet_2["text"] = "Вы промазали: {} раз".format(lie)

        newWindow_truth = tk.Toplevel(window_lab)
        newWindow_truth.title("Попадания")
        newWindow_truth.geometry("250x250")
        columns = ("n", "x", "y")
        tree = Treeview(newWindow_truth, columns=columns, show="headings")
        tree.grid(column=1, row=2)
        tree.heading("n", text="N")
        tree.heading("x", text="X")
        tree.heading("y", text="Y")
        tree.column("#1", width=70)
        tree.column("#2", width=70)
        tree.column("#3", width=70)
        for i in truth_data:
            tree.insert(parent='', index='end', values=i)

        newWindow_lie = tk.Toplevel(window_lab)
        newWindow_lie.title("Промахи")
        newWindow_lie.geometry("250x250")
        columns = ("n", "x", "y")
        tree = Treeview(newWindow_lie, columns=columns, show="headings")
        tree.grid(column=1, row=2)
        tree.heading("n", text="N")
        tree.heading("x", text="X")
        tree.heading("y", text="Y")
        tree.column("#1", width=70)
        tree.column("#2", width=70)
        tree.column("#3", width=70)
        for j in lie_data:
            tree.insert(parent='', index='end', values=j)


    except:
        label_otvet_1["text"] = "Неправильные входные данные"
        label_otvet_2["text"] = "Неправильные входные данные"


frame_for_window = tk.Frame(window_lab)
frame_for_window["bg"] = "#83DA8B"

label_digit = tk.Label(frame_for_window, text="Стреляем по мишени \n Введите количество выстрелов:", bg="#83DA8B", font=("Times New Roman", 15))
entry_digit = tk.Entry(frame_for_window, font=("Times New Roman", 15))
label_r = tk.Label(frame_for_window, text="Введите r:", bg="#83DA8B", font=("Times New Roman", 15))
entry_r = tk.Entry(frame_for_window, font=("Times New Roman", 15))
btn_run = tk.Button(frame_for_window, text="Запуск", command=add, bg="#FFFFFF", font=("Times New Roman", 20))
label_otvet_1 = tk.Label(frame_for_window, bg="#83DA8B", font=("Times New Roman", 15))
label_otvet_2 = tk.Label(frame_for_window, bg="#83DA8B", font=("Times New Roman", 15))

label_digit.grid(column=1, row=0)
entry_digit.grid(column=1, row=1, pady=10)
label_r.grid(column=1, row=2)
entry_r.grid(column=1, row=3, pady=10)
btn_run.grid(column=1, row=6)
label_otvet_1.grid(column=1, row=7, pady=10)
label_otvet_2.grid(column=1, row=8, pady=10)

frame_for_window.pack()
window_lab.mainloop()
