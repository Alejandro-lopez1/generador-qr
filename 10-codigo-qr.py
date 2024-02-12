import tkinter as tk 
from tkinter import ttk 
import qrcode

class GeneradorQrApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Generador de códigos QR")

        self.label_texto = ttk.Label(self.master, text="Texto para el código QR")
        self.label_texto.grid(row=0, column=0, padx=5, pady=5)

        self.texto_entry = ttk.Entry(self.master, width=50)
        self.texto_entry.grid(row=0, column=1, padx=5, pady=5)

        self.generar_button = ttk.Button(self.master, text="Generar QR", command=self.generar_qr)
        self.generar_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.qr_image = tk.Label(self.master)
        self.qr_image.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def generar_qr(self):
        texto = self.texto_entry.get()
        qr = qrcode.make(texto)
        qr = qr.resize((200, 200))
        qr.save("codigo_qr.png")

        self.qr_image.config(image=None)
        qr_image = tk.PhotoImage(file="codigo_qr.png")
        self.qr_image.config(image=qr_image)
        self.qr_image.image = qr_image

if __name__ == "__main__":
    root = tk.Tk()
    app = GeneradorQrApp(root)
    root.mainloop()
