import tkinter as tk

window_lab = tk.Tk()
window_lab.title("Студент: Маноцков Е.С. ЛР №3 ")
window_lab.geometry("400x400")
window_lab.resizable(width=False, height=False)
window_lab["bg"] = "#83DA8B"

def add():
    label_otvet.config(text="")
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        r = float(entry_r.get())

        if (x * x + y * y <= r * r and 0 <= x <= r and -r <= y <= r) \
                or (-x >= y and -r <= x <= 0 and 0 <= y <= r) \
                or (y <= x and -r <= x <= 0 and -r <= y <= 0):
            label_otvet["text"] = "Точка принадлежит"
        else:
            label_otvet["text"] = "Точка не принадлежит"
    except:
        label_otvet["text"] = "Неправильные входные данные"


frame_for_window = tk.Frame(window_lab)
frame_for_window["bg"] = "#83DA8B"

label_x = tk.Label(frame_for_window, text="Принадлежит ли точка области \n Введите X:", bg="#83DA8B", font=("Times New Roman", 15))
entry_x = tk.Entry(frame_for_window, font=("Times New Roman", 15))
label_y = tk.Label(frame_for_window, text="Введите Y:", bg="#83DA8B", font=("Times New Roman", 15))
entry_y = tk.Entry(frame_for_window, font=("Times New Roman", 15))
label_r = tk.Label(frame_for_window, text="Введите R:", bg="#83DA8B", font=("Times New Roman", 15))
entry_r = tk.Entry(frame_for_window, font=("Times New Roman", 15))
btn_run = tk.Button(frame_for_window, text="Запуск", command=add, bg="#FFFFFF", font=("Times New Roman", 20))
label_otvet = tk.Label(frame_for_window, bg="#83DA8B", font=("Times New Roman", 15))

label_x.grid(column=1, row=0)
entry_x.grid(column=1, row=1, pady=10)
label_y.grid(column=1, row=2)
entry_y.grid(column=1, row=3, pady=10)
label_r.grid(column=1, row=4)
entry_r.grid(column=1, row=5, pady=10)
btn_run.grid(column=1, row=6)
label_otvet.grid(column=1, row=8, pady=10)

frame_for_window.pack()
window_lab.mainloop()
