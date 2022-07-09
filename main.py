from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3

def Database():
    global connection, cursor
    connection = sqlite3.connect("contact.db")
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS KONTAKTI (RID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, IME TEXT, PREZIME TEXT, BROJ_TELEFONA TEXT, ADRESA TEXT, EMAIL TEXT)")

def DisplayForm():
    display_screen = Tk()
    display_screen.geometry("1200x800")
    display_screen.title("Kontakti")
    global tree
    global SEARCH
    global ime, prezime, broj_telefona, adresa, email
    SEARCH = StringVar()
    ime = StringVar()
    prezime = StringVar()
    broj_telefona = StringVar()
    adresa = StringVar()
    email = StringVar()
    TopViewForm = Frame(display_screen, width=500, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LFrom = Frame(display_screen, width="350", bg="#393E46")
    LFrom.pack(side=LEFT, fill=Y)
    LeftViewForm = Frame(display_screen, width="350", bg="#393E46")
    LeftViewForm.pack(side=RIGHT, fill=Y)
    MidViewForm = Frame(display_screen, width="1000")
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="Kontakti", font=('Calibri', 22), width=400, bg="#222831", fg="white")
    lbl_text.pack(fill=X)
    Label(LFrom, text="Ime", font=("calibri", 13), bg="#00ADB5", fg="#EEEEEE").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=ime).pack(side=TOP, padx=10, pady=10, fill=X)
    Label(LFrom, text="Prezime", font=("calibri", 13), bg="#00ADB5", fg="#EEEEEE").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=prezime).pack(side=TOP, padx=10,pady=10, fill=X)
    Label(LFrom, text="Broj telefona", font=("calibri", 13), bg="#00ADB5", fg="#EEEEEE").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=broj_telefona).pack(side=TOP, padx=10,pady=10, fill=X)
    Label(LFrom, text="Adresa", font=("calibri", 13), bg="#00ADB5", fg="#EEEEEE").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=adresa).pack(side=TOP, padx=10,pady=10, fill=X)
    Label(LFrom, text="E-Mail", font=("calibri", 13), bg="#00ADB5", fg="#EEEEEE").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=email).pack(side=TOP, padx=10, pady=10, fill=X)
    Button(LFrom, text="Submit", font=("calibri", 13), command=register, bg="#00ADB5", fg="#EEEEEE").pack(
        side=TOP, padx=10, pady=5, fill=X)

    lbl_txtsearch = Label(LeftViewForm, text="Unesite ime za pretragu:", font=('calibri', 12), bg="#00ADB5", fg="#EEEEEE")
    lbl_txtsearch.pack()
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('calibri', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Pretraži",font=('calibri', 12), command=SearchRecord, bg="#00ADB5", fg="#EEEEEE")
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_view = Button(LeftViewForm, text="Prikaži sve",font=('calibri', 12), command=DisplayData, bg="#00ADB5", fg="#EEEEEE")
    btn_view.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Ponovno postavi",font=('calibri', 12), command=Reset, bg="#00ADB5", fg="#EEEEEE")
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Obriši", font=('calibri', 12), command=Delete, bg="#00ADB5", fg="#EEEEEE")
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Ažuriraj",font=('calibri', 12), command=Update, bg="#00ADB5", fg="#EEEEEE")
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("ID", "Ime", "Prezime", "Broj telefona", "Adresa", "E-Mail"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set,
                        xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('ID', text="ID", anchor=W)
    tree.heading('Ime', text="Ime", anchor=W)
    tree.heading('Prezime', text="Prezime", anchor=W)
    tree.heading('Broj telefona', text="Broj telefona", anchor=W)
    tree.heading('Adresa', text="Adresa", anchor=W)
    tree.heading('E-Mail', text="E-Mail", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=150)
    tree.column('#4', stretch=NO, minwidth=0, width=150)
    tree.column('#5', stretch=NO, minwidth=0, width=150)
    tree.pack()
    DisplayData()

def register():
    Database()
    ime1 = ime.get()
    prezime1 = prezime.get()
    broj_telefona1 = broj_telefona.get()
    adresa1 = adresa.get()
    email1 = email.get()
    if ime1 == '' or prezime1 == '' or broj_telefona1 == '' or adresa1 == '' or email1 == '':
        tkMessageBox.showinfo("Molimo, popunite sva polja!!!")
    else:
        connection.execute('INSERT INTO KONTAKTI (IME,PREZIME,BROJ_TELEFONA,ADRESA,EMAIL) \
              VALUES (?,?,?,?,?)', (ime1, prezime1, broj_telefona1, adresa1, email1));
        connection.commit()
        tkMessageBox.showinfo("Poruka", "Podaci uspješno spremljeni!")
        DisplayData()
        connection.close()

def Update():
    Database()
    ime1 = ime.get()
    prezime1 = prezime.get()
    broj_telefona1 = broj_telefona.get()
    adresa1 = adresa.get()
    email1 = email.get()
    if ime1 == '' or prezime1 == '' or broj_telefona1 == '' or adresa1 == '' or email1 == '':
        tkMessageBox.showinfo("Pozor", "Molimo, popunite sva polja!!!")
    else:
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']
        connection.execute('UPDATE KONTAKTI SET IME=?,PREZIME=?,BROJ_TELEFONA=?,ADRESA=?,EMAIL=? WHERE RID = ?',(ime1,prezime1,broj_telefona1,adresa1,email1, selecteditem[0]))
        connection.commit()
        tkMessageBox.showinfo("Poruka","Podaci uspješno ažurirani!")
        Reset()
        DisplayData()
        connection.close()

def Delete():
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Upozorenje","Odaberite podatke za brisanje!")
    else:
        result = tkMessageBox.askquestion('Potvrdite', 'Želite li obrisati ove podatke?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor=connection.execute("DELETE FROM KONTAKTI WHERE RID = %d" % selecteditem[0])
            connection.commit()
            cursor.close()
            connection.close()

def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")
    ime.set("")
    prezime.set("")
    broj_telefona.set("")
    adresa.set("")
    email.set("")

def SearchRecord():
    Database()
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        cursor=connection.execute("SELECT * FROM KONTAKTI WHERE IME LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        connection.close()

def DisplayData():
    Database()
    tree.delete(*tree.get_children())
    cursor=connection.execute("SELECT * FROM KONTAKTI")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
        tree.bind("<Double-1>",OnDoubleClick)
    cursor.close()
    connection.close()

def OnDoubleClick(self):
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    ime.set(selecteditem[1])
    prezime.set(selecteditem[2])
    broj_telefona.set(selecteditem[3])
    adresa.set(selecteditem[4])
    email.set(selecteditem[5])

DisplayForm()
if __name__=='__main__':
    mainloop()