from tkinter import *
from tkinter.ttk import *
import ScrollableText
import L2Panel
import C1Panel
import F2Panel
import I2Panel
import R1Panel


class Gui(Frame):

    def __init__(self):
        Frame.__init__(self)
        # self.master.iconbitmap(tools.icon32)
        # tools.StaticImages()
        #self.master.wm_minsize(800, 600)
        self.master.state('normal')
        self.master.title("Matemática Discreta")
        # tools.center_window(self.master)
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.grid({"row": 0, "column": 0, "sticky": NSEW})
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.nb = Notebook(self)
        #   add tabs
        self.nb_files = [("L2", Frame(self.nb)),
                         ("C1", Frame(self.nb)),
                         ("F2", Frame(self.nb)),
                         ("I2", Frame(self.nb)),
                         ("R1", Frame(self.nb))]
        for i in self.nb_files:
            self.nb.add(i[1], text="    " + i[0] + "    ")
        self.nb.grid({"row": 0, "column": 0, "sticky": NSEW})
        self.nb.bind("<<NotebookTabChanged>>", self._tab_switch)

        L2Panel.L2Panel(self.nb_files[0][1])
        C1Panel.C1Panel(self.nb_files[1][1])
        F2Panel.F2Panel(self.nb_files[2][1])
        I2Panel.I2Panel(self.nb_files[3][1])
        R1Panel.R1Panel(self.nb_files[4][1])

        frame = Frame(self)
        frame.grid({"row": 0, "column": 1, "sticky": NSEW, "pady": 4, "padx": 4})
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        self.text_widget = ScrollableText.ScrollableText(frame)

        self.mainloop()

    def _tab_switch(self, event):
        file = self.nb_files[self.nb.index(self.nb.select())][0] + ".py"
        try:
            handle = open(file, "r", encoding="utf-8")
        except OSError:
            print(OSError.args)
        self.text_widget.clear()
        for line in handle.readlines():
            self.text_widget.append_text(line)
        handle.close()


if __name__ == '__main__':
    gui = Gui()




