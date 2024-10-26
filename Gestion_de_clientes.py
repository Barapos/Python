# Definición de la clase Cliente, que representa a un cliente con nombre, email y teléfono.
class Cliente:
    # Constructor de la clase Cliente. Se inicializan los atributos, nombre, email y telefono.
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    # Método especial __str__ que define cómo se debe mostrar la información de un objeto Cliente
    def __str__(self):
        return f"Cliente: {self.nombre}\nEmail: {self.email}\nTeléfono: {self.telefono}"


# Definición de la clase SistemaClientes, que gestiona una colección de objetos Cliente.
class SistemaClientes:
    # Constructor de la clase SistemaClientes. Inicializa una lista vacía para almacenar clientes.
    def __init__(self):
        self.clientes = []

    # Método para agregar un nuevo cliente al sistema.
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nombre} agregado con éxito.")

    # Método para eliminar un cliente del sistema por su nombre.
    def eliminar_cliente(self, nombre):
        # Recorre la lista de clientes buscando el nombre indicado.
        for cliente in self.clientes:
            if cliente.nombre == nombre:
                # Si se encuentra el cliente, se elimina de la lista y se confirma la eliminación.
                self.clientes.remove(cliente)
                print(f"Cliente {nombre} eliminado con éxito.")
                return
        # Si no se encuentra el cliente, se informa al usuario.
        print(f"No se encontró el cliente con el nombre: {nombre}")

    # Método para buscar un cliente por su nombre y devolver el objeto Cliente correspondiente.
    def buscar_cliente(self, nombre):
        for cliente in self.clientes:
            if cliente.nombre == nombre:
                return cliente  # Devuelve el cliente si se encuentra.
        return None  # Devuelve None si no se encuentra el cliente.

    # Método para listar todos los clientes registrados en el sistema.
    def listar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")  # Mensaje si no hay clientes en el sistema.
        else:
            for cliente in self.clientes:
                print(cliente)  # Muestra cada cliente utilizando el método __str__ de la clase Cliente.


# Función principal que contiene el menú para interactuar con el usuario.
def main():
    sistema = SistemaClientes()  # Se crea una instancia del sistema de gestión de clientes.

    while True:
        # Menú de opciones para el usuario.
        print("\nSistema de Gestión de Clientes")
        print("1. Agregar Cliente")
        print("2. Eliminar Cliente")
        print("3. Buscar Cliente")
        print("4. Listar Clientes")
        print("5. Salir")

        option = input("Seleccione una opción: ")

        # Opción 1: Agregar un nuevo cliente al sistema.
        if option == '1':
            nombre = input("Ingrese el nombre del cliente: ")
            email = input("Ingrese el email del cliente: ")
            telefono = input("Ingrese el teléfono del cliente: ")
            cliente = Cliente(nombre, email, telefono)  # Se crea un nuevo objeto Cliente.
            sistema.agregar_cliente(cliente)

        # Opción 2: Eliminar un cliente del sistema.
        elif option == '2':
            nombre = input("Ingrese el nombre del cliente a eliminar: ")
            sistema.eliminar_cliente(nombre)

        # Opción 3: Buscar un cliente por su nombre.
        elif option == '3':
            nombre = input("Ingrese el nombre del cliente a buscar: ")
            cliente = sistema.buscar_cliente(nombre)
            if cliente:
                print(cliente)  # Si se encuentra, se muestra la información del cliente.
            else:
                print("Cliente no encontrado.")  # Mensaje si no se encuentra el cliente.

        # Opción 4: Listar todos los clientes registrados en el sistema.
        elif option == '4':
            sistema.listar_clientes()

        # Opción 5: Salir del sistema.
        elif option == '5':
            print("Saliendo del sistema...")
            break

        # Manejo de opción inválida.
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")


# Punto de entrada del programa. Si se ejecuta el script, se llama a la función main.
if __name__ == "__main__":
    main()
