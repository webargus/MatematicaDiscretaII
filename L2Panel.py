"""
    UFRPE - BSI 2019.1
    Matemática Discreta - prof. Marcelo Gama
    Dupla: Edson Kropniczki + Cristina Oliveira

    GUI p/ questão L2

"""

from tkinter import *
from tkinter import messagebox
import ScrollableText
import L2


class L2Panel:

    def __init__(self, frame):

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        wrap = Frame(frame)
        wrap.grid({"row": 0, "column": 0, "sticky": NSEW})
        wrap.grid_rowconfigure(2, weight=1)
        wrap.grid_columnconfigure(0, weight=1)

        header = Frame(wrap)
        header.grid({"row": 0, "column": 0, "sticky": NSEW})
        l1 = Label(header, {"text": "Entre as cadeias de bits x e y:",
                            "font": ("Arial", 12),
                            "padx": 20,
                            "pady": 20})
        l1.grid({"row": 0, "column": 0})

        form = Frame(wrap, {"pady": 8, "padx": 8})
        form.grid({"row": 1, "column": 0, "sticky": NSEW, "pady": 8, "padx": 8})
        Label(form, {"text": "x: ",
                     "font": ("Arial", 12)}).grid({"row": 0, "column": 0})
        self.x = StringVar()
        Entry(form, {"textvariable": self.x}).grid({"row": 0, "column": 1})
        Label(form, {"text": "y: ",
                     "font": ("Arial", 12)}).grid({"row": 0, "column": 2})
        self.y = StringVar()
        Entry(form, {"textvariable": self.y}).grid({"row": 0, "column": 3})
        params = {"text": "Ok",
                  "width": 5,
                  "font": ("Arial", 10),
                  "command": self._submit_form
                  }
        Button(form, params).grid({"row": 0, "column": 4, "padx": 4, "pady": 8, "sticky": W})

        text = Frame(wrap, {"pady": 8, "padx": 8})
        text.grid({"row": 2, "column": 0, "sticky": NSEW})
        text.grid_columnconfigure(0, weight=1)
        text.grid_rowconfigure(0, weight=1)
        self.text = ScrollableText.ScrollableText(text)

    def _submit_form(self):
        c1 = self.x.get()
        c2 = self.y.get()
        try:
            x, y = [int(c, 2) for c in (c1, c2)]
        except ValueError:
            messagebox.showerror("Êpa!!",
                                 "Entrada inválida!\nEntre cadeias somente com 1s e 0s.")
            return
        # salva o comprimento da maior cadeia em max_len
        max_len = max(len(c1), len(c2))
        # preenche cadeias com zeros à esquerda para que fiquem com o mesmo comprimento (açúcar)
        c1 = c1.zfill(max_len)
        c2 = c2.zfill(max_len)
        # executa operações lógicas bit a bit e as imprime formatadas
        ops = L2.bloco1_logica_l2(x, y)
        self.text.append_text("\n" + c1 + " OR " + c2 + " = " + bin(ops[0])[2:].zfill(max_len) + "\n")
        self.text.append_text(c1 + " XOR " + c2 + " = " + bin(ops[1])[2:].zfill(max_len) + "\n")
        self.text.append_text(c1 + " AND " + c2 + " = " + bin(ops[2])[2:].zfill(max_len) + "\n")
        self.text.append_text("_"*50 + "\n")







