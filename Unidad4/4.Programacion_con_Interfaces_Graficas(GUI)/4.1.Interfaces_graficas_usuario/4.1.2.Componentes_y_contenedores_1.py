import tkinter as tk
from tkinter import ttk, messagebox

# Función para cerrar la ventana
def close_window():
    app.destroy()

# Función para cambiar el color del botón cuando el ratón esté sobre él
def on_hover(event):
    close_button.config(bg="white", fg="black")  # Cambia el color cuando esté encima

# Función para regresar el color original cuando el ratón salga del botón
def on_leave(event):
    close_button.config(bg="#00008B", fg="white")  # Restablece los colores cuando salga el ratón

# Función para agregar una tarea nueva a la lista
def agregar_evento():
    fecha = entry_fecha.get()  # Obtiene el valor del campo de fecha
    hora = entry_hora.get()    # Obtiene el valor del campo de hora
    descripcion = entry_descripcion.get()  # Obtiene el valor de la descripción

    if fecha and hora and descripcion:  # Si todos los campos están llenos
        treeview.insert('', 'end', values=(fecha, hora, descripcion))  # Agrega la tarea a la lista
        entry_fecha.delete(0, tk.END)  # Limpia el campo de fecha
        entry_hora.delete(0, tk.END)   # Limpia el campo de hora
        entry_descripcion.delete(0, tk.END)  # Limpia el campo de descripción
    else:
        messagebox.showwarning("Campos incompletos", "Por favor, llena todos los campos")

# Función para eliminar el evento seleccionado
def eliminar_evento():
    seleccion = treeview.selection()  # Obtiene el elemento seleccionado en la lista
    if seleccion:
        treeview.delete(seleccion)  # Elimina el elemento seleccionado
    else:
        messagebox.showwarning("Selección Vacía", "Por favor selecciona una tarea para eliminar")

# Crear la ventana principal
app = tk.Tk()
app.geometry('600x580')
app.title('Tarea 14: Componentes y Contenedores')
app.configure(background='#ADD8E6')  # Configurar el fondo de la ventana

# Atributos adicionales para la ventana
app.attributes("-topmost", True)  # Siempre encima
app.attributes("-alpha", 0.9)  # Transparencia

# Crear el TreeView para mostrar las tareas
treeview = ttk.Treeview(app, columns=("Fecha", "Hora", "Descripción"), show="headings")
treeview.heading("Fecha", text="Fecha")
treeview.heading("Hora", text="Hora")
treeview.heading("Descripción", text="Descripción")
treeview.pack(pady=20, fill=tk.BOTH, expand=True)  # Expande el TreeView para que llene el espacio disponible

# Etiquetas y campos de entrada para agregar nuevas tareas
label_fecha = tk.Label(app, text="Fecha (dd/mm/yyyy):", bg='#ADD8E6')
label_fecha.pack()
entry_fecha = tk.Entry(app)
entry_fecha.pack()

label_hora = tk.Label(app, text="Hora (HH:MM):", bg='#ADD8E6')
label_hora.pack()
entry_hora = tk.Entry(app)
entry_hora.pack()

label_descripcion = tk.Label(app, text="Descripción de la Tarea:", bg='#ADD8E6')
label_descripcion.pack()
entry_descripcion = tk.Entry(app)
entry_descripcion.pack()

# Botones de acción
boton_agregar = tk.Button(app, text="Agregar Evento", command=agregar_evento)
boton_agregar.pack(pady=10)

boton_eliminar = tk.Button(app, text="Eliminar Evento Seleccionado", command=eliminar_evento)
boton_eliminar.pack(pady=10)

# Crear un botón "Salir"
close_button = tk.Button(app, text="Salir", font=("Helvetica", 12), bg="#6e7b84", fg="white", bd=1, command=close_window,
                         highlightbackground="white", highlightthickness=1)  # Borde verde
close_button.pack(side="bottom", pady=20)  # Posicionar en la parte inferior con margen

# Configurar tamaño del botón "Salir"
close_button.config(width=10, height=1)

# Agregar eventos de hover (cuando el ratón esté sobre el botón "Salir")
close_button.bind("<Enter>", on_hover)
close_button.bind("<Leave>", on_leave)

app.mainloop()  # Loop para mantener la ventana abierta
