import pandas as pd
import numpy
import re
import tkinter as tk
from tkinter import ttk 

tonalidades = ['','C','Db','D','Eb','E','F','F#','Gb','G','Ab','A','Bb','B',
               'Cm','C#m','Dm','Ebm','Em','Fm','F#m','Gm','G#m','Am','A#m','Bbm','Bm']
andamentos = ['','1 - Muito lento','2 - Lento','3 - Médio','4 - Rápido','5 - Muito Rápido']
arquivo='repertorio.csv'
def open():
    global df
    tabela.delete(*tabela.get_children())
    df=pd.read_csv(arquivo)
    df_exibicao=df.sort_index(ascending=False)
    tabela['column']=list(df_exibicao.columns)
    tabela['show']= 'headings'
    for col in tabela['column']:
        tabela.column(col,anchor='center', stretch=False, width=100)
        tabela.heading(col, text=col)
    linhas=df_exibicao.to_numpy().tolist()
    for linha in linhas:
        tabela.insert('','end',values=linha)

def cadastrar():
    janela_cadastro()

def deletar():
    global df
    selected_item = tabela.selection()[0]
    nome=tabela.item(selected_item,'values')[0]
    df=df.loc[df['nome'] != nome]
    df.to_csv('repertorio.csv', index=False)
    tabela.delete(selected_item)
    


def janela_consultar():
    global tabela
    janela_consulta=tk.Tk()
    janela_consulta.title('Consulta de músicas')
    janela_consulta.geometry('900x900')

    botao=tk.Button(janela_consulta,text='Cadastrar Nova Música',command=cadastrar)
    botao.pack(pady=20)
    botao=tk.Button(janela_consulta,text='Deletar',command=deletar)
    botao.pack(pady=20)
    tabela=ttk.Treeview(janela_consulta, selectmode='browse')
    tabela.pack(side ='left')
    tabela.heading('#0', text='\n')
    tabela['height']=20
    scrlbar = ttk.Scrollbar(janela_consulta, orient ="vertical", command = tabela.yview)
    scrlbar.pack(side ='right')
    tabela.configure(xscrollcommand = scrlbar.set)
    open() 
    janela_consulta.mainloop()



#--------------------------

def salvar_cadastro():
    global df
    novo_cadastro= {'nome':insert_nome.get(), 'tom':insert_tom.get(),'compositor':insert_compositor.entry.get(),
                     'artista':insert_artista.entry.get(),'genero':insert_genero.entry.get(),
                     'subgenero':insert_subgenero.entry.get(),'andamento':insert_andamento.get(),
                     'clima':insert_clima.entry.get(),'tema':insert_tema.entry.get()}
    
    df = df._append(novo_cadastro,ignore_index=True)
    df.to_csv(arquivo,index=False)
    tabela.insert('',index=0,values=[insert_nome.get(),insert_tom.get(),insert_compositor.entry.get(),insert_artista.entry.get(),
                                     insert_genero.entry.get(),insert_subgenero.entry.get(),insert_andamento.get(),
                                     insert_clima.entry.get(),insert_tema.entry.get()])



class EntryLimit(tk.Entry):
    def __init__(self, master, limit, width=10):
        self.limit_var=limit
        tk.Entry.__init__(self, master=master, width=width)
        self.var=tk.StringVar()
        self.var.trace_add(mode='write', callback=self.valida_entry)
        self['textvariable']=self.var
    def valida_entry(self, name, index, mode):
        if len(self.var.get())>0:
            self.var.set(self.var.get()[:self.limit_var])



class MeuComboBox():
    def __init__(self, master, limit, dados, width=10):
        self.dados=dados
        self.limit=limit
        self.width=width
        self.janela=master
        self.data=[]
        self.var_str=tk.StringVar()
        self.var_str.trace_add(mode='write', callback=self.valida)
    
    def pack(self):
        self.frame=tk.Frame(self.janela)
        self.frame.pack()
        self.entry=ttk.Combobox(self.frame, width=self.width, values=self.dados,textvariable=self.var_str)
        self.entry.pack()
        self.list_box=tk.Listbox(self.frame, listvariable=self.data, height=0, width=self.width, selectmode='browse', activestyle='dotbox')
        self.list_box.bind('<<ListboxSelect>>',self.clica_lista)
                
    def clica_lista(self,evt):
        try:
            selecionado=self.list_box.curselection()
            self.entry.set(self.list_box.get(selecionado))
            self.entry.focus()
            self.list_box.pack_forget()
        except:
            self.list_box.pack_forget()
    
    def valida(self,var,index,write):
        self.list_box.delete(0, tk.END)
        if len(self.var_str.get())==0:
            self.list_box.pack_forget()
            self.entry['values']=self.dados
        elif len(self.var_str.get())>0:
            self.entry.set(self.entry.get()[:self.limit])
            data=[]
            indice_lista=0
            for compositor in self.dados:
                if compositor.lower().startswith(self.var_str.get().lower()):
                    data.append(compositor)
                    self.list_box.pack()
                    self.list_box.insert(indice_lista, compositor)
                    indice_lista+=1
            if data == []:
                self.entry['values']=self.dados
                self.list_box.pack_forget()
            else:
                self.entry['values']=data

    

def janela_cadastro():
    global insert_nome, insert_tom, insert_compositor, insert_artista, insert_genero, insert_subgenero, insert_andamento, insert_clima, insert_tema
    janela=tk.Toplevel()
    janela.grab_set()
    janela.title('Cadastro de nova música')
    janela.geometry('900x900')



    label_nome=tk.Label(janela,text='Nome da música')
    label_nome.pack()
    insert_nome=EntryLimit(master=janela,width=55,limit=50)
    insert_nome.pack(pady=5)

    label_tom=tk.Label(janela,text='Tom')
    label_tom.pack()
    insert_tom=ttk.Combobox(janela, values=tonalidades, state='readonly',width=5)
    insert_tom.pack(pady=5)



    janela_compositor=tk.Frame(janela)
    janela_compositor.pack()
    label_compositor=tk.Label(janela_compositor,text='Compositor')
    label_compositor.pack()
    insert_compositor=MeuComboBox(master=janela_compositor, limit=50, width=55, dados=df['compositor'].unique().tolist())
    insert_compositor.pack()
    

    janela_artista=tk.Frame(janela)
    janela_artista.pack()
    label_artista=tk.Label(janela_artista,text='Artista')
    label_artista.pack()
    insert_artista=MeuComboBox(master=janela_artista, limit=50, width=55, dados=df['artista'].unique().tolist())
    insert_artista.pack()

    janela_genero=tk.Frame(janela)
    janela_genero.pack()
    label_genero=tk.Label(janela_genero,text='Gênero')
    label_genero.pack()
    insert_genero=MeuComboBox(master=janela_genero, limit=50, width=55, dados=df['genero'].unique().tolist())
    insert_genero.pack()

    janela_subgenero=tk.Frame(janela)
    janela_subgenero.pack()
    label_subgenero=tk.Label(janela_subgenero,text='Sub-Gênero')
    label_subgenero.pack()
    insert_subgenero=MeuComboBox(master=janela_subgenero, limit=50, width=55, dados=df['subgenero'].unique().tolist())
    insert_subgenero.pack()


    label_andamento=tk.Label(janela,text='Andamento')
    label_andamento.pack(pady=5)
    insert_andamento=ttk.Combobox(janela, values=andamentos, state='readonly')
    insert_andamento.pack(pady=10)

    janela_clima=tk.Frame(janela)
    janela_clima.pack()
    label_clima=tk.Label(janela_clima,text='Clima')
    label_clima.pack()
    insert_clima=MeuComboBox(master=janela_clima, limit=50, width=55, dados=df['clima'].unique().tolist())
    insert_clima.pack()

    janela_tema=tk.Frame(janela)
    janela_tema.pack()
    label_tema=tk.Label(janela_tema,text='Tema')
    label_tema.pack()
    insert_tema=MeuComboBox(master=janela_tema, limit=50, width=55, dados=df['tema'].unique().tolist())
    insert_tema.pack()

    botao=tk.Button(janela,text='Salvar nova música',command=salvar_cadastro)
    botao.pack(pady=20)
    janela.mainloop()
janela_consultar()
        




