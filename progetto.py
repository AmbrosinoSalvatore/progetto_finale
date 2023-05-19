import tkinter as tk
import pymssql

def register_user():
    # PRENDEi dati inseriti dall'utente
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    # connessione al database
    conn = pymssql.connect(server='192.168.40.16\SQLEXPRESS', user='dilecce.gabriele', password='xxx123##', database='dilecce.gabriele')

    # creazione del cursore
    cursor = connxzxzx.cursor()

    # inserimento dei dati degli utenti nella tabella
    cursor.execute('INSERT INTO Utenti (Username, Email, Password, ConfermaPassword) VALUES (%s,%s,%s,%s)',
                   (username, email, password, confirm_password))
    conn.commit()

    # chiusura della connessione
    conn.close()

    # messaggio di conferma
    confirmation_label.config(text="Registrazione completata con successo.")

# creazione della finestra principale
window = tk.Tk()
window.title("Registrazione Utente")

# creazione dei widget della finestra
username_label = tk.Label(text="Username:")
username_entry = tk.Entry()
email_label = tk.Label(text="Email:")
email_entry = tk.Entry()
password_label = tk.Label(text="Password:")
password_entry = tk.Entry(show="*")
confirm_password_label = tk.Label(text="Conferma Password:")
confirm_password_entry = tk.Entry(show="*")
register_button = tk.Button(text="Registrati", command=register_user)
confirmation_label = tk.Label(text="")

# posizionamento dei widget nella finestra
username_label.pack()
username_entry.pack()
email_label.pack()
email_entry.pack()
password_label.pack()
password_entry.pack()
confirm_password_label.pack()
confirm_password_entry.pack()
register_button.pack()
confirmation_label.pack()

# avvio dell'applicazione
window.mainloop()