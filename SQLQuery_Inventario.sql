CREATE DATABASE InventarioProductos;
    USE InventarioProductos;

CREATE TABLE Producto (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    subcategoria VARCHAR(50),
    material VARCHAR(50),
    color VARCHAR(30)
);

CREATE TABLE ProductoPiscina (
    id INT PRIMARY KEY,
    cantidad_unidad_venta VARCHAR(100) NOT NULL,
    FOREIGN KEY (id) REFERENCES Producto(id)
);

CREATE TABLE ProductoTerminacion (
    id INT PRIMARY KEY,
    tipo_terminacion VARCHAR(50) NOT NULL,
    FOREIGN KEY (id) REFERENCES ProductoPiscina(id)
);

CREATE TABLE ProductoBorde (
    id INT PRIMARY KEY,
    tipo_borde VARCHAR(50) NOT NULL,
    largo DECIMAL(10, 2) NOT NULL,
    ancho DECIMAL(10, 2) NOT NULL,
    espesor DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id) REFERENCES ProductoPiscina(id)
);

CREATE TABLE ProductoRevestimiento (
    id INT PRIMARY KEY,
    cantidad_unidad_venta INT NOT NULL,
    tipo_superficie VARCHAR(50) NOT NULL,
    ubicacion VARCHAR(50) NOT NULL,
    largo DECIMAL(10, 2) NOT NULL,
    ancho DECIMAL(10, 2) NOT NULL,
    espesor DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id) REFERENCES Producto(id)
);

CREATE TABLE ProductoAdicionales (
    id INT PRIMARY KEY,
    uso_funcion VARCHAR(100) NOT NULL,
    FOREIGN KEY (id) REFERENCES Producto(id)
);

SELECT * FROM Producto

--ver todas las tablas
SELECT TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_TYPE = 'BASE TABLE';

--consulta que combina las tablas Producto, ProductoPiscina, y ProductoRevestimiento
SELECT 
    p.id,
    p.nombre,
    p.precio,
    p.stock,
    p.categoria,
    p.subcategoria,
    p.material,
    p.color,
    pp.cantidad_unidad_venta,
    pr.tipo_superficie,
    pr.ubicacion,
    pr.largo,
    pr.ancho,
    pr.espesor
FROM 
    Producto p
LEFT JOIN 
    ProductoPiscina pp ON p.id = pp.id
LEFT JOIN 
    ProductoRevestimiento pr ON p.id = pr.id;

-- vista unificada, para crear una vista que maneje las diferencias en los tipos de datos en cantidad de unidades de venta.
CREATE VIEW VistaProductos AS
SELECT 
    p.id,
    p.nombre,
    p.precio,
    p.stock,
    p.categoria,
    p.subcategoria,
    p.material,
    p.color,
    COALESCE(pp.cantidad_unidad_venta, pr.cantidad_unidad_venta) AS cantidad_unidad_venta,
    pr.tipo_superficie,
    pr.ubicacion,
    pr.largo,
    pr.ancho,
    pr.espesor
FROM 
    Producto p
LEFT JOIN 
    ProductoPiscina pp ON p.id = pp.id
LEFT JOIN 
    ProductoRevestimiento pr ON p.id = pr.id;

--ver la nueva vista unificada que fue creda
SELECT * FROM VistaProductos;


-- modificacion para eliminar en cascada un producto 
ALTER TABLE ProductoPiscina
ADD CONSTRAINT fk_producto_piscina
FOREIGN KEY (id) REFERENCES Producto(id)
ON DELETE CASCADE;

ALTER TABLE ProductoTerminacion
ADD CONSTRAINT fk_producto_terminacion
FOREIGN KEY (id) REFERENCES ProductoPiscina(id)
ON DELETE CASCADE;

ALTER TABLE ProductoBorde
ADD CONSTRAINT fk_producto_borde
FOREIGN KEY (id) REFERENCES ProductoPiscina(id)
ON DELETE CASCADE;

ALTER TABLE ProductoRevestimiento
ADD CONSTRAINT fk_producto_revestimiento
FOREIGN KEY (id) REFERENCES Producto(id)
ON DELETE CASCADE;

ALTER TABLE ProductoAdicionales
ADD CONSTRAINT fk_producto_adicionales
FOREIGN KEY (id) REFERENCES Producto(id)
ON DELETE CASCADE;