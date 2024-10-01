'''
Desafío 1: Sistema de Gestión de Productos
Objetivo: Desarrollar un sistema para manejar productos en un inventario.

Requisitos:

Crear una clase base Producto con atributos como nombre, precio, cantidad en stock, etc.
Definir al menos 2 clases derivadas para diferentes categorías de productos (por ejemplo, ProductoElectronico, ProductoAlimenticio) con atributos y métodos específicos.
Implementar operaciones CRUD para gestionar productos del inventario.
Manejar errores con bloques try-except para validar entradas y gestionar excepciones.
Persistir los datos en archivo JSON.

'''
'''
Crear una clase base Producto con atributos como ProductoId, Nombre, CategoriaId, Stock, Habilitado, Precio, Color, Medida, Material
'''
import mysql.connector
from mysql.connector import Error
from decouple import config


class Producto:
    def __init__(self, nombre, precio, stock , categoria, subcategoria, material, color): # Constructor de la clase.
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.__categoria = categoria
        self.__subcategoria = subcategoria
        self.__material = material
        self.__color = color

    @property # Decorador para definir un método getter.
    def nombre(self):
        return self.__nombre.capitalize()

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    @property
    def categoria(self):
        return self.__categoria.capitalize()

    @property
    def subcategoria(self):
        return self.__subcategoria.capitalize()

    @property
    def material(self):
        return self.__material.capitalize()

    @property
    def color(self):
        return self.__color.capitalize()

    @nombre.setter # Decorador para definir un método setter.
    def nombre(self, nuevo_nombre):
        self.__nombre = self.validar_nombre(nuevo_nombre)

    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = self.validar_precio(nuevo_precio)

    @stock.setter
    def stock(self, cantidad):
        self.__stock = self.validar_stock(cantidad)

    @categoria.setter
    def categoria(self, nueva_categoria):
        self.__categoria = self.validar_categoria(nueva_categoria)

    @subcategoria.setter
    def subcategoria(self, nueva_subcategoria):
        self.__subcategoria = self.validar_subcategoria(nueva_subcategoria)

    @material.setter
    def material(self, nuevo_material):
        self.__material = self.validar_material(nuevo_material)

    @color.setter
    def color(self, nuevo_color):
        self.__color = self.validar_color(nuevo_color)

    # Método de bloques try-except para validar entradas y gestionar excepciones verificando que el nombre no sea vacío y que no este repetido.
    def validar_nombre(self, nombre):
        try:
            nombre_valido = nombre.capitalize()
            if not nombre_valido:
                raise ValueError('El nombre no puede estar vacío.')
            return nombre_valido
        except ValueError:
            raise ValueError('El nombre no puede estar vacío.')  # Lanzar excepción


    # Método de bloques try-except para validar entradas y gestionar excepciones verificando que el precio sea mayor o igual a 0
    def validar_precio(self, precio):
        try:
            precio_valido = float(precio)
            if precio_valido < 0:
                raise ValueError('El precio no puede ser negativo.')
            return precio_valido
        except ValueError:
            raise ValueError('El precio no puede ser negativo.')

    # Método de bloques try-except para validar entradas y gestionar excepciones verificando que el stock sea mayor o igual a 0
    def validar_stock(self, cantidad):
        try:
            cantidad_valida = int(cantidad)
            if cantidad_valida < 0:
                raise ValueError('La cantidad no puede ser negativa.')
            return cantidad_valida
        except ValueError:
            raise ValueError('La cantidad no puede ser negativa.')

    # Método de bloques try-except para validar entradas y gestionar excepciones verificando que la categoría no sea vacía
    def validar_categoria(self, categoria):
        try:
            categoria_valida = categoria.capitalize()
            if not categoria_valida:
                raise ValueError('La categoría no puede estar vacía.')
            return categoria_valida
        except ValueError:
            raise ValueError('La categoría no puede estar vacía.')

    # Método de bloques try-except para validar entradas y gestionar excepciones verificando que la subcategoría sea Terminación o Borde
    def validar_subcategoria(self, tipo):
        try:
            tipo_valido = tipo.capitalize()
            if tipo_valido not in ['Terminación', 'Borde']:
                raise ValueError('El tipo de producto debe ser Terminación o Borde.')
            return tipo_valido
        except ValueError:
            raise ValueError('El tipo de producto debe ser Terminación o Borde.')

    # Método de bloques try-except para validar entradas y gestionar excepciones verificando que el material no sea vacío
    def validar_material(self, material):
        try:
            material_valido = material.capitalize()
            if not material_valido:
                raise ValueError('El material no puede estar vacío.')
            return material_valido
        except ValueError:
            raise ValueError('El material no puede estar vacío.')

    # Método de bloques try-except para validar entradas y gestionar excepciones verificando que el color no sea vacío
    def validar_color(self, color):
        try:
            color_valido = color.capitalize()
            if not color_valido:
                raise ValueError('El color no puede estar vacío.')
            return color_valido
        except ValueError:
            raise ValueError('El color no puede estar vacío.')

    # Método para convertir la instancia en un diccionario y devolverlo como para poder serializarla a JSON.
    def to_dict(self):
        return {
            'nombre': self.nombre,
            # 'id': self.id,
            'precio': self.precio,
            'stock': self.stock,
            'categoria': self.categoria,
            'subcategoria': self.subcategoria,
            'material': self.material,
            'color': self.color}
    # Métodos comunes para todas las instancias de Producto.

    def __str__(self):
        return f'Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}, Categoria: {self.categoria}, Subcategoría: {self.subcategoria}, Material: {self.material}, Color: {self.color}'

'''
Definir al menos 2 clases derivadas para diferentes categorías de productos (por ejemplo, ProductoElectronico, ProductoAlimenticio) con atributos y métodos específicos.
'''
class ProductoPiscina(Producto):
    def __init__(self, nombre, precio, stock, categoria, subcategoria, material, color, cantidad_unidad_venta):
        super().__init__(nombre, precio, stock, categoria, subcategoria, material, color)
        self.__cantidad_unidad_venta = cantidad_unidad_venta

    @property
    def cantidad_unidad_venta(self):
        return self.__cantidad_unidad_venta.capitalize()

    @cantidad_unidad_venta.setter
    def cantidad_unidad_venta(self, cantidad):
        self.__cantidad_unidad_venta = self.validar_cantidad(cantidad)


    def validar_cantidad(self, cantidad):
        try:
            cantidad_valida = cantidad.capitalize()
            if not cantidad_valida:
                raise ValueError('La cantidad de unidades del producto no puede estar vacía.')
            return cantidad_valida
        except ValueError:
            raise ValueError('La cantidad de unidades del producto no puede estar vacía.')

    def to_dict(self):
        data = super().to_dict()
        data['cantidad_unidad_venta'] = self.cantidad_unidad_venta
        return data

    def __str__(self):
        return f'Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}, Categoria: {self.categoria}, Tipo de producto: {self.subcategoria}, Material: {self.material}, Color: {self.color}, Cantidad de unidad x venta: {self.cantidad_unidad_venta}'

class ProductoTerminacion(ProductoPiscina):
    def __init__(self, nombre, precio, stock, categoria, subcategoria, material, color, cantidad_unidad_venta, tipo_terminacion):
        super().__init__(nombre, precio, stock, categoria, subcategoria, material, color, cantidad_unidad_venta)
        self.__tipo_terminacion = tipo_terminacion

    @property
    def tipo_terminacion(self):
        return self.__tipo_terminacion.capitalize()

    @tipo_terminacion.setter
    def tipo_terminacion(self, nuevo_tipo):
        self.__tipo_terminacion = self.validar_tipo(nuevo_tipo)

    def validar_tipo(self, tipo):
        try:
            tipo_valido = tipo.capitalize()
            if tipo_valido not in ['Pintura', 'Revestimiento', 'Impermeabilizante']:
                raise ValueError('El tipo de producto debe ser Pintura, Revestimiento o Impermeabilizante.')
            return tipo_valido
        except ValueError:
            raise ValueError('El tipo de producto debe ser Pintura, Revestimiento o Impermeabilizante.')

    # Métodos específicos para productos de terminación.
    def to_dict(self):
        data = super().to_dict()
        data['tipo_terminacion'] = self.tipo_terminacion
        return data

    def __str__(self):
        return f'Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}, Categoria: {self.categoria}, Tipo de producto: {self.subcategoria}, Material: {self.material}, Color: {self.color}, Cantidad de unidad x venta: {self.cantidad_unidad_venta}, Tipo de terminación: {self.tipo_terminacion}'

class ProductoBorde(ProductoPiscina):
    def __init__(self, nombre, precio, stock, categoria, subcategoria, material, color, cantidad_unidad_venta, tipo_borde, largo, ancho, espesor):
        super().__init__(nombre, precio, stock, categoria, subcategoria, material, color, cantidad_unidad_venta)
        self.__tipo_borde = tipo_borde
        self.__largo = largo
        self.__ancho = ancho
        self.__espesor = espesor

    @property
    def tipo_borde(self):
        return self.__tipo_borde.capitalize()

    @property
    def largo(self):
        return self.__largo

    @property
    def ancho(self):
        return self.__ancho

    @property
    def espesor(self):
        return self.__espesor

    @tipo_borde.setter
    def tipo_borde(self, nuevo_tipo):
        self.__tipo_borde = self.validar_tipo(nuevo_tipo)

    @largo.setter
    def largo(self, nuevo_largo):
        self.__largo = self.validar_medida(nuevo_largo)

    @ancho.setter
    def ancho(self, nuevo_ancho):
        self.__ancho = self.validar_medida(nuevo_ancho)

    @espesor.setter
    def espesor(self, nuevo_espesor):
        self.__espesor = self.validar_medida(nuevo_espesor)

    def validar_tipo(self, tipo):
        try:
            tipo_valido = tipo.capitalize()
            if tipo_valido not in ['Borde ballena', 'Borde recto', 'Borde l', 'Esquina ballena', 'Esquina recta', 'Esquina l']:
                raise ValueError('El tipo de borde debe ser Borde ballena, Borde recto, Borde l, Esquina ballena, Esquina recta o Esquina l.')
            return tipo_valido
        except ValueError:
            raise ValueError('El tipo de borde debe ser Borde ballena, Borde recto, Borde l, Esquina ballena, Esquina recta o Esquina l.')

    def validar_medida(self, medida):
        try:
            medida_valida = float(medida)
            if medida_valida < 0:
                raise ValueError('La medida no puede ser negativa.')
            return medida_valida
        except ValueError:
            raise ValueError('La medida no puede ser negativa.')

    # Métodos específicos para productos de borde.
    def to_dict(self):
        data = super().to_dict()
        data['tipo_borde'] = self.tipo_borde
        data['largo'] = self.largo
        data['ancho'] = self.ancho
        data['espesor'] = self.espesor
        return data

    def __str__(self):
        return f'Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}, Categoria: {self.categoria}, Subcategoría: {self.subcategoria}, Material: {self.material}, Color: {self.color}, Cantidad de unidad x venta: {self.cantidad_unidad_venta}, Tipo de borde: {self.tipo_borde}, Largo: {self.largo} cm, Ancho: {self.ancho} cm, Espesor: {self.espesor} cm'

class ProductoRevestimiento(Producto):
    def __init__(self, nombre, precio, stock, categoria, subcategoria, material, color, cantidad_unidad_venta, tipo_superficie, ubicacion,
                 largo, ancho, espesor):
        super().__init__(nombre, precio, stock, categoria, subcategoria, material, color)
        self.__cantidad_unidad_venta = self.validar_cantidad(cantidad_unidad_venta)
        self.__tipo_superficie = tipo_superficie  # Piso, pared o ambas
        self.__ubicacion = ubicacion # Interior, exterior o ambas
        self.__largo = largo
        self.__ancho = ancho
        self.__espesor = espesor


    @property
    def cantidad_unidad_venta(self):
        return self.__cantidad_unidad_venta

    @property
    def tipo_superficie(self):
        return self.__tipo_superficie.capitalize()

    @property
    def ubicacion(self):
        return self.__ubicacion.capitalize()

    @property
    def largo(self):
        return self.__largo

    @property
    def ancho(self):
        return self.__ancho

    @property
    def espesor(self):
        return self.__espesor

    @cantidad_unidad_venta.setter
    def cantidad_unidad_venta(self, cantidad):
        self.__cantidad_unidad_venta = self.validar_cantidad(cantidad)

    @tipo_superficie.setter
    def tipo_superficie(self, nuevo_tipo):
        self.__tipo_superficie = self.validar_tipo(nuevo_tipo)

    @ubicacion.setter
    def ubicacion(self, nueva_ubicacion):
        self.__ubicacion = self.validar_ubicacion(nueva_ubicacion)


    @largo.setter
    def largo(self, nuevo_largo):
        self.__largo = self.validar_medida(nuevo_largo)

    @ancho.setter
    def ancho(self, nuevo_ancho):
        self.__ancho = self.validar_medida(nuevo_ancho)

    @espesor.setter
    def espesor(self, nuevo_espesor):
        self.__espesor = self.validar_medida(nuevo_espesor)

    def validar_cantidad(self, cantidad):
        try:
            cantidad_valida = int(cantidad)  # Convertimos la cantidad a un entero
            if cantidad_valida <= 0:
                raise ValueError('La cantidad de unidades del producto debe ser mayor que cero.')
            return cantidad_valida
        except ValueError:
            print('La cantidad de unidades del producto debe ser un número entero mayor que cero.')
            return None  # Devolvemos None en caso de error para manejarlo más adelante

    def validar_tipo(self, tipo):
        try:
            tipo_valido = tipo.capitalize()
            if tipo_valido not in ['Piso', 'Pared', 'Ambas']:
                raise ValueError('El tipo de superficie debe ser Piso, Pared o Ambas.')
            return tipo_valido
        except ValueError:
            print('El tipo de superficie debe ser Piso, Pared o Ambas.')

    def validar_ubicacion(self, ubicacion):
        try:
            ubicacion_valida = ubicacion.capitalize()
            if ubicacion_valida not in ['Interior', 'Exterior', 'Ambas']:
                raise ValueError('La ubicación debe ser Interior, Exterior o Ambas.')
            return ubicacion_valida
        except ValueError:
            print('La ubicación debe ser Interior, Exterior o Ambas.')

    def validar_medida(self, medida):
        try:
            medida_valida = float(medida)
            if medida_valida < 0:
                raise ValueError('La medida no puede ser negativa.')
            return medida_valida
        except ValueError:
            raise ValueError('La medida debe ser un número válido.')

    # Métodos específicos para ProductoRevestimiento.
    def to_dict(self):
        data = super().to_dict()
        data['cantidad_unidad_venta'] = self.cantidad_unidad_venta
        data['tipo_superficie'] = self.tipo_superficie
        data['ubicacion'] = self.ubicacion
        data['largo'] = self.largo
        data['ancho'] = self.ancho
        data['espesor'] = self.espesor
        return data

    def __str__(self):
        return f'Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}, Categoria: {self.categoria}, Subcategoría: {self.subcategoria}, Material: {self.material}, Color: {self.color},  Cantidad de unidad x venta: {self.cantidad_unidad_venta}, Tipo de superficie: {self.tipo_superficie}, Ubicación: {self.ubicacion}, Largo: {self.largo} cm, Ancho: {self.ancho} cm, Espesor: {self.espesor} cm'

class ProductoAdicionales(Producto):
    def __init__(self, nombre, precio, stock, categoria, subcategoria, material, color, uso_funcion):
        super().__init__(nombre, precio, stock , categoria, subcategoria, material, color)
        self.__uso_funcion = uso_funcion

    @property
    def uso_funcion(self):
        return self.__uso_funcion.capitalize()

    @uso_funcion.setter
    def uso_funcion(self, nuevo_uso):
        self.__uso_funcion = self.validar_uso(nuevo_uso)

    def validar_uso(self, uso):
        try:
            uso_valido = uso.capitalize()
            if not uso_valido:
                raise ValueError('El uso o función no puede estar vacío.')
            return uso_valido
        except ValueError:
            print('El uso o función no puede estar vacío.')

    # Métodos específicos para ProductoAdicionales.

    def to_dict(self):
        data = super().to_dict()
        data['uso_funcion'] = self.uso_funcion
        return data

    def __str__(self):
        return f'Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}, Categoria: {self.categoria}, Uso o función: {self.uso_funcion}, Material: {self.material}, Color: {self.color}'


'''
Implementar operaciones CRUD para gestionar productos del inventario.
'''
class Inventario:
    def __init__(self):
        self.host=config('DB_HOST')
        self.user=config('DB_USER')
        self.password=config('DB_PASSWORD')
        self.database=config('DB_NAME')
        self.port=config('DB_PORT')
        print(f'Host: {self.host}, User: {self.user}, Password: {self.password}, Database: {self.database}, Port: {self.port}')

    # Método para establecer la conexión a la base de datos
    def conectar(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            if connection.is_connected():
                print('Conexión exitosa')
                return connection
        except mysql.connector.Error as e:
            print(f'Error al conectar a la base de datos T.T: {e}')
            return None
        except Exception as e:
            print(f'Error inesperado al conectar a la base de datos ¬¬: {e}')
            return None
    

    def cerrar_conexion(self):
        self.cursor.close()
        self.conn.close()
    
    
    # Método para "crear" un producto y agregarlo al inventario.
    def crear_producto(self, producto):
        try:
            connection = self.conectar()
            print(f'llegue a la coneccion')
            if connection:
                with connection.cursor() as cursor:
                    # Verificar si el nombre del producto ya existe
                    cursor.execute('SELECT id FROM producto WHERE nombre = %s', (producto.nombre,))
                    if cursor.fetchone():
                        print(f'El producto con nombre {producto.nombre} ya existe en la base de datos.')
                        return
                    # Insertar datos básicos en la tabla Producto
                    query = '''
                    INSERT INTO Producto (nombre, precio, stock, categoria, subcategoria, material, color)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)'''
                    cursor.execute(query, (producto.nombre, producto.precio, producto.stock, producto.categoria, producto.subcategoria, producto.material, producto.color))
                    producto.id = cursor.lastrowid
                    print(f'Producto {producto.nombre} insertado en la tabla Producto con ID {producto.id}.')

                    # Insertar datos en la tabla ProductoPiscina si es un producto de piscina
                    if isinstance(producto, ProductoPiscina):
                        query = '''
                        INSERT INTO ProductoPiscina (id, cantidad_unidad_venta)
                        VALUES (%s, %s)'''
                        cursor.execute(query, (producto.id, producto.cantidad_unidad_venta))
                        print(f'Producto {producto.nombre} insertado en la tabla ProductoPiscina.')

                    # Insertar datos adicionales en las tablas específicas de cada subcategoría de producto de piscina
                    if isinstance(producto, ProductoTerminacion):
                        query ='''
                        INSERT INTO ProductoTerminacion (id,  tipo_terminacion)
                        VALUES (%s, %s)'''
                        cursor.execute(query, (producto.id, producto.tipo_terminacion))
                    elif isinstance(producto, ProductoBorde):
                        query ='''
                        INSERT INTO ProductoBorde (id, tipo_borde, largo, ancho, espesor)
                        VALUES (%s, %s, %s, %s, %s)'''
                        cursor.execute(query, (producto.id, producto.tipo_borde, producto.largo, producto.ancho, producto.espesor))
                    elif isinstance(producto, ProductoRevestimiento):
                        query ='''
                        INSERT INTO ProductoRevestimiento ( id, cantidad_unidad_venta, tipo_superficie, ubicacion, largo, ancho, espesor)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)'''
                        cursor.execute(query, (producto.id, producto.cantidad_unidad_venta, producto.tipo_superficie,producto.ubicacion, producto.largo, producto.ancho, producto.espesor))
                    elif isinstance(producto, ProductoAdicionales):
                        query ='''
                        INSERT INTO ProductoAdicionales (id, uso_funcion)
                        VALUES (%s, %s)'''
                        cursor.execute(query, (producto.id, producto.uso_funcion))

                    print(f'Producto {producto.nombre} insertado en la tabla específica correspondiente.')

                    connection.commit()
                    print(f'Producto {producto.nombre} agregado correctamente.')
        except Exception as e:
            print(f'Error al agregar el producto: {e}')



    # Método para buscar o leer un producto por su nombre.
    def buscar_producto_por_nombre(self, nombre):
        try:
            connection = self.conectar()
            if connection:
                with connection.cursor(dictionary=True) as cursor:
                    # Consulta para obtener los datos del producto por nombre
                    cursor.execute('SELECT * FROM Producto WHERE nombre = %s', (nombre,))
                    producto_data = cursor.fetchone()

                    if producto_data:
                        producto = None
                        # Determinar el tipo de producto basado en la subcategoría o categoría
                        if producto_data['subcategoria'] == 'Terminacion':
                            cursor.execute('SELECT * FROM ProductoPiscina WHERE id = %s', (producto_data['id'],))
                            piscina_data = cursor.fetchone()
                            producto_data.update(piscina_data)
                            cursor.execute('SELECT * FROM ProductoTerminacion WHERE id = %s', (producto_data['id'],))
                            terminacion_data = cursor.fetchone()
                            producto_data.update(terminacion_data)
                            producto = ProductoTerminacion(**{k: v for k, v in producto_data.items() if k != 'id'})
                        elif producto_data['subcategoria'] == 'Borde':
                            cursor.execute('SELECT * FROM ProductoPiscina WHERE id = %s', (producto_data['id'],))
                            piscina_data = cursor.fetchone()
                            producto_data.update(piscina_data)
                            cursor.execute('SELECT * FROM ProductoBorde WHERE id = %s', (producto_data['id'],))
                            borde_data = cursor.fetchone()
                            producto_data.update(borde_data)
                            producto = ProductoBorde(**{k: v for k, v in producto_data.items() if k != 'id'})
                        elif producto_data['categoria'] == 'Revestimiento':
                            cursor.execute('SELECT * FROM ProductoRevestimiento WHERE id = %s', (producto_data['id'],))
                            revestimiento_data = cursor.fetchone()
                            producto_data.update(revestimiento_data)
                            producto = ProductoRevestimiento(**{k: v for k, v in producto_data.items() if k != 'id'})
                        elif producto_data['categoria'] == 'Adicionales':
                            cursor.execute('SELECT * FROM ProductoAdicionales WHERE id = %s', (producto_data['id'],))
                            adicionales_data = cursor.fetchone()
                            producto_data.update(adicionales_data)
                            producto = ProductoAdicionales(**{k: v for k, v in producto_data.items() if k != 'id'})
                        else:
                            print(f'Tipo de producto desconocido para nombre: {nombre}')# Maneja el caso de producto desconocido
                             
                        print(f'Producto encontrado con {producto}')
                        
                    else:
                        print(f'Producto con nombre: {nombre} no encontrado.')# Maneja el caso de producto no encontrado
                          
        except Exception as error:
            print(f'Error al buscar el producto: {error}') # Maneja el error de otra forma
            


    # Método para buscar o leer un producto por su Id de producto.
    def buscar_producto(self, id):
        try:
            connection = self.conectar()
            if connection:
                with connection.cursor(dictionary=True) as cursor:
                    # Consulta para obtener los datos del producto
                    cursor.execute('SELECT * FROM Producto WHERE id = %s', (id,))
                    producto_data = cursor.fetchone()

                    if producto_data:
                        producto = None
                        # Determinar el tipo de producto basado en la subcategoría o categoría
                        if producto_data['subcategoria'] == 'Terminacion':
                            cursor.execute('SELECT * FROM ProductoPiscina WHERE id = %s', (id,))
                            piscina_data = cursor.fetchone()
                            producto_data.update(piscina_data)
                            cursor.execute('SELECT * FROM ProductoTerminacion WHERE id = %s', (id,))
                            terminacion_data = cursor.fetchone()
                            producto_data.update(terminacion_data)
                            producto = ProductoTerminacion(**{k: v for k, v in producto_data.items() if k != 'id'})
                        elif producto_data['subcategoria'] == 'Borde':
                            cursor.execute('SELECT * FROM ProductoPiscina WHERE id = %s', (id,))
                            piscina_data = cursor.fetchone()
                            producto_data.update(piscina_data)
                            cursor.execute('SELECT * FROM ProductoBorde WHERE id = %s', (id,))
                            borde_data = cursor.fetchone()
                            producto_data.update(borde_data)
                            producto = ProductoBorde(**{k: v for k, v in producto_data.items() if k != 'id'})
                        elif producto_data['categoria'] == 'Revestimiento':
                            cursor.execute('SELECT * FROM ProductoRevestimiento WHERE id = %s', (id,))
                            revestimiento_data = cursor.fetchone()
                            producto_data.update(revestimiento_data)
                            producto = ProductoRevestimiento(**{k: v for k, v in producto_data.items() if k != 'id'})
                        elif producto_data['categoria'] == 'Adicionales':
                            cursor.execute('SELECT * FROM ProductoAdicionales WHERE id = %s', (id,))
                            adicionales_data = cursor.fetchone()
                            producto_data.update(adicionales_data)
                            producto = ProductoAdicionales(**{k: v for k, v in producto_data.items() if k != 'id'})
                        else:
                            print(f'Tipo de producto desconocido para ID: {id}') 
                            return None # Maneja el caso de producto desconocido
                        print(f'Producto encontrado con Id: {id} - {producto}')
                        return producto
                    else:
                        print(f'Producto con Id: {id} no encontrado.')
                        return None # Maneja el caso de producto no encontrado
        except Exception as error:
            print(f'Error al buscar el producto: {error}')
            return None # Maneja el error de otra forma
             


    # Método para actualizar un producto en el inventario.
    def actualizar_atributo(self, id, atributo, nuevo_valor):
        try:
            connection = self.conectar()
            if connection:
                with connection.cursor() as cursor:
                    # Determinar la tabla a actualizar basado en el atributo
                    if atributo in ['cantidad_unidad_venta', 'tipo_terminacion']:
                        if atributo == 'tipo_terminacion':
                            tabla = 'ProductoTerminacion'
                        else:
                            tabla = 'ProductoPiscina'
                    else:
                        tabla = 'Producto'
                    
                    # Crear la consulta SQL para actualizar el atributo
                    query = f'UPDATE {tabla} SET {atributo} = %s WHERE id = %s'
                    cursor.execute(query, (nuevo_valor, id))
                    connection.commit()
                    print(f"Atributo '{atributo}' actualizado correctamente para el producto con ID {id}.")
        except Exception as error:
            print(f'Error al actualizar el atributo: {error}')


    # Método para eliminar un producto del inventario.
    def eliminar_producto(self, id):
        try:
            connection = self.conectar()
            if connection:
                with connection.cursor() as cursor:
                    # Eliminar el producto de la tabla Producto
                    query = 'DELETE FROM Producto WHERE id = %s'
                    cursor.execute(query, (id,))
                    
                    # También eliminar de las tablas específicas si es necesario
                    cursor.execute('DELETE FROM ProductoPiscina WHERE id = %s', (id,))
                    cursor.execute('DELETE FROM ProductoTerminacion WHERE id = %s', (id,))
                    cursor.execute('DELETE FROM ProductoBorde WHERE id = %s', (id,))
                    cursor.execute('DELETE FROM ProductoRevestimiento WHERE id = %s', (id,))
                    cursor.execute('DELETE FROM ProductoAdicionales WHERE id = %s', (id,))
                    
                    connection.commit()
                    print(f'Producto con Id: {id} eliminado correctamente.')
            else:
                print(f'No se pudo conectar a la base de datos.')
        except Exception as error:
            print(f'Error al eliminar el producto: {error}')


    # Método para listar todos los productos del inventario.
    def listar_productos(self):
        try:
            connection = self.conectar()
            if connection:
                with connection.cursor() as cursor:
                    query = 'SELECT * FROM Producto'
                    cursor.execute(query)
                    productos = cursor.fetchall()
                    
                    for producto in productos:
                        print(producto)
            else:
                print(f'No se pudo conectar a la base de datos.')
        except Exception as error:
            print(f'Error al listar los productos: {error}')





