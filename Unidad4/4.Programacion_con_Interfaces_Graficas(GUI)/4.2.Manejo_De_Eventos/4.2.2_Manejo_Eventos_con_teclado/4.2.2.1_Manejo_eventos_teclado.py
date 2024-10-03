import tkinter as tk
from tkinter import messagebox

# Clase Administrador de Tareas
class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Administrador de Tareas con Atajos de Teclado")
        self.root.geometry("650x350")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.root.quit)
        self.root.bind("<Escape>", self.root.quit)
        self.root.bind("<Return>", self.add_task_event)  # Atajo para añadir tarea
        self.root.bind("c", self.complete_task_event)    # Atajo para completar tarea
        self.root.bind("<Delete>", self.delete_task_event) # Atajo para eliminar tarea

        # Color de fondo de la ventana
        self.root.configure(bg="#f9f9f9")  # Color pastel claro

        # Marco para el campo de entrada y el botón de agregar tarea
        self.input_frame = tk.Frame(self.root, bg="#fffacd")  # Color pastel suave
        self.input_frame.pack(padx=10, pady=10)

        # Defino entry para campo entrada
        self.entry = tk.Entry(self.input_frame, width=50)
        self.entry.pack(side=tk.LEFT)

        # Defino un menú al inicio de la ventana con colores personalizados
        self.menu = tk.Menu(self.root, bg="#b0e0e6", fg="black")  # Color pastel
        self.root.config(menu=self.menu)

        # Crear una opción de menú "Archivo" con una opción "Salir"
        file_menu = tk.Menu(self.menu, tearoff=0, bg="#b0e0e6", fg="black", font=("Arial", 8))
        file_menu.add_command(label="Salir", command=self.root.quit)
        self.menu.add_cascade(label="Menu", menu=file_menu)

        # Botón para agregar tarea
        self.add_task_button = tk.Button(
            self.input_frame,
            text="Agregar Tarea",
            command=self.add_task,
            font=("Arial", 8, "bold"),
            width=18,
            height=1,
            bg="#add8e6",  # Color pastel
            fg="black"     # Color de texto
        )
        self.add_task_button.pack(side=tk.LEFT, padx=5)

        # Label para indicar que se puede presionar Enter
        self.enter_label = tk.Label(
            self.root,
            text="(O presiona Enter)",
            font=("Arial", 8, "italic"),
            bg="#f9f9f9",  # Color de fondo
            fg="black"      # Color de texto
        )
        self.enter_label.place(x=460, y=40)

        # Label para el Visualizador de Tareas
        self.task_label = tk.Label(
            self.root,
            text="Visualizador de Tareas",
            font=("Arial", 10, "bold"),
            bg="#f9f9f9",  # Color de fondo
            fg="black"      # Color de texto
        )
        self.task_label.place(x=50, y=50)

        # Listbox para mostrar las tareas
        self.task_listbox = tk.Listbox(self.root, width=50, height=10, bg="#fffacd", fg="black")  # Color pastel
        self.task_listbox.place(x=50, y=80)

        # Evento de doble clic en una tarea
        self.task_listbox.bind("<Double-1>", self.complete_task_event)

        # Botón para Marcar como Completada
        self.complete_task_button = tk.Button(
            self.root,
            text="Marcar Tarea Completada",
            command=self.complete_task,
            font=("Arial", 8),
            width=18,
            height=1,
            bg="#98fb98",  # Color pastel
            fg="black"      # Color de texto
        )
        self.complete_task_button.place(x=460, y=80)

        # Label para indicar cómo completar tareas
        self.enter_label = tk.Label(
            self.root,
            text="(Doble clic en la Tarea\n O presione la letra 'c')",
            font=("Arial", 8, "italic"),
            bg="#f9f9f9",  # Color de fondo
            fg="black"      # Color de texto
        )
        self.enter_label.place(x=460, y=109)

        # Botón para Eliminar Tarea
        self.delete_task_button = tk.Button(
            self.root,
            text="Eliminar Tarea",
            command=self.delete_task,
            font=("Arial", 8),
            width=18,
            height=1,
            bg="#ffb6c1",  # Color pastel
            fg="black"      # Color de texto
        )
        self.delete_task_button.place(x=460, y=140)

        # Label para indicar cómo completar tareas
        self.enter_label = tk.Label(
            self.root,
            text="(O presione telca Supr)",
            font=("Arial", 8, "italic"),
            bg="#f9f9f9",  # Color de fondo
            fg="black"      # Color de texto
        )
        self.enter_label.place(x=460, y=169)


    # Añadir tarea con el botón
    def add_task(self):
        task = self.entry.get().strip()
        if task and not self.task_exists(task):
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
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

    # Marcar tarea como completada con el botón o atajo
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

    # Eliminar tarea
    def delete_task_event(self, event):
        self.delete_task()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task = self.task_listbox.get(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            messagebox.showinfo("Tarea Eliminada", f"Tarea: {selected_task} ha sido eliminada.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")
##
# Llamar a la función
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
