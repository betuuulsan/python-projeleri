print("merhaba dünya")
import tkinter as tk
from tkinter import ttk

pencere = tk.Tk()
pencere.geometry("300x200")
pencere.title("Selamlama sayfası")

mesaj = tk.Label(pencere,
                text="merhaba,dünya",
                font=("Helvetica",20),
                bg="#87a889")
mesaj.pack()

buton = ttk.Button(pencere,
                   text= "EXIT",
                   command=lambda: pencere.quit())
buton.pack()




pencere.mainloop()
