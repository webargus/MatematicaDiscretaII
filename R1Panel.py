from tkinter import *
from tkinter import messagebox
import ScrollableText
import R1


class R1Panel:

    def __init__(self, frame):

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        wrap = Frame(frame)
        wrap.grid({"row": 0, "column": 0, "sticky": NSEW})
        wrap.grid_rowconfigure(2, weight=1)
        wrap.grid_columnconfigure(0, weight=1)

        header = Frame(wrap)
        header.grid({"row": 0, "column": 0, "sticky": NSEW})
        l1 = Label(header, {"text": "Entre os pares de inteiros (a,m) e (b,n):",
                            "font": ("Arial", 12),
                            "padx": 20,
                            "pady": 20})
        l1.grid({"row": 0, "column": 0})

        form = Frame(wrap, {"pady": 8, "padx": 8})
        form.grid({"row": 1, "column": 0, "sticky": NSEW, "pady": 8, "padx": 8})

        Label(form, {"text": "s ≡ a ",
                     "font": ("Arial", 12)}).grid({"row": 0, "column": 0})
        self.a = StringVar()
        Entry(form, {"textvariable": self.a}).grid({"row": 0, "column": 1})
        Label(form, {"text": "(mod m) ",
                     "font": ("Arial", 12)}).grid({"row": 0, "column": 2})
        self.m = StringVar()
        Entry(form, {"textvariable": self.m}).grid({"row": 0, "column": 3})

        Label(form, {"text": "s ≡ b ",
                     "font": ("Arial", 12)}).grid({"row": 1, "column": 0})
        self.b = StringVar()
        Entry(form, {"textvariable": self.b}).grid({"row": 1, "column": 1})
        Label(form, {"text": "(mod n) ",
                     "font": ("Arial", 12)}).grid({"row": 1, "column": 2})
        self.n = StringVar()
        Entry(form, {"textvariable": self.n}).grid({"row": 1, "column": 3})
        params = {"text": "Ok",
                  "width": 5,
                  "font": ("Arial", 10),
                  "command": self._submit_form
                  }
        self.btn = Button(form, params)
        self.btn.grid({"row": 1, "column": 4, "padx": 4, "pady": 8, "sticky": W})

        text = Frame(wrap, {"pady": 8, "padx": 8})
        text.grid({"row": 2, "column": 0, "sticky": NSEW})
        text.grid_columnconfigure(0, weight=1)
        text.grid_rowconfigure(0, weight=1)
        self.text = ScrollableText.ScrollableText(text)

    def _submit_form(self):
        try:
            a, m = [int(x) for x in (self.a.get(), self.m.get())]
            if (a >= m) or (a < 0) or (m < 2):
                raise ValueError
            b, n = [int(x) for x in (self.b.get(), self.n.get())]
            if (b >= n) or (b < 0) or (n < 2):
                raise ValueError
        except ValueError:

            messagebox.showerror("Êpa!!",
                                 "Entrada inválida!\nVerifique os dados.")
            return

        self.text.append_text("\ns ≡ %d (mod %d)" % (a, m))
        self.text.append_text("\ns ≡ %d (mod %d)\n" % (b, n))
        flag, txt = R1.checa_mdc(m, n)
        self.text.append_text("\n" + txt)
        if flag:
            self.text.append_text("\n\ndependendo das entradas, isso pode levar alguns minutos\n")
            self.text.append_text("...calculando...\n")
            self.btn.configure(state="disabled")
            R1.metodo_geometrico_thread(a, b, m, n, self.callback)
        else:
            self.text.append_text("\n" + "_" * 55 + "\n")

    def callback(self, param):
        self.text.append_text(param)
        self.text.append_text("\n" + "_"*55 + "\n")
        self.btn.configure(state="normal")


