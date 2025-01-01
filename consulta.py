from tkinter import *
from tkinter import messagebox

def busca_arquivo():
    try:
        Nome_arquivo = entry_consulta.get()
        
       
        with open(f'{Nome_arquivo}.txt', 'r') as file:
            conteudo = file.read()
        
       
        text_area.delete(1.0, END) 
        text_area.insert(END, conteudo) 
        label_arquivo_info.config(text=f"Arquivo: {Nome_arquivo}.txt")
        
    except FileNotFoundError:
        messagebox.showerror('Erro', 'Nome do arquivo informado está errado ou não existe')
        return

def salvar_arquivo():
    Nome_arquivo = entry_consulta.get()
    conteudo = text_area.get(1.0, END)
    
    try:
        with open(f'{Nome_arquivo}.txt', 'w') as file:
            file.write(conteudo)
        messagebox.showinfo('Sucesso', 'Arquivo salvo com sucesso!')
    except Exception as e:
        messagebox.showerror('Erro', f'Ocorreu um erro ao salvar o arquivo: {str(e)}')

def voltar():
    import subprocess
    subprocess.Popen(["python", "inicial.py"])
    root.destroy()

def abrir_pesquisa():
    # Cria uma nova janela para pesquisa
    pesquisa_window = Toplevel(root)
    pesquisa_window.title("Pesquisar Palavra")
    pesquisa_window.geometry("400x200")
    
    label_pesquisa = Label(pesquisa_window, text="Digite a palavra para pesquisar:", font='Arial 14')
    label_pesquisa.pack(pady=10)
    
    entry_pesquisa = Entry(pesquisa_window, font='Arial 14')
    entry_pesquisa.pack(pady=10)
    
    def realizar_busca():
        palavra = entry_pesquisa.get()
        if palavra:
            # Tenta abrir o arquivo e buscar as ocorrências
            Nome_arquivo = entry_consulta.get()
            try:
                with open(f'{Nome_arquivo}.txt', 'r') as file:
                    conteudo = file.read()  # Lê todo o conteúdo do arquivo
                
                # Divida o conteúdo em blocos usando linhas vazias como delimitadores
                blocos = [bloco.strip() for bloco in conteudo.split('\n\n') if bloco.strip()]
                
                # Busca o bloco que contém a palavra
                encontrado = False
                for bloco in blocos:
                    if palavra.lower() in bloco.lower():  # Busca pela palavra (case-insensitive)
                        # Encontrou o bloco com a palavra
                        pos_window = Toplevel(pesquisa_window)
                        pos_window.title("Bloco Encontrado")
                        pos_window.geometry("600x400")
                        
                        label_posicoes = Label(pos_window, text=f"Conteúdo do bloco com '{palavra}':", font='Arial 14')
                        label_posicoes.pack(pady=10)

                        text_posicoes = Text(pos_window, font='Arial 12', height=15, width=70)
                        text_posicoes.pack(pady=10)
                        
                        # Exibe o conteúdo do bloco
                        text_posicoes.insert(END, bloco)
                        text_posicoes.config(state=DISABLED)  # Desabilita a edição da área de texto
                        
                        encontrado = True
                        break
                
                if not encontrado:
                    messagebox.showinfo("Resultado", f"Palavra '{palavra}' não encontrada.")
                
            except FileNotFoundError:
                messagebox.showerror('Erro', 'Nome do arquivo informado está errado ou não existe')
                return
        else:
            messagebox.showwarning('Aviso', 'Por favor, insira uma palavra para buscar.')

    # Botão para realizar a busca
    botao_buscar = Button(pesquisa_window, text="Pesquisar", font='Arial 14', command=realizar_busca)
    botao_buscar.pack(pady=10)
    
    # Botão de fechar
    botao_fechar = Button(pesquisa_window, text="Fechar", font='Arial 14', command=pesquisa_window.destroy)
    botao_fechar.pack(pady=10)

root = Tk()
root.config(bg='#1c1c1c')
root.title('Consulta')
root.attributes('-fullscreen', True)

# Labels e entrada
label_consulta = Label(text='Consulta:', font='Arial 20', bg='#1c1c1c', fg='white')
label_consulta.place(relx=0.3, rely=0.1)
entry_consulta = Entry(font='Arial 20', bg='#1c1c1c', fg='white')
entry_consulta.place(relx=0.5, rely=0.1)

# Botões
butao_confirmar = Button(height=1, width=12, text='Buscar Arquivo', bg='#1c1c1c', fg='white', font='Arial 20', command=busca_arquivo)
butao_confirmar.place(relx=0.43, rely=0.2)

# Botão para abrir a janela de pesquisa
butao_pesquisar = Button(height=1, width=12, text='Pesquisar', bg='#1c1c1c', fg='white', font='Arial 20', command=abrir_pesquisa)
butao_pesquisar.place(relx=0.61, rely=0.2)

# Área de texto para exibir e editar conteúdo
text_area = Text(root, font='Arial 16', height=20, width=50, bg='#1c1c1c', fg='white', wrap=WORD)
text_area.place(relx=0.5, rely=0.56, anchor='center')

# Label para mostrar nome do arquivo
label_arquivo_info = Label(text='', font='Arial 16', bg='#1c1c1c', fg='white')
label_arquivo_info.place(relx=0.5, rely=0.85, anchor='center')

# Botão de salvar
butao_salvar = Button(height=1, width=12, text='Salvar', bg='#1c1c1c', fg='white', font='Arial 20', command=salvar_arquivo)
butao_salvar.place(relx=0.43, rely=0.86)

# Voltar tela
butao_voltar = Button(height=2, width=9, text='Voltar', bg='#1c1c1c', fg='white', font='Arial 20', command=voltar)
butao_voltar.place(relx=0.90, rely=0.90, anchor='w')

root.mainloop()
