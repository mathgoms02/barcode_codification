import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from barcode_codification import inser, crea
import pyautogui as pygui

def main():
    root = tk.Tk()
    root.title('Key Generator (barcode)')
    root.geometry('600x500')
    root.resizable(width=False, height=False)
    root.configure(background='#000000')

    root.iconbitmap("barcode.ico")


    margin = Canvas(root, width=600, bg='#FFFFFF', height=10, bd=1, highlightthickness=1, relief='ridge')
    margin.pack()

    Label_inserir_nome = Label(root, bg='#000000', fg='#FFFFFF', text='Nome:', font=('Arial', 12, 'bold'))
    Label_inserir_nome.pack(pady=10)
    box_name = tk.Entry(root, width=60)
    box_name.pack(pady=1)

    Label_inserir_re = Label(root, bg='#000000', fg='#FFFFFF', text='RE:', font=('Arial', 12, 'bold'))
    Label_inserir_re.pack(pady=10)
    box_re = tk.Entry(root, width=60)
    box_re.pack(pady=1)




    def add_barcode():
        name = box_name.get()
        re = box_re.get()
        try:
            inser(name, re)
            messagebox.showinfo('Adicionado', 'Informações adicionadas!!\nPara criar, clique em "Create')
        except FileNotFoundError as err:
            messagebox.showinfo('ERROR', str(err))

        box_name.delete(0, END)
        box_re.delete(0, END)

        table_operator.insert("", tk.END, values=(name, re))

        pygui.hotkey('shift', 'tab')

    def create_barcode():
        try:
            crea()
            messagebox.showinfo('Sucesso!', 'Código(s) de barra criado com sucesso!!!')

            table_operator.delete(*table_operator.get_children())

        except Exception as err:
            messagebox.showinfo('ERROR', str(err))
        

    button_add = Button(root, text='Add', width=5, font=('Montserrat', 12, 'bold'), command=add_barcode)
    button_add.configure(bg="#808080", fg="black", relief="raised", padx=10, pady=5, activebackground="#808080")
    button_add.place(x=200, y=190)

    button_create = Button(root, text='Create', width=5, font=('Montserrat', 12, 'bold'), command=create_barcode)
    button_create.configure(bg="#808080", fg="black", relief="raised", padx=10, pady=5, activebackground="#808080")
    button_create.place(x=300, y=190)

    # Criando tabela para usuário ver os QRCodes ja criado
    table_operator = ttk.Treeview(root)
    table_operator["columns"] = ("Nome", "RE")

    # Formatando colunas
    table_operator.column("#0", width=0, stretch=tk.NO)
    table_operator.column("Nome", width=120, anchor="center")
    table_operator.column("RE", width=120, anchor="center")

    # Definindo cabeçalho
    table_operator.heading("#0", text="", anchor=tk.W)
    table_operator.heading("Nome", text="Nome", anchor=tk.W)
    table_operator.heading("RE", text="RE", anchor=tk.W)

    table_operator.place(x=175, y=250)

    root.mainloop()

if __name__ == "__main__":
    main()