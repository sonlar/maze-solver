from tkinter import Tk, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze-solver")
        canvas = Canvas(self.__root, width=width, height=height)
        canvas.pack()
        self.__in_progress = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close())

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        self.__in_progress = True
        while self.__in_progress:
            self.redraw()

    def close(self):
        self.__in_progress = False


if __name__ == "__main__":
    window = Window(500, 500)
    window.wait_for_close()
