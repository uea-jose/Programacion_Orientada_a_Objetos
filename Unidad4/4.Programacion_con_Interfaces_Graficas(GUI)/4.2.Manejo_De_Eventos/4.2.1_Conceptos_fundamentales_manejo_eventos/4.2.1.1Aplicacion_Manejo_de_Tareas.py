import tkinter as tk
from tkinter import messagebox


# Clase Administrador de Tareas
class Task_Manager:
    def __init__(self, root):
        self.root = root
        self.root.title("Administrador de Tareas")
        self.root.geometry("650x500")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.root.quit)
        self.root.bind("<Escape>", self.root.quit)

        # Marco para el campo de entrada y el botón de agregar tarea
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(padx=10, pady=10)

        # Defino entry para campo entrada
        self.entry = tk.Entry(self.input_frame, width=50)
        self.entry.pack(side=tk.LEFT)

        #Defino un menu al inicio de la ventana
        self.menu = tk.Menu(self.root)
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
            font=("Arial", 8),  # Cambia el tamaño de letra aquí
            width=18,
            height=1  # Ajusta la altura del botón
        )
        self.add_task_button.pack(side=tk.LEFT, padx=5)

        # Botón para Marcar como Completada, usando 'place' para posicionar
        self.complete_task_button = tk.Button(
            self.root,
            text="Marcar Tarea Completada",
            command=self.complete_task,
            font=("Arial", 8),  # Cambia el tamaño de letra aquí
            width=18,
            height=1  # Ajusta la altura del botón
        )
        # Mover el botón a la posición del cuadro rojo (coordenadas ajustadas)
        self.complete_task_button.place(x=460, y=45)  # Ajusta estas coordenadas según sea necesario

        # Botón para Eliminar Tarea
        self.delete_task_button = tk.Button(
            self.root,
            text="Eliminar Tarea",
            command=self.delete_task,
            font=("Arial", 8),  width=18, height=1

        )
        #mover boton a la posicio bajo del botn Marcar Tarea Completada"
        self.delete_task_button.place(x=460, y=80)

    def add_task(self):
        task = self.entry.get()
        if task:
            messagebox.showinfo("Tarea Agregada", f"Tarea: {task}")
            self.entry.delete(0, tk.END)  # Limpiar el campo de entrada

    def complete_task(self):
        messagebox.showinfo("Tarea Completada", "Tarea marcada como completada.")

    #funcion para mensaje de Tarea fue ELiminada
    def delete_task(self):
        messagebox.showinfo("Tarea Eliminada", f"Tarea: {self.entry.get()}")







# Llamar a la función
if __name__ == "__main__":
    root = tk.Tk()
    app = Task_Manager(root)
    root.mainloop()
