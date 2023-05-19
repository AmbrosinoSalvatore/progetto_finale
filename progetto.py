import tkinter as tk

def saluta():
    nome = entry_nome.get()
    label_saluto.config(text="Ciao " + nome)

root = tk.Tk()

label_nome = tk.Label(root, text="Inserisci il tuo nome:")
label_nome.pack()

entry_nome = tk.Entry(root)
entry_nome.pack()

button_saluta = tk.Button(root, text="Saluta", command=saluta)
button_saluta.pack()

label_saluto = tk.Label(root)
label_saluto.pack()

s
root.mainloop()