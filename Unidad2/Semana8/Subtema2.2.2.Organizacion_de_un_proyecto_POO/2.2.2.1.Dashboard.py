import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': '/home/lubuntu/PycharmProjects/Programacion_Orientada_a_Objetos/Unidad1/Semana2/1.2.Tecnicas_de_programacion/1.2.1.ABSTRACCION.py',
        '2': '/home/lubuntu/PycharmProjects/Programacion_Orientada_a_Objetos/Unidad1/Semana2/1.2.Tecnicas_de_programacion/1.2.2.HERENCIA.py',
        '3': '/home/lubuntu/PycharmProjects/Programacion_Orientada_a_Objetos/Unidad1/Semana2/1.2.Tecnicas_de_programacion/1.2.3.ENCAPSULAMIENTO.py',
        '4': '/home/lubuntu/PycharmProjects/Programacion_Orientada_a_Objetos/Unidad1/Semana2/1.2.Tecnicas_de_programacion/1.2.4.POLIMORFISMO.py',
        '5': '/home/lubuntu/PycharmProjects/Programacion_Orientada_a_Objetos/Unidad1/Semana3/2.1.POO_Frente_a_Programacion_Tradicional/2.1.1.Clase_Temporal_POO.py',
        '6': '/home/lubuntu/PycharmProjects/Programacion_Orientada_a_Objetos/Unidad1/Semana3/2.1.POO_Frente_a_Programacion_Tradicional/2.1.2.Funcion_Temporal_Tradicional.py',
        '7': '/home/lubuntu/PycharmProjects/Programacion_Orientada_a_Objetos/Unidad1/Semana4/2.2.Caracteristicas_de_la_POO/2.2.1.Ejmplo_Mundo_Real/2.2.1.1.Mundo_Real_Viajes.py',
        '8': '/home/lubuntu/PycharmProjects/Programacion_Orientada_a_Objetos/Unidad2/Semana5/1.1_Tipos_de_datos_Identificadores.py',
        '9': '/home/lubuntu/PycharmProjects/Programacion_Orientada_a_Objetos/Unidad2/Semana6/2_1_Clase_objetos_herencia_encapsulamoto_polimorfismo.py',
        '10': '/home/lubuntu/PycharmProjects/Programacion_Orientada_a_Objetos/Unidad2/Semana7/Tema2.2.Constructores_y_Destructores/2.2.1_Constuctor_Destructor.py',
        '11': '/home/lubuntu/PycharmProjects/Programacion_Orientada_a_Objetos/Unidad2/Semana8/Subtema2.2.2.Organizacion_de_un_proyecto_POO/2.2.2.1.Dashboard.py',

        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
