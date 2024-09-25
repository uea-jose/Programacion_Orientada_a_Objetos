import tkinter as tk
from tkinter import messagebox

# Clase Administrador de Tareas
class Task_Manager:
    def __init__(self, root):
        self.root = root
        self.root.title("Administrador de Tareas")
        self.root.geometry("650x350")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.root.quit)
        self.root.bind("<Escape>", self.root.quit)

        # Marco para el campo de entrada y el botón de agregar tarea
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(padx=10, pady=10)

        # Defino entry para campo entrada
        self.entry = tk.Entry(self.input_frame, width=50)
        self.entry.pack(side=tk.LEFT)

        # Bind del evento 'Enter' para agregar la tarea
        self.entry.bind("<Return>", self.add_task_event)

        # Defino un menú al inicio de la ventana
        self.menu = tk.Menu(self.root, bg="#808080", fg="white",)
        self.root.config(menu=self.menu)

        # Crear una opción de menú "Archivo" con una opción "Salir"
        menu = tk.Menu(self.menu, tearoff=0)
        menu.add_command(label="Salir", command=self.root.quit)
        self.menu.add_cascade(label="Menu", menu=menu)

        # Botón para agregar tarea
        self.add_task_button = tk.Button(
            self.input_frame,
            text="Agregar Tarea",
            command=self.add_task,
            font=("Arial", 8, "bold"),  # Cambia el tamaño de letra aquí
            width=18,
            height=1  # Ajusta la altura del botón
        )
        self.add_task_button.pack(side=tk.LEFT, padx=5)

        # Label para indicar que se puede presionar Enter
        self.enter_label = tk.Label(
            self.root,
            text="(O presiona Enter)",  # Texto del label
            font=("Arial", 8, "italic")  # Cambiar tamaño y estilo de fuente a itálica
        )
        self.enter_label.place(x=460, y=40)  # Ubicación debajo del botón

        # Label para el Visualizador de Tareas (en negrita)
        self.task_label = tk.Label(
            self.root,
            text="Visualizador de Tareas",
            font=("Arial", 10, "bold")  # Negrita con el parámetro "bold"
        )
        self.task_label.place(x=50, y=50)

        # Listbox para mostrar las tareas
        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.place(x=50, y=80)

        # Bind del evento de doble clic en una tarea
        self.task_listbox.bind("<Double-1>", self.complete_task_event)

        # Botón para Marcar como Completada
        self.complete_task_button = tk.Button(
            self.root,
            text="Marcar Tarea Completada",
            command=self.complete_task,
            font=("Arial", 8),
            width=18,
            height=1  # Ajusta la altura del botón
        )

        self.complete_task_button.place(x=460, y=80)
        # Label para indicar que se puede presionar Enter
        self.enter_label = tk.Label(
            self.root,
            text="(O doble click en la Tarea)",  # Texto del label
            font=("Arial", 8, "italic")  # Cambiar tamaño y estilo de fuente a itálica
        )
        self.enter_label.place(x=460, y=110)  # Ubicación debajo del botón

        # Botón para Eliminar Tarea
        self.delete_task_button = tk.Button(
            self.root,
            text="Eliminar Tarea",
            command=self.delete_task,
            font=("Arial", 8), width=18, height=1
        )
        self.delete_task_button.place(x=460, y=140)

    # Añadir tarea con el botón
    def add_task(self):
        task = self.entry.get().strip()
        if task and not self.task_exists(task):
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "La tarea ya existe o está vacía.")

    # Añadir tarea con la tecla Enter
    def add_task_event(self, event):
        self.add_task()

    # Función para comprobar si una tarea ya existe en la lista
    def task_exists(self, task):
        tasks = self.task_listbox.get(0, tk.END)
        return task in tasks

    # Marcar tarea como completada al hacer doble clic
    def complete_task_event(self, event):
        self.complete_task()

    # Marcar tarea como completada con el botón
    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task = self.task_listbox.get(selected_task_index)

            # Verificar si la tarea ya ha sido completada
            if "✓" not in selected_task:
                completed_task = f"{selected_task} ✓"
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, completed_task)
                messagebox.showinfo("Tarea Completada", f"Tarea: {selected_task} marcada como completada.")
            else:
                messagebox.showwarning("Advertencia", "La tarea ya está marcada como completada.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")
#
    # Eliminar tarea
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task = self.task_listbox.get(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            messagebox.showinfo("Tarea Eliminada", f"Tarea: {selected_task} ha sido eliminada.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

# Llamar a la función
if __name__ == "__main__":
    root = tk.Tk()
    app = Task_Manager(root)
    root.mainloop()
