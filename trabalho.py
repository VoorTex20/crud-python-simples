import psycopg2
from tkinter import *
 
conexao = psycopg2.connect(
    host= "localhost",
    database= "python2",
    user= "postgres",
    password= "JoaoVini.20",
 )
cu = conexao.cursor()

def criarTabela():
    cu.execute("create table funcionarios"
                '(nome varchar(20))'
              )
    conexao.commit()

def InsereNomeTabela():
    nomeDigitado = entrada.get()
    sql = """INSERT INTO funcionarios (nome) values (%s)"""
    
    print(sql, nomeDigitado)
    cu.execute(sql, (nomeDigitado,))
    conexao.commit()

def DeleteNomeTabela():
    nomeDigitado = entrada.get()
    sql = """DELETE FROM funcionarios where nome = %s"""
    
    print(sql, nomeDigitado)
    cu.execute(sql, (nomeDigitado,))
    conexao.commit()

def UpdateNomeTabela():
    UpdateNome = entrada.get()
    nomeDigitado = entrada_update.get()
    sql = """UPDATE funcionarios set nome = %s where nome = %s"""
    print(sql, nomeDigitado)
    cu.execute(sql, (UpdateNome, nomeDigitado,))
    conexao.commit()

def amostrartudo():
    cu.execute('SELECT * FROM funcionarios')
    registros = cu.fetchall()
    dados = "\n".join([f"nome: {registro[0]}"for registro in registros])
    label_dados["text"] = dados

root = Tk()


entrada = Entry(root)
entrada.pack(pady=5)


botao = Button(root, text="enviar nome", command= InsereNomeTabela)
botao.pack(pady=5)

botao_delete = Button(root, text="Deletar nome", command= DeleteNomeTabela)
botao_delete.pack(pady=5)

entrada_update = Entry(root)
entrada_update.pack(pady=5)

botao_update = Button(root, text="Novo nome", command= UpdateNomeTabela)
botao_update.pack(pady=5)

label_dados = Label(root, text="", wraplength=300)
label_dados.pack(pady=5)

tudobanco = Button(root, text='selecionar todos', command=amostrartudo)
tudobanco.pack(pady=5)

root.geometry("250x250")

root.mainloop()
 
criarTabela()

