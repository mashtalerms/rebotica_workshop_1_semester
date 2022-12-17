# Создать прямоугольник с тенью. Тень должна находиться под наклоном.
# Создать кнопки управления: вверх, вниз, вправо, влево.
# Прямоугольник с тенью должны двигаться при нажатии на на кнопки.

from tkinter import *


def main():

    def move_up():
        canvas.move(square_object, 0, -3)
        canvas.move(shadow, 0, -3)

    def move_down():
        canvas.move(square_object, 0, 3)
        canvas.move(shadow, 0, 3)

    def move_right():
        canvas.move(square_object, 3, 0)
        canvas.move(shadow, 3, 0)

    def move_left():
        canvas.move(square_object, -3, 0)
        canvas.move(shadow, -3, 0)

    tk = Tk()
    tk.geometry("600x800")

    canvas = Canvas(width=400, height=500, bg='lightgrey')
    canvas.pack()

    square_object = canvas.create_rectangle(100, 100, 150, 150, fill="wheat")
    shadow = canvas.create_rectangle(130, 150, 170, 190, fill="gray")

    but_up = Button(text='↑', command=move_up)

    but_down = Button(text='↓', command=move_down)

    but_right = Button(text='→', command=move_right)

    but_left = Button(text='←', command=move_left)

    but_up.pack(expand=True, side=RIGHT)
    but_down.pack(expand=True, side=RIGHT)
    but_right.pack(expand=True, side=LEFT)
    but_left.pack(expand=True, side=LEFT)

    tk.mainloop()


if __name__ == "__main__":
    main()
