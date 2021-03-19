from tkinter import *


class DrawingPad:
    def __init__(self):
        self.root = Tk()
        self.c = Canvas(self.root, bg='white', width=1000, height=650, cursor="tcross")
        self.c.pack()
        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.c.bind('<B1-Motion>', self.draw)

    def draw(self, event):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y)
        self.old_x = event.x
        self.old_y = event.y


if __name__ == '__main__':
    DrawingPad()
