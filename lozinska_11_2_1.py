from tkinter import *

def system(x1, x2, y1, y2, c1, c2):
    assert x1 !=0 and x2 != 0 and y1 != 0 and y2 != 0
    f = c1 / y1 - c2 / y2
    s = x1 / y1 - x2 / y2
    x = f / s
    y = c1 / y1 - ((x1 * f) / (y1 * s))
    return ("x=%.0f, y=%.0f" % (x, y))

def calculate():
    try:
        x1 = int(ein.get())
        x2 = int(ein1.get())
        y1 = int(ein2.get())
        y2 = int(ein3.get())
        c1 = int(ein4.get())
        c2 = int(ein5.get())
    except ValueError:
        lrez["text"] = "Були введені не всі дані," \
                       " або дані некорректні"
    else:
        try:
            f = system(x1, x2, y1, y2, c1, c2)
        except AssertionError:
            lrez["text"] = 'Один або декілька коефіціентів дорівнює 0!'
        else:
            lrez["text"] = '{}'.format(f)

root = Tk()

#==========================ПОЛЯ1=======================================

ein = Entry(master = root, font=('arial', 16))
ein.grid(row = 1, column = 1, sticky = W)

Label(root, text='x',
      font=('arial', 16)).grid(row = 1, column = 2, sticky = W)

Label(root, text='+',
      font=('arial', 16)).grid(row = 1, column = 3, sticky = W)

ein1 = Entry(root, font=('arial', 16))
ein1.grid(row = 1, column = 4, sticky = W)

Label(root, text='y',
      font=('arial', 16)).grid(row = 1, column = 5, sticky = W)

Label(root, text='=',
      font=('arial', 16)).grid(row = 1, column = 6, sticky = W)

ein2 = Entry(root, font=('arial', 16))
ein2.grid(row = 1, column = 7, sticky = W)

#=============================ПОЛЯ2==========================================

ein3 = Entry(root, font=('arial', 16))
ein3.grid(row = 2, column = 1, sticky = W)

Label(root, text='x',
      font=('arial', 16)).grid(row = 2, column = 2, sticky = W)

Label(root, text='+',
      font=('arial', 16)).grid(row = 2, column = 3, sticky = W)

ein4 = Entry(root, font=('arial', 16))
ein4.grid(row = 2, column = 4, sticky = W)

Label(root, text='y',
      font=('arial', 16)).grid(row = 2, column = 5, sticky = W)

Label(root, text='=',
      font=('arial', 16)).grid(row = 2, column = 6, sticky = W)

ein5 = Entry(root, font=('arial', 16))
ein5.grid(row = 2, column = 7, sticky = W)

#==========================ВИВЕДЕННЯ=========================================

Label(root, text='Відповідь',
font=('arial', 16)).grid(row = 3, column = 1, sticky = W)

lrez = Label(root, font=('arial', 16))
lrez.grid(row = 3, column = 1, sticky = W)

#=============================КНОПКИ=============================================

Button(root, text='Обчислити', command=calculate,
font=('arial', 16)).grid(row = 5, column = 1, sticky = W)

Button(root, text='Закрити', command=root.quit,
font=('arial', 16)).grid(row = 5, column = 7, sticky = E)

root.title("Калькулятор системи")
ein.focus()
ein1.focus()
ein2.focus()
ein3.focus()
ein4.focus()
ein5.focus()
root.mainloop()