from tkinter import *
from tkinter import ttk
import tkinter.ttk


def combos(eventObject):
    global x
    x = combo.get()
    return x

def enviar():
    global soma
    qtd = entry_1.get()
    combos(Event)


    if int(qtd) == 1 and x=='Somente letras até 8cm':
        soma = 72.00
        description = '      Para personalizar 1 item,\n         você deve adicionar:'

    elif 2<=int(qtd)<=3 and x=='Somente letras até 8cm':
        soma = 24.00
        description = f'       Para personalizar {entry_1.get()} itens,\n         você deve adicionar:'

    elif 4<=int(qtd)<=7 and x=='Somente letras até 8cm':
        soma = 10.29
        description = f'       Para personalizar {entry_1.get()} itens,\n         você deve adicionar:'

    elif 8<=int(qtd)<=11 and x=='Somente letras até 8cm':
        soma = 6.55
        description = f'       Para personalizar {entry_1.get()} itens,\n         você deve adicionar:'

    elif int(qtd)>=12 and x=='Somente letras até 8cm':
        soma = 6.00
        description = f'       Para personalizar {entry_1.get()} itens,\n         você deve adicionar:'

    elif int(qtd) == 1 and x == 'Somente letras até 16cm':
        soma = 96.00
        description = '      Para personalizar 1 item,\n         você deve adicionar:'

    elif 2<=int(qtd)<=3 and x == 'Somente letras até 16cm':
        soma = 32.00
        description = f'       Para personalizar {entry_1.get()} itens,\n         você deve adicionar:'

    elif 4<=int(qtd)<=7 and x == 'Somente letras até 16cm':
        soma = 13.71
        description = f'       Para personalizar {entry_1.get()} itens,\n         você deve adicionar:'

    elif 8<=int(qtd)<=11 and x == 'Somente letras até 16cm':
        soma = 8.73
        description = f'       Para personalizar {entry_1.get()} itens,\n         você deve adicionar:'

    elif int(qtd)>=12 and x == 'Somente letras até 16cm':
        soma = 8.00
        description = f'       Para personalizar {entry_1.get()} itens,\n         você deve adicionar:'

    elif int(qtd) == 1 and x == 'Logo sem fundo até 8cm':
        soma = 108.00
        description = '      Para personalizar 1 item,\n         você deve adicionar:'

    elif 2<=int(qtd)<=3 and x == 'Logo sem fundo até 8cm':
        soma = 36.00
        description = f'       Para personalizar {entry_1.get()} itens,\n         você deve adicionar:'

    elif 4<=int(qtd)<=7 and x == 'Logo sem fundo até 8cm':
        soma = 15.43
        description = f'       Para personalizar {entry_1.get()} itens,\n         você deve adicionar:'

    elif 8<=int(qtd)<=11 and x == 'Logo sem fundo até 8cm':
        soma = 9.82
        description = f'       Para personalizar {entry_1.get()} itens,\n         você deve adicionar:'

    elif int(qtd)>=12 and x == 'Logo sem fundo até 8cm':
        soma = 9.00
        description = f'       Para personalizar {entry_1.get()} itens,\n         você deve adicionar:'

    elif int(qtd) == 1 and x == 'Logo sem fundo até 16cm':
        soma = 156.00
        description = '      Para personalizar 1 item,\n         você deve adicionar:'

    elif 2<=int(qtd)<=3 and x == 'Logo sem fundo até 16cm':
        soma = 52.00
        description = f'       Para personalizar {entry_1.get()} itens,\n         você deve adicionar:'

    elif 4<=int(qtd)<=7 and x == 'Logo sem fundo até 16cm':
        soma = 22.29
        description = f'       Para personalizar {entry_1.get()} itens,\n         você deve adicionar:'

    elif 8<=int(qtd)<=11 and x == 'Logo sem fundo até 16cm':
        soma = 14.18
        description = f'       Para personalizar {entry_1.get()} itens,\n         você deve adicionar:'

    elif int(qtd)>=12 and x == 'Logo sem fundo até 16cm':
        soma = 13.00
        description = f'       Para personalizar {entry_1.get()} itens,\n         você deve adicionar:'

    elif int(qtd) == 1 and x == 'Logo com fundo até 8cm':
        soma = 180.00
        description = '      Para personalizar 1 item,\n         você deve adicionar:'

    elif 2<=int(qtd)<=3 and x == 'Logo com fundo até 8cm':
        soma = 60.00
        description = f'       Para personalizar {entry_1.get()} itens,\n         você deve adicionar:'

    elif 4<=int(qtd)<=7 and x == 'Logo com fundo até 8cm':
        soma = 25.71
        description = f'       Para personalizar {entry_1.get()} itens,\n         você deve adicionar:'

    elif 8<=int(qtd)<=11 and x == 'Logo com fundo até 8cm':
        soma = 16.36
        description = f'       Para personalizar {entry_1.get()} itens,\n         você deve adicionar:'

    elif int(qtd)>=12 and x == 'Logo com fundo até 8cm':
        soma = 15.00
        description = f'       Para personalizar {entry_1.get()} itens,\n         você deve adicionar:'

    elif int(qtd) == 1 and x == 'Logo com fundo até 16cm':
        soma = 240.00
        description = '      Para personalizar 1 item,\n         você deve adicionar:'

    elif 2<=int(qtd)<=3 and x == 'Logo com fundo até 16cm':
        soma = 80.00
        description = f'       Para personalizar {entry_1.get()} itens,\n         você deve adicionar:'

    elif 4<=int(qtd)<=7 and x == 'Logo com fundo até 16cm':
        soma = 34.29
        description = f'       Para personalizar {entry_1.get()} itens,\n         você deve adicionar:'

    elif 8<=int(qtd)<=11 and x == 'Logo com fundo até 16cm':
        soma = 21.82
        description = f'       Para personalizar {entry_1.get()} itens,\n         você deve adicionar:'

    elif int(qtd)>=12 and x == 'Logo com fundo até 16cm':
        soma = 20.00
        description = f'       Para personalizar {entry_1.get()} itens,\n         você deve adicionar:'

    
    label_4.configure(text=f'{y} R${soma:.2f} além\ndo valor da peça.')
    clean()
    entry_1.focus()

def clean():
    entry_1.delete(0, END)
    

window = Tk()
window.geometry('400x300')
window.resizable(False, False)
window.title('Calculadora')



# Frames
frame_1 = Frame(window, bg='#b82323')
frame_1.place(relx=0, rely=0, relheight=1, relwidth=1)


# Labels
label_1 = Label(window, text='Calculadora Bordado', font=('Helvetica', 20, 'bold'), width=450, bg='#871010', height=2, fg="white")
label_1.place(relx=0.5, rely=0.1, anchor='c')

label_2 = Label(frame_1, text='Quantidade', fg='white', bg='#b82323', font=('Arial', 15, 'bold'))
label_2.place(relx=0.2, rely=0.35, relheight=0.1)

label_3 = Label(frame_1, text='Valor Bordado', fg='white', bg='#b82323', font=('Arial', 15, 'bold'))
label_3.place(relx=0.13, rely=0.45, relheight=0.1)

label_4 = Label(frame_1, text='', fg='white', bg='#b82323', font=('Arial', 12, 'bold'))
label_4.place(relx=0.08, rely=0.74, relheight=0.2, relwidth=0.83)


# Entrys
entry_1 = Entry(frame_1, relief='flat')
entry_1.place(relx=0.52, rely=0.377, relheight=0.06, relwidth=0.385)


# Buttons
btn_1 = Button(frame_1, relief='flat', text='Enviar', command=enviar)
btn_1.place(relx=0.757, rely=0.57, relheight=0.07, relwidth=0.15)




combo = ttk.Combobox(frame_1, width=22, values=['Somente letras até 8cm',
 'Somente letras até 16cm', 'Logo sem fundo até 8cm', 'Logo sem fundo até 16cm',
 'Logo com fundo até 8cm', 'Logo com fundo até 16cm'])
combo.place(relx=0.52, rely=0.47)
x = combo.bind("<<ComboboxSelected>>", combos)


if __name__ == '__main__':
    window.mainloop()

