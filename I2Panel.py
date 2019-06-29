from tkinter import *
from tkinter import messagebox
import ScrollableText
import I2


class I2Panel:

    def __init__(self, frame):

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        wrap = Frame(frame)
        wrap.grid({"row": 0, "column": 0, "sticky": NSEW})
        wrap.grid_rowconfigure(2, weight=1)
        wrap.grid_columnconfigure(0, weight=1)

        header = Frame(wrap)
        header.grid({"row": 0, "column": 0, "sticky": NSEW})
        l1 = Label(header, {"text": "Entre um inteiro positivo > 1 (n):",
                            "font": ("Arial", 12),
                            "padx": 20,
                            "pady": 20})
        l1.grid({"row": 0, "column": 0})

        form = Frame(wrap, {"padx": 8})
        form.grid({"row": 1, "column": 0, "sticky": NSEW, "pady": 8, "padx": 8})
        Label(form, {"text": "n: ",
                     "font": ("Arial", 12)}).grid({"row": 0, "column": 0})
        self.n = StringVar()
        Entry(form, {"textvariable": self.n}).grid({"row": 0, "column": 1})
        self.radio = IntVar()
        R1 = Radiobutton(form, text="is_prime", variable=self.radio, value=0, font=("Arial", 12))
        R1.grid({"row": 0, "column": 2})
        R2 = Radiobutton(form, text="is_prime_naif", variable=self.radio, value=1, font=("Arial", 12))
        R2.grid({"row": 0, "column": 3})
        params = {"text": "Ok",
                  "width": 5,
                  "font": ("Arial", 10),
                  "command": self._submit_form
                  }
        self.btn = Button(form, params)
        self.btn.grid({"row": 0, "column": 4, "padx": 4, "pady": 8, "sticky": W})

        text = Frame(wrap, {"pady": 8, "padx": 8})
        text.grid({"row": 2, "column": 0, "sticky": NSEW})
        text.grid_columnconfigure(0, weight=1)
        text.grid_rowconfigure(0, weight=1)
        self.text = ScrollableText.ScrollableText(text)

    def _submit_form(self):
        try:
            n = int(self.n.get())
            if n < 2:
                raise ValueError
        except ValueError:
            messagebox.showerror("Êpa!!",
                                 "Entrada inválida!\nEntre um inteiro > 1.")
            return

        self.text.append_text("\n...processando...\n")
        self.btn.configure(state="disabled")
        I2.check_prime_thread(n, self.radio.get(), self.report)

    def report(self, flag, n):
        s = "%d "
        if not flag:
            s += "não "
        s += "é primo."

        self.text.append_text("\n" + (s % n))
        self.text.append_text("\n" + "_"*50 + "\n")
        self.btn.configure(state="normal")

