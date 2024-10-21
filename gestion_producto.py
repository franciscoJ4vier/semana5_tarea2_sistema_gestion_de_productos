
productos = []

def añadir_producto():
    # Lógica para añadir un producto
    nombre = input('Introduzca el nombre del producto: ')
    
    while True:
        try:
            precio = float(input('Introduzca el precio del producto: '))
            break
        except ValueError:
            print("Error: El precio debe ser un número.")

    while True:
        try:
            cantidad = int(input('Introduzca la cantidad del producto: '))
            break
        except ValueError:
            print("Error: La cantidad debe ser un número entero.")

    producto = {
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }
    productos.append(producto)
    print(f"Producto '{nombre}' añadido correctamente.")

def ver_productos():
    # Lógica para ver todos los productos
    if not productos:
        print("No hay productos registrados.")
        return
    
    print("Lista de productos")
    for producto in productos:
            precio = int(producto['precio']) if producto['precio'].is_integer() else producto['precio']
            print(f"Nombre: {producto['nombre']}, Precio: {precio}, Cantidad: {producto['cantidad']}")
        
def actualizar_producto():
    # Lógica para actualizar un producto
    nombre = input("Introduzca el nombre del producto a actualizar: ")
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            nuevo_nombre = input("Introduzca el nuevo nombre del producto (No poner nada para no cambiar el nombre): ")
            if nuevo_nombre:
                producto['nombre'] = nuevo_nombre
            
            nuevo_precio = input("Introduzca el nuevo precio del producto (No poner nada para no cambiar el precio): ")
            if nuevo_precio:
                try:
                    producto['precio'] = float(nuevo_precio)
                except ValueError:
                    print("Error: El precio debe ser un número.")
                    return
            
            nueva_cantidad = input("Introduzca la nueva cantidad del producto (No poner nada para no cambiar la cantidad): ")
            if nueva_cantidad:
                try:
                    producto['cantidad'] = int(nueva_cantidad)
                except ValueError:
                    print("Error: La cantidad debe ser un número entero.")
                    return
            
            print(f"Producto '{nombre}' actualizado correctamente.")
            return
    print(f"No se encontró el producto '{nombre}'.")

def eliminar_producto():
    # Lógica para eliminar un producto
    nombre = input("Introduzca el nombre del producto para eliminar: ")
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado correctamente.")
            return
        
    print(f"No se encontró el producto '{nombre}'.")
    

def guardar_datos():
    # Lógica para guardar los datos en un archivo
    with open('productos.txt','w') as file:
        for producto in productos:
            file.write(f"{producto['nombre']}|{producto['precio']}|{producto['cantidad']}\n")
        print("Datos guardados exitosamente")


def cargar_datos():
    try:
        with open('productos.txt','r') as file:
            for linea in file:
                try:
                    nombre, precio, cantidad = linea.strip().split('|')
                    producto = {
                        'nombre': nombre,
                        'precio': float(precio),
                        'cantidad': int(cantidad)
                    }
                    productos.append(producto)
                except ValueError:
                    print(f"Error en la linea: {linea.strip()}")
        print("Datos cargados exitosamente")
    except FileNotFoundError:
        print("No se encontró el archivo 'productos.txt'.")


def menu():
    cargar_datos()  # cargar la lista de productos.txt al iniciar el programa
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Selecciona una opción válida.")


menu()