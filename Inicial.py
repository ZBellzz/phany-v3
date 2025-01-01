from tkinter import *
import consulta
import cadastro


def abrir_cadrastro():
    import subprocess
    subprocess.Popen(["python", "cadastro.py"])
    root.destroy()

def abrir_consulta():
    import subprocess
    subprocess.Popen(["python", "consulta.py"])
    root.destroy()
    
def sair():
    root.destroy()

root = Tk()
root.configure(bg='#1c1c1c')
root.title('Tela inicial')
root.attributes('-fullscreen',True)

botão_cadrastro = Button(text='cadastro', bg='#1c1c1c', fg='white', font='Arial 30', command=abrir_cadrastro)
botão_cadrastro.place(relx=0.5, rely=0.3, anchor= 'center')

botão_consulta = Button(text='consulta', bg='#1c1c1c', fg='white', font='Arial 30',command= abrir_consulta)
botão_consulta.place(relx=0.5, rely=0.6, anchor= 'center')

butao_sair = Button(height=2, width=9, text='Sair',bg='#1c1c1c',fg='white', font='Arial 20', command= sair)
butao_sair.place(relx=0.90, rely=0.90, anchor= 'w')

root.mainloop()