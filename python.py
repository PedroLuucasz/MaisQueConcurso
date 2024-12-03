import tkinter as tk

# Função para abrir o menu


def abrir_menu():
    menu_frame.pack(fill='both', expand=True)
    overlay_frame.pack(fill='both', expand=True)

# Função para fechar o menu


def fechar_menu(event=None):
    menu_frame.pack_forget()
    overlay_frame.pack_forget()


# Cria a janela principal
root = tk.Tk()
root.geometry('300x500')  # Tamanho da janela

# Botão para abrir o menu
btn_menu = tk.Button(root, text="Abrir Menu", command=abrir_menu)
btn_menu.pack(pady=20)

# Frame do menu
menu_frame = tk.Frame(root, bg="lightgray", width=200, height=500)
menu_frame.bind("<Button-1>", fechar_menu)  # Fecha ao clicar no próprio menu

# Overlay (fundo escuro)
overlay_frame = tk.Frame(root, bg="black", width=300, height=500)
overlay_frame.bind("<Button-1>", fechar_menu)  # Fecha ao clicar no overlay
overlay_frame.lower()  # Coloca o overlay atrás do menu

# Executa o loop da aplicação
root.mainloop()
