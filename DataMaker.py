import math
from tkinter import *
import tkinter as tk

from PIL import ImageTk, Image


class App(tk.Tk):
    def click_button(self):
        self.canvas.delete("all")

        newlabel = Label(self)

        newlabel.image = self.image
        newlabel["image"] = newlabel.image
        # newlabel.place(x=300,y=300)
        self.canvas.create_image(200, 200, image=self.image)

    def __init__(self, pilImage):
        super().__init__()
        self.title("Базовый canvas")
        self.line_start = None
        # self.form = LineForm(self)
        self.canvas = tk.Canvas(self, bg="snow", width=800, height=800)
        self.label = tk.Label(self)
        self.canvas.bind('<Button-1>', self.draw)
        self.angle= 0
        # self.form.pack(side=tk.LEFT, padx=10, pady=10)
        self.canvas.pack(side=tk.LEFT)
        self.label.pack()
        btn = Button(text="Следующий", background="#555", foreground="#ccc",
                     padx="20", pady="8", font="16", command=self.click_button)
        btn.pack()
        self.image = ImageTk.PhotoImage(pilImage)

        newlabel = Label(self)

        newlabel.image = self.image
        newlabel["image"] = newlabel.image
        # newlabel.place(x=300,y=300)
        self.canvas.create_image(200, 200, image=self.image)




    def draw(self, event):
        x, y = event.x, event.y
        text = "Позиция курсора: ({}, {})".format(x, y)
        self.label.config(text=text)
        if not self.line_start:
            self.line_start = (x, y)
        else:
            x_origin, y_origin = self.line_start
            self.line_start = None
            line = (x_origin, y_origin, x, y)
            # arrow = self.form.get_arrow()

            # width = self.form.get_width()

            self.canvas.create_line(*line)

            tg = (y - y_origin) / ((x - x_origin) + 0.001)
            text = text + str(math.degrees(math.atan(tg)))
            self.label.config(text=text)
            #self.canvas.delete("all")
            return str(math.degrees(math.atan(tg)))


if __name__ == "__main__":
    image_ = Image.open("pixel.jpg")
    app = App(image_)
    app.mainloop()
