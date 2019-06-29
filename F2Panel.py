from tkinter import *
from tkinter import messagebox
import ScrollableText
import F2


class F2Panel:

    def __init__(self, frame):

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        wrap = Frame(frame)
        wrap.grid({"row": 0, "column": 0, "sticky": NSEW})
        wrap.grid_rowconfigure(2, weight=1)
        wrap.grid_columnconfigure(0, weight=1)

        header = Frame(wrap)
        header.grid({"row": 0, "column": 0, "sticky": NSEW})
        l1 = Label(header, {"text": "Entre a semente (n):",
                            "font": ("Arial", 12),
                            "padx": 20,
                            "pady": 20})
        l1.grid({"row": 0, "column": 0})

        form = Frame(wrap, {"pady": 8, "padx": 8})
        form.grid({"row": 1, "column": 0, "sticky": NSEW, "pady": 8, "padx": 8})
        Label(form, {"text": "n: ",
                     "font": ("Arial", 12)}).grid({"row": 0, "column": 0})
        self.n = StringVar()
        Entry(form, {"textvariable": self.n}).grid({"row": 0, "column": 1})
        params = {"text": "Ok",
                  "width": 5,
                  "font": ("Arial", 10),
                  "command": self._submit_form
                  }
        Button(form, params).grid({"row": 0, "column": 2, "padx": 4, "pady": 8, "sticky": W})

        text = Frame(wrap, {"pady": 8, "padx": 8})
        text.grid({"row": 2, "column": 0, "sticky": NSEW})
        text.grid_columnconfigure(0, weight=1)
        text.grid_rowconfigure(0, weight=1)
        self.text = ScrollableText.ScrollableText(text)

    def _submit_form(self):
        try:
            n = int(self.n.get())
        except ValueError:
            messagebox.showerror("Êpa!!",
                                 "Entrada inválida!\nEntre um valor inteiro qualquer.")
            return

        self.text.append_text(("\nX0 = %d; sequência aleatória: " % n) + F2.middle_square(n))
        self.text.append_text("\n" + "_"*50 + "\n")

