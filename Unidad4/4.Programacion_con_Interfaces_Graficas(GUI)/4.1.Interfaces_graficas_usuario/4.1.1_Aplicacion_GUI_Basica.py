import tkinter as tk

# Creación de la ventana principal
app = tk.Tk()
app.geometry('480x580')
app.title('Tarea 13: Creación de una Aplicación GUI Básica')

# Configurar el fondo de la ventana
app.configure(background='#ADD8E6')

# Función para cerrar la ventana
def cerrar():
    app.quit()

# Botón para cerrar la ventana (fondo rojo, letras blancas)
boton_salir = tk.Button(app, text='Salir', command=cerrar, width=10, height=2,
                        font=('Arial', 12, 'bold'), bg='red', fg='white', relief='raised')
boton_salir.pack(side="bottom", pady=10, padx=10)

# Función para añadir el valor del Entry a la Listbox
def mostrar_valor():
    valor_actual = entry_texto.get()  # Obtiene el texto del Entry
    if valor_actual:  # Solo añade si no está vacío
        listbox_valores.insert(tk.END, valor_actual)  # Añade el texto a la Listbox
        entry_texto.delete(0, tk.END)  # Limpia el Entry después de añadir el texto

# Botón "Mostrar Valor"
boton_mostrar = tk.Button(
    app,
    text='Agregar',
    command=mostrar_valor,
    width=10, height=1, font=('Arial', 15, 'bold'),
    bg='white',  # Fondo blanco
    fg='black'   # Texto negro
)
# Posiciona el botón en la parte superior de la ventana
boton_mostrar.pack(pady=20)  # Añade margen en la parte superior

# Label para "Ingresar texto"
label_texto = tk.Label(app, text="Ingresar texto:",
                       font=('Arial', 12), bg='#ADD8E6', fg='black')
label_texto.pack(anchor='w', padx=20)  # Alineado a la izquierda con margen

# Entry para ingresar texto
entry_texto = tk.Entry(
    app,
    font=('Arial', 12),
    width=30, bg='#F0F0F0', fg='black')
entry_texto.pack(padx=20, pady=10)  # Añade márgenes

# Listbox para mostrar los valores ingresados
listbox_valores = tk.Listbox(app,
                             height=5,
                             width=20,
                             font=('Arial', 15),
                             bg='#F0F0F0', fg='black')
listbox_valores.pack(padx=25, pady=25)  # Añade márgenes
#funcion para limpiar lista
def limpiar_lista():
    listbox_valores.delete(0, tk.END)
# Botón "Limpiar"
boton_limpiar = tk.Button(
    app,
    text='Limpiar',
    command=limpiar_lista,
    width=10, height=1, font=('Arial', 15, 'bold'),
    bg='#00008B',  # Fondo azul eléctrico
    fg='white'    # Texto blanco
)
# Posiciona el botón debajo del Entry
boton_limpiar.pack(pady=10)
app.mainloop()  # Loop para mantener la ventana abierta
