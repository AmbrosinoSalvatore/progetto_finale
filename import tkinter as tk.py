import tkinter as tk

root = tk.Tk()  # crea una finestra
root.title("La mia finestra")  # imposta il titolo della finestra

etichetta = tk.Label(root, text="Ciao, mondo!")  # crea una etichetta
etichetta.pack()  # posiziona l'etichetta nella finestra

root.mainloop()  # avvia il ciclo di eventi della finestra