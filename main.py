import tkinter as tk
from tkinter import simpledialog, messagebox

def adicionar_categoria():
    nova_categoria = simpledialog.askstring("Nova Categoria", "Digite o nome da nova categoria:")
    if nova_categoria and nova_categoria not in categorias_organizadas:
        categorias_organizadas[nova_categoria] = []
        atualizar_categorias()

def adicionar_item():
    categoria = categoria_var.get()
    item = item_entry.get()
    if item and categoria:
        categorias_organizadas[categoria].append(item)
        item_entry.delete(0, tk.END)
        atualizar_lista()

def atualizar_categorias():
    categoria_menu['menu'].delete(0, 'end')
    for cat in categorias_organizadas.keys():
        categoria_menu['menu'].add_command(label=cat, command=lambda value=cat: categoria_var.set(value))
    categoria_var.set(next(iter(categorias_organizadas)))

def atualizar_lista():
    lista_text.delete(1.0, tk.END)
    for cat, itens in categorias_organizadas.items():
        lista_text.insert(tk.END, f"{cat}: {', '.join(itens)}\n")

root = tk.Tk()
root.title("Lista de Supermercado")

categorias_organizadas = {"Outros": []}

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

item_entry = tk.Entry(frame)
item_entry.pack(side=tk.LEFT, padx=(0, 10))

categoria_var = tk.StringVar(root)
categoria_menu = tk.OptionMenu(frame, categoria_var, *categorias_organizadas.keys())
categoria_menu.pack(side=tk.LEFT, padx=(0, 10))

botao_adicionar = tk.Button(frame, text="Adicionar Item", command=adicionar_item)
botao_adicionar.pack(side=tk.LEFT, padx=(0, 10))

botao_nova_categoria = tk.Button(frame, text="Nova Categoria", command=adicionar_categoria)
botao_nova_categoria.pack(side=tk.LEFT)

lista_text = tk.Text(root, height=10, width=50)
lista_text.pack(padx=10, pady=(0, 10))

atualizar_categorias()
root.mainloop()
