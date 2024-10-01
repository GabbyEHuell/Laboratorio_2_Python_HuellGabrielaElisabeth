import os
import platform
import mysql.connector

from laboratorio_Poo import Inventario, ProductoTerminacion, ProductoBorde, ProductoRevestimiento, ProductoAdicionales

atributos_modificables = {
    'ProductoTerminacion': ['nombre', 'precio', 'stock', 'material', 'color', 'cantidad_unidad_venta', 'tipo_terminacion'],
    'ProductoBorde': ['nombre', 'precio', 'stock', 'material', 'color', 'cantidad_unidad_venta', 'tipo_borde', 'largo', 'ancho', 'espesor'],
    'ProductoRevestimiento': ['nombre', 'precio', 'stock', 'material', 'color', 'cantidad_unidad_venta', 'tipo_superficie', 'ubicacion', 'largo', 'ancho', 'espesor'],
    'ProductoAdicionales': ['nombre', 'precio', 'stock', 'material', 'color', 'uso_funcion']
}

def limpiar_pantalla():
    ''' Limpiar la pantalla según el sistema operativo'''
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear') # Para Linux/Unix/MacOs

def mostrar_menu():
    print('========== Menú de Gestión de de Productos ==========')
    print('1. Agregar Productos')
    print('2. Buscar Productos por Nombre de producto')
    print('3. Buscar Productos por id de producto')
    print('4. Actualizar Productos')
    print('5. Eliminarar Productos por id de producto')
    print('6. Mostrar Todos los Productos')
    print('7. Salir')
    print('======================================================')

def obtener_categoria():
    while True:
        try:
            opcion = int(input('Seleccione una categoría:\n1. Piscina\n2. Revestimiento\n3. Adicionales\n'))
            if opcion in [1, 2, 3]:
                if opcion == 1:
                    return 'Piscina'
                elif opcion == 2:
                    return 'Revestimiento'
                elif opcion == 3:
                    return 'Adicionales'
            else:
                print('Opción no válida. Intente nuevamente.')
        except ValueError:
            print('Debe ingresar un número válido (1, 2 o 3).')

def obtener_subcategoria(categoria):
    while True:
        try:
            if categoria == 'Piscina':
                opcion = int(input('Seleccione una subcategoría:\n1. Terminación\n2. Borde\n'))
                if opcion in [1, 2]:
                    if opcion == 1:
                        return 'Terminacion'
                    elif opcion == 2:
                        return 'Borde'
                    else:
                        print('Opción no válida. Intente nuevamente.')
            elif categoria == 'Revestimiento':
                opcion = int(input('Seleccione una subcategoría:\n1. Piso\n2. Pared\n3. Piso y Pared\n'))
                if opcion in [1, 2, 3]:
                    if opcion == 1:
                        return 'Piso'
                    elif opcion == 2:
                        return 'Pared'
                    elif opcion == 3:
                        return 'Piso y Pared'
                    else:
                        print('Opción no válida. Intente nuevamente.')
            elif categoria == 'Adicionales':
                opcion = int(input('Seleccione una subcategoría:\n1. Tuberías de PVC\n2. Skimmers\n3. Desagües\n4. Bomba de agua\n5. Filtro\n6. Clorador\n7. Iluminación\n8. Cableado eléctrico\n9. Escaleras\n'))
                if opcion in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    if opcion == 1:
                        return 'Tuberías de PVC'
                    elif opcion == 2:
                        return 'Skimmers'
                    elif opcion == 3:
                        return 'Desagües'
                    elif opcion == 4:
                        return 'Bomba de agua'
                    elif opcion == 5:
                        return 'Filtro'
                    elif opcion == 6:
                        return 'Clorador'
                    elif opcion == 7:
                        return 'Iluminación'
                    elif opcion == 8:
                        return 'Cableado eléctrico'
                    elif opcion == 9:
                        return 'Escaleras'
            else:
                print('Categoría no válida. Intente nuevamente.')
        except ValueError:
            print('Debe ingresar un número válido.')

def obtener_tipo_terminacion():
    while True:
        try:
            opcion = int(input('Seleccione el tipo de terminación:\n1. Pintura\n2. Revestimiento\n3. Impermeabilizante\n'))
            if opcion in [1, 2, 3]:
                if opcion == 1:
                    return 'Pintura'
                elif opcion == 2:
                    return 'Revestimiento'
                elif opcion == 3:
                    return 'Impermeabilizante'
            else:
                print('Opción no válida. Intente nuevamente.')
        except ValueError:
            print('Debe ingresar un número válido (1, 2 o 3).')

def obtener_tipo_borde():
    while True:
        try:
            opcion = int(input('Seleccione el tipo de borde:\n1. Borde ballena\n2. Borde recto\n3. Borde L\n4. Esquina ballena\n5. Esquina recta\n6. Esquina L\n'))
            if opcion in [1, 2, 3, 4, 5, 6]:
                if opcion == 1:
                    return 'Borde ballena'
                elif opcion == 2:
                    return 'Borde recto'
                elif opcion == 3:
                    return 'Borde L'
                elif opcion == 4:
                    return 'Esquina ballena'
                elif opcion == 5:
                    return 'Esquina recta'
                elif opcion == 6:
                    return 'Esquina L'
            else:
                print('Opción no válida. Intente nuevamente.')
        except ValueError:
            print('Debe ingresar un número válido (1 al 6).')

def obtener_tipo_superficie():
    while True:
        try:
            opcion = int(input('Seleccione el tipo de superficie:\n1. Piso\n2. Pared\n3. Piso y Pared\n'))
            if opcion in [1, 2, 3]:
                if opcion == 1:
                    return 'Piso'
                elif opcion == 2:
                    return 'Pared'
                elif opcion == 3:
                    return 'Piso y Pared'
            else:
                print('Opción no válida. Intente nuevamente.')
        except ValueError:
            print('Debe ingresar un número válido (1, 2 o 3).')

def obtener_ubicacion():
    while True:
        try:
            opcion = int(input('Seleccione la ubicación:\n1. Interior\n2. Exterior\n3. Interior y Exterior\n'))
            if opcion in [1, 2, 3]:
                if opcion == 1:
                    return 'Interior'
                elif opcion == 2:
                    return 'Exterior'
                elif opcion == 3:
                    return 'Interior y Exterior'
            else:
                print('Opción no válida. Intente nuevamente.')
        except ValueError:
            print('Debe ingresar un número válido (1, 2 o 3).')

def agregar_producto(gestion):
    try:
        nombre = input('Ingrese el nombre del producto: ')
        # id_producto = input('Ingrese el ID del producto: ')# Cambio de nombre de la variable para evitar conflicto con 'id'
        precio = float(input('Ingrese el precio del producto: '))
        stock = int(input('Ingrese la cantidad en stock: '))
        categoria = obtener_categoria()
        subcategoria = obtener_subcategoria(categoria)
        material = input('Ingrese el material del producto: ')
        color = input('Ingrese el color del producto: ')

        if categoria == 'Piscina':
            cantidad_unidad_venta = input('A- Ingrese la cantidad y unidad de venta del producto: ')
            if subcategoria.lower().strip() == 'borde':
                tipo_borde = obtener_tipo_borde()
                largo = float(input('Ingrese el largo del producto en cm: '))
                ancho = float(input('Ingrese el ancho del producto en cm: '))
                espesor = float(input('Ingrese el espesor del producto en cm: '))
                producto = ProductoBorde(nombre, precio, stock, categoria, subcategoria, material, color, cantidad_unidad_venta, tipo_borde, largo, ancho, espesor)
                print('Presiona cualquier tecla para continuar...')
                input()
                print('¡Continuaste!')
                
                gestion.crear_producto(producto)
                input('Presione Enter para continuar...')
            else:
                if subcategoria.lower().strip() == 'terminacion':
                    tipo_terminacion = obtener_tipo_terminacion()
                    producto = ProductoTerminacion(nombre, precio, stock, categoria, subcategoria, material, color, cantidad_unidad_venta, tipo_terminacion)
                    gestion.crear_producto(producto)
                    input('Presione Enter para continuar...')
        
        elif categoria == 'Revestimiento':
            cantidad_unidad_venta = int(input('B- Ingrese la cantidad y unidad de venta del producto: '))
            tipo_superficie = obtener_tipo_superficie()
            ubicacion = obtener_ubicacion()
            largo = float(input('Ingrese el largo del producto en Cm: '))
            ancho = float(input('Ingrese el ancho del productoen Cm: '))
            espesor = float(input('Ingrese el espesor del producto en Cm: '))
            producto = ProductoRevestimiento(nombre, precio, stock, categoria, subcategoria, material, color, cantidad_unidad_venta, tipo_superficie, ubicacion, largo, ancho, espesor)
            gestion.crear_producto(producto)
            input('Presione Enter para continuar...')
        
        elif categoria == 'Adicionales':
            uso_funcion = input('C- Ingrese el uso o función del producto: ')
            producto = ProductoAdicionales(nombre, precio, stock, categoria, subcategoria, material, color, uso_funcion )
            gestion.crear_producto(producto)
            input('Presione Enter para continuar...')
    except ValueError as e:
        print(f'Error:', e)
    except Exception as e:
        print(f'Por favor, intente nuevamente')

def buscar_producto_por_nombre(gestion):
    ''' Buscar un producto en el inventario por su nombre'''
    nombre = input('Ingrese el nombre del producto a buscar: ')
    producto = gestion.buscar_producto_por_nombre(nombre)
    input('Presione Enter para continuar...')

def buscar_producto_por_id(gestion):
    ''' Buscar un if de producto en el inventario'''
    id = (input('Ingrese el codigo id del producto a buscar: '))
    gestion.buscar_producto(id)
    input('Presione Enter para continuar...')

def mostrar_opciones_modificacion(subclase):
    ''' Muestra las opciones de atributos disponibles para modificar '''
    atributos = atributos_modificables.get(subclase, []) 
    print('Opciones de atributos modificables:')
    for i, atributo in enumerate(atributos, start=1):
        print(f'{i}. {atributo}')

def obtener_atributo_seleccionado(subclase):
    ''' Obtiene el atributo seleccionado por el usuario '''
    opcion = input('Seleccione el número de atributo a modificar: ')

    atributos_disponibles = atributos_modificables.get(subclase, {})
    if opcion.isdigit() and 1 <= int(opcion) <= len(atributos_disponibles):
        atributo_seleccionado = atributos_disponibles[int(opcion) - 1]
        if atributo_seleccionado == 'tipo_terminacion':
             nuevo_valor = obtener_tipo_terminacion()
             return atributo_seleccionado, nuevo_valor
        return atributo_seleccionado, None
    else:
        print('Opción no válida. Seleccione un número de atributo válido.')
        return None, None

def actualizar_producto(gestion):
    ''' Actualizar atributos de un producto'''
    id_producto = input('Ingrese el id del producto a actualizar: ')
    producto = gestion.buscar_producto(id_producto)
    if producto:
        subclase = producto.__class__.__name__  # Obtén el nombre de la subclase
        mostrar_opciones_modificacion(subclase)
        atributo_seleccionado, nuevo_valor = obtener_atributo_seleccionado(subclase)
        print('atributo seleccionado es:', atributo_seleccionado)

        if atributo_seleccionado:
            if nuevo_valor is None:
                nuevo_valor = input(f"Ingrese el nuevo valor para '{atributo_seleccionado}':")
            gestion.actualizar_atributo(id_producto, atributo_seleccionado, nuevo_valor)
            print('Producto actualizado correctamente')
            input('Presione Enter para continuar...')
        
        else:
            print('Opción no válida. Seleccione un número de atributo válido.')
            input('Presione Enter para continuar...') 
    else:
        print(f'El producto {id_producto} no se encuentra en el inventario')
        input('Presione Enter para continuar...')

def eliminar_producto(gestion):
    ''' Eliminar un producto por nombre'''
    id_producto = input('Ingrese el id del producto a eliminar: ')
    producto = gestion.buscar_producto(id_producto)
    if producto:
        gestion.eliminar_producto(id_producto)
        print(f'Producto {id_producto} eliminado correctamente')
        input('Presione Enter para continuar...')
    else:
        print(f'El producto {id_producto} no se encuentra en el inventario')
        input('Presione Enter para continuar...')

def listar_productos(gestion):
    ''' Listar todos los productos'''
    print('==============Listar todos los productos==============')
    try:
        connection = gestion.conectar()
        if connection:
            print("Conexión establecida")
            cursor = connection.cursor(dictionary=True)
            # Consultar todos los productos desde la vista VistaProductos
            query = 'SELECT * FROM VistaProductos'
            cursor.execute(query)
            productos = cursor.fetchall()
            print("Consulta ejecutada")

            for producto in productos:
                print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Stock: {producto['stock']}, Categoría: {producto['categoria']}, Subcategoría: {producto['subcategoria']}, Material: {producto['material']}, Color: {producto['color']}, Cantidad Unidad Venta: {producto['cantidad_unidad_venta']}, Tipo Superficie: {producto['tipo_superficie']}, Ubicación: {producto['ubicacion']}, Largo: {producto['largo']}, Ancho: {producto['ancho']}, Espesor: {producto['espesor']}")
        else:
            print('No se pudo conectar a la base de datos.')
    except mysql.connector.Error as e:
        print(f'Error al listar los productos: {e}')
    except Exception as error:
        print(f'Error inesperado: {error}')
    print('======================================================')
    input('Presione Enter para continuar...')


# Programa principal
if __name__ == "__main__":
    gestion_productos = Inventario()

    # Cargar los productos desde el archivo
    while True: 
        limpiar_pantalla()
        mostrar_menu()
        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            agregar_producto(gestion_productos)

        elif opcion == '2':
            buscar_producto_por_nombre(gestion_productos)

        elif opcion == '3':
            buscar_producto_por_id(gestion_productos)

        elif opcion == '4':
            actualizar_producto(gestion_productos)

        elif opcion == '5':
            eliminar_producto(gestion_productos)

        elif opcion == '6':
            listar_productos(gestion_productos)

        elif opcion == '7':
            print('Saliendo del programa...')
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción válida (1-8)')