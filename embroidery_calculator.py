from tkinter import *
from tkinter import ttk


def main():
    global combo, label_result_text_area, entry_qty

    window = Tk()
    window.geometry('400x300')
    window.resizable(False, False)
    window.title('Calculadora')

    # Frames
    frame_main = Frame(window, bg='#b82323')
    frame_main.place(relx=0, rely=0, relheight=1, relwidth=1)

    # Labels
    label_calculator = Label(window, text='Calculadora Bordado', font=(
        'Helvetica', 20, 'bold'), width=450, bg='#871010', height=2, fg="white")
    label_calculator.place(relx=0.5, rely=0.1, anchor='c')

    label_qty = Label(frame_main, text='Quantidade', fg='white',
                      bg='#b82323', font=('Arial', 15, 'bold'))
    label_qty.place(relx=0.2, rely=0.35, relheight=0.1)

    label_embroidery_value = Label(
        frame_main, text='Valor Bordado', fg='white', bg='#b82323', font=('Arial', 15, 'bold'))
    label_embroidery_value.place(relx=0.13, rely=0.45, relheight=0.1)

    label_result_text_area = Label(
        frame_main, text='', fg='white', bg='#b82323', font=('Arial', 12, 'bold'))
    label_result_text_area.place(
        relx=0.08, rely=0.74, relheight=0.2, relwidth=0.83)

    # Entrys
    entry_qty = Entry(frame_main, relief='flat')
    entry_qty.place(relx=0.52, rely=0.377, relheight=0.06, relwidth=0.385)

    # Buttons
    btn_send = Button(frame_main, relief='flat', text='Enviar', command=send)
    btn_send.place(relx=0.757, rely=0.57, relheight=0.07, relwidth=0.15)

    combo = ttk.Combobox(frame_main, width=22, values=['Somente letras até 8cm',
                                                       'Somente letras até 16cm', 'Logo sem fundo até 8cm', 'Logo sem fundo até 16cm',
                                                       'Logo com fundo até 8cm', 'Logo com fundo até 16cm'])
    combo.place(relx=0.52, rely=0.47)
    x = combo.bind("<<ComboboxSelected>>", combos)

    window.mainloop()


def combos(eventObject):
    global combo_get

    combo_get = combo.get()
    return combo_get


def send():
    global corresponding_value

    qtd = entry_qty.get()
    combos(Event)

    if int(qtd) == 1 and combo_get == 'Somente letras até 8cm':
        corresponding_value = 72.00
        description = '      Para personalizar 1 item,\n         você deve adicionar:'

    elif 2 <= int(qtd) <= 3 and combo_get == 'Somente letras até 8cm':
        corresponding_value = 24.00
        description = f'       Para personalizar {qtd} itens,\n         você deve adicionar:'

    elif 4 <= int(qtd) <= 7 and combo_get == 'Somente letras até 8cm':
        corresponding_value = 10.29
        description = f'       Para personalizar {qtd} itens,\n         você deve adicionar:'

    elif 8 <= int(qtd) <= 11 and combo_get == 'Somente letras até 8cm':
        corresponding_value = 6.55
        description = f'       Para personalizar {qtd} itens,\n         você deve adicionar:'

    elif int(qtd) >= 12 and combo_get == 'Somente letras até 8cm':
        corresponding_value = 6.00
        description = f'       Para personalizar {qtd} itens,\n         você deve adicionar:'

    elif int(qtd) == 1 and combo_get == 'Somente letras até 16cm':
        corresponding_value = 96.00
        description = '      Para personalizar 1 item,\n         você deve adicionar:'

    elif 2 <= int(qtd) <= 3 and combo_get == 'Somente letras até 16cm':
        corresponding_value = 32.00
        description = f'       Para personalizar {qtd} itens,\n         você deve adicionar:'

    elif 4 <= int(qtd) <= 7 and combo_get == 'Somente letras até 16cm':
        corresponding_value = 13.71
        description = f'       Para personalizar {qtd} itens,\n         você deve adicionar:'

    elif 8 <= int(qtd) <= 11 and combo_get == 'Somente letras até 16cm':
        corresponding_value = 8.73
        description = f'       Para personalizar {qtd} itens,\n         você deve adicionar:'

    elif int(qtd) >= 12 and combo_get == 'Somente letras até 16cm':
        corresponding_value = 8.00
        description = f'       Para personalizar {qtd} itens,\n         você deve adicionar:'

    elif int(qtd) == 1 and combo_get == 'Logo sem fundo até 8cm':
        corresponding_value = 108.00
        description = '      Para personalizar 1 item,\n         você deve adicionar:'

    elif 2 <= int(qtd) <= 3 and combo_get == 'Logo sem fundo até 8cm':
        corresponding_value = 36.00
        description = f'       Para personalizar {qtd} itens,\n         você deve adicionar:'

    elif 4 <= int(qtd) <= 7 and combo_get == 'Logo sem fundo até 8cm':
        corresponding_value = 15.43
        description = f'       Para personalizar {qtd} itens,\n         você deve adicionar:'

    elif 8 <= int(qtd) <= 11 and combo_get == 'Logo sem fundo até 8cm':
        corresponding_value = 9.82
        description = f'       Para personalizar {qtd} itens,\n         você deve adicionar:'

    elif int(qtd) >= 12 and combo_get == 'Logo sem fundo até 8cm':
        corresponding_value = 9.00
        description = f'       Para personalizar {qtd} itens,\n         você deve adicionar:'

    elif int(qtd) == 1 and combo_get == 'Logo sem fundo até 16cm':
        corresponding_value = 156.00
        description = '      Para personalizar 1 item,\n         você deve adicionar:'

    elif 2 <= int(qtd) <= 3 and combo_get == 'Logo sem fundo até 16cm':
        corresponding_value = 52.00
        description = f'       Para personalizar {qtd} itens,\n         você deve adicionar:'

    elif 4 <= int(qtd) <= 7 and combo_get == 'Logo sem fundo até 16cm':
        corresponding_value = 22.29
        description = f'       Para personalizar {qtd} itens,\n         você deve adicionar:'

    elif 8 <= int(qtd) <= 11 and combo_get == 'Logo sem fundo até 16cm':
        corresponding_value = 14.18
        description = f'       Para personalizar {qtd} itens,\n         você deve adicionar:'

    elif int(qtd) >= 12 and combo_get == 'Logo sem fundo até 16cm':
        corresponding_value = 13.00
        description = f'       Para personalizar {qtd} itens,\n         você deve adicionar:'

    elif int(qtd) == 1 and combo_get == 'Logo com fundo até 8cm':
        corresponding_value = 180.00
        description = '      Para personalizar 1 item,\n         você deve adicionar:'

    elif 2 <= int(qtd) <= 3 and combo_get == 'Logo com fundo até 8cm':
        corresponding_value = 60.00
        description = f'       Para personalizar {qtd} itens,\n         você deve adicionar:'

    elif 4 <= int(qtd) <= 7 and combo_get == 'Logo com fundo até 8cm':
        corresponding_value = 25.71
        description = f'       Para personalizar {qtd} itens,\n         você deve adicionar:'

    elif 8 <= int(qtd) <= 11 and combo_get == 'Logo com fundo até 8cm':
        corresponding_value = 16.36
        description = f'       Para personalizar {qtd} itens,\n         você deve adicionar:'

    elif int(qtd) >= 12 and combo_get == 'Logo com fundo até 8cm':
        corresponding_value = 15.00
        description = f'       Para personalizar {qtd} itens,\n         você deve adicionar:'

    elif int(qtd) == 1 and combo_get == 'Logo com fundo até 16cm':
        corresponding_value = 240.00
        description = '      Para personalizar 1 item,\n         você deve adicionar:'

    elif 2 <= int(qtd) <= 3 and combo_get == 'Logo com fundo até 16cm':
        corresponding_value = 80.00
        description = f'       Para personalizar {qtd} itens,\n         você deve adicionar:'

    elif 4 <= int(qtd) <= 7 and combo_get == 'Logo com fundo até 16cm':
        corresponding_value = 34.29
        description = f'       Para personalizar {qtd} itens,\n         você deve adicionar:'

    elif 8 <= int(qtd) <= 11 and combo_get == 'Logo com fundo até 16cm':
        corresponding_value = 21.82
        description = f'       Para personalizar {qtd} itens,\n         você deve adicionar:'

    elif int(qtd) >= 12 and combo_get == 'Logo com fundo até 16cm':
        corresponding_value = 20.00
        description = f'       Para personalizar {qtd} itens,\n         você deve adicionar:'

    label_result_text_area.configure(
        text=f'{description} R${corresponding_value:.2f} além\ndo valor da peça.')
    clean()
    entry_qty.focus()


def clean():
    entry_qty.delete(0, END)


if __name__ == '__main__':
    main()
