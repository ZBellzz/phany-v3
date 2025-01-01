from tkinter import *
import unicodedata



def ler_pedidos(nome_arquivo):
    try:
        with open(f'{nome_arquivo}.txt', 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        return []

def salvar_pedidos(pedidos, nome_arquivo):
    with open(f'{nome_arquivo}.txt', 'w') as f:
        f.writelines(pedidos)
        
def atualizar_lista_pedidos(lista_pedidos, nome_arquivo):
    lista_pedidos.delete(0, END)
    pedidos = ler_pedidos(nome_arquivo)
    for pedido in pedidos:
        lista_pedidos.insert(END, pedido.strip())


def adicionar_pedido(nome, escola_ou_empresa, data_entrega, itens, lista_pedidos, nome_arquivo):
    pedidos = ler_pedidos(nome_arquivo)
    pedido = f'{nome}\nTelefone: {escola_ou_empresa}\nData de Entrega: {data_entrega}\n'
    for item in itens:
        pedido += f'{item}\n'
    pedidos.append(pedido + '\n')
    salvar_pedidos(pedidos, nome_arquivo)
    atualizar_lista_pedidos(lista_pedidos, nome_arquivo)

# Cadastro de pedidos
def cadastrar_pedido(entry_nome, entry_telefone, entry_data_entrega, entry_itens, lista_pedidos, entry_arquivo):
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    data_entrega = entry_data_entrega.get()
    itens = entry_itens.get("1.0", END).strip().split("\n")
    nome_arquivo = entry_arquivo.get()  # Pega o nome do arquivo do campo de entrada
    nome_arquivo = nome_arquivo.title()
    nome_arquivo = ''.join(
    c for c in unicodedata.normalize('NFD', nome_arquivo) if unicodedata.category(c) != 'Mn'
)
    
    if nome_arquivo == "":  # Verifica se o nome do arquivo está vazio
        print("Por favor, insira o nome do arquivo.")  # Você pode adicionar uma mensagem de erro aqui
        return
    
    adicionar_pedido(nome, telefone, data_entrega, itens, lista_pedidos, nome_arquivo)
    entry_nome.delete(0, END)
    entry_telefone.delete(0, END)
    entry_data_entrega.delete(0, END)
    entry_itens.delete("1.0", END)
    entry_arquivo.delete(0, END)


# Processo
def voltar():
    import subprocess
    subprocess.Popen(["python", "inicial.py"])
    root.destroy()

# Configuração da tela
root = Tk()
root.title("Sistema de Pedidos - Loja de Uniformes Escolares")
root.config(bg='#1c1c1c')
root.attributes('-fullscreen', True)

# Arquivo
label_arquivo = Label(root, text="Nome arquivo:", font='Arial 20', bg='#1c1c1c', fg='white')
label_arquivo.place(relx=0.3, rely=0.05)
entry_arquivo = Entry(root, font='Arial 20', bg='#1c1c1c', fg='white')
entry_arquivo.place(relx=0.5, rely=0.05)

# Nome
label_nome = Label(root, text="Nome do Cliente:", font='Arial 20', bg='#1c1c1c', fg='white')
label_nome.place(relx=0.3, rely=0.1)
entry_nome = Entry(root, font='Arial 20', bg='#1c1c1c', fg='white')
entry_nome.place(relx=0.5, rely=0.1)

# Telefone
label_telefone = Label(root, font='Arial 20', bg='#1c1c1c', fg='white', text="Telefone:")
label_telefone.place(relx=0.3, rely=0.15)
entry_telefone = Entry(root, font='Arial 20', bg='#1c1c1c', fg='white')
entry_telefone.place(relx=0.5, rely=0.15)

# Data
label_data_entrega = Label(root, font='Arial 20', bg='#1c1c1c', fg='white', text="Data de Entrega:")
label_data_entrega.place(relx=0.3, rely=0.20)
entry_data_entrega = Entry(root, font='Arial 20', bg='#1c1c1c', fg='white')
entry_data_entrega.place(relx=0.5, rely=0.20)

# Pedidos
lista_pedidos = Listbox(root, font='Arial 20', bg='#1c1c1c', fg='white', width=44, height=10)
lista_pedidos.place(relx=0.31, rely=0.6)

label_itens = Label(root, font='Arial 20', bg='#1c1c1c', fg='white', text="Pedido:")
label_itens.place(relx=0.3, rely=0.25)
entry_itens = Text(root, font='Arial 15', bg='#1c1c1c', fg='white', height=11, width=27)
entry_itens.place(relx=0.5, rely=0.25)

# --- Botões ---
# Botão cadastro
btn_cadastrar = Button(root, font='Arial 15', bg='#1c1c1c', fg='white', text="Cadastrar Pedido", width=60, command=lambda: cadastrar_pedido(entry_nome, entry_telefone, entry_data_entrega, entry_itens, lista_pedidos, entry_arquivo))
btn_cadastrar.place(relx=0.31, rely=0.55)

# Voltar tela
butao_voltar = Button(height=2, width=9, text='Voltar', bg='#1c1c1c', fg='white', font='Arial 20', command=voltar)
butao_voltar.place(relx=0.90, rely=0.90, anchor='w')

root.mainloop()
