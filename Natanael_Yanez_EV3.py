class Libreria:
    def __init__(self):
        self.libros = []
        self.ventas = []

    def registrar_libro(self):
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        genero = input("Ingrese el género del libro: ")
        precio = float(input("Ingrese el precio del libro: "))

        if titulo and autor and genero and precio:
            libro = [titulo, autor, genero, precio]
            self.libros.append(libro)
            print("Libro registrado. ")
        else:
            print("Error todos los campos son obligatorios.")

    def listar_libros(self):
        if self.libros:
            print("Lista de libros.:")
            for libro in self.libros:
                print(f"Título: {libro[0]}, Autor: {libro[1]}, Género: {libro[2]}, Precio: {libro[3]}")
        else:
            print("No hay libros registrados.")

    def registrar_venta(self):
        titulo = input("Ingrese el título del libro vendido: ")
        for libro in self.libros:
            if libro[0] == titulo:
                self.ventas.append(libro)
                print("Venta registrada con éxito.")
                return
        print("Error: Libro no encontrado.")

    def imprimir_reporte_ventas(self):
        if self.ventas:
            print("Reporte de ventas:")
            for libro in self.ventas:
                print(f"Título: {libro[0]}, Autor: {libro[1]}, Género: {libro[2]}, Precio: {libro[3]}")
        else:
            print("No hay ventas registradas.")

    def generar_txt(self):
        with open("VentasLibros.txt", "w") as f:
            for libro in self.ventas:
                f.write(f"{libro[0]},{libro[1]},{libro[2]},{libro[3]}\n")
        print("Archivo generado con éxito")
        
#Aqui el Archivo TXT lo manda para el Disco Local C despues en Usuarios y el Usuario donde se esté ejecutando el codigo y tiene de nombre "VentasLibros".

def main():
    libreria = Libreria()

    while True:
        print("Menú:")
        print("1. Registrar libro")
        print("2. Listar todos los libros")
        print("3. Registrar venta")
        print("4. Imprimir reporte de ventas")
        print("5. Generar txt")
        print("6. Salir del programa")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            libreria.registrar_libro()
        elif opcion == "2":
            libreria.listar_libros()
        elif opcion == "3":
            libreria.registrar_venta()
        elif opcion == "4":
            libreria.imprimir_reporte_ventas()
        elif opcion == "5":
            libreria.generar_txt()
        elif opcion == "6":
            print("Adios")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "main":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    



