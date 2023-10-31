-- create database comercioit;

-- CREATE TABLE comercioit.productos (
--     idProducto INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     nombre VARCHAR(50) NOT NULL,
--     precio DOUBLE,
--     marca VARCHAR(30) NOT NULL,
--     categoria VARCHAR(30) NOT NULL,
--     stock INT NOT NULL,
--     disponible BOOLEAN DEFAULT FALSE
-- )

-- drop table comercioit.productos;

-- show databases;

describe comercioit.productos;

-- alter table comercioit.productos add column almacen varchar(30) null;

-- alter table comercioit.productos add column subcategoria  varchar(30) null after categoria;

-- alter table comercioit.productos change almacen inventario varchar(30) null;

-- alter table comercioit.productos drop inventario;

# Manera completa 

-- insert into comercioit.productos (
--      nombre,
--      precio,
--      marca,
--      categoria,
--      subcategoria,
--      stock,
--      disponible)
--      values (
--      "TV 85",
--      1000,
--      "Samsung",
--      "TV / Monitores",
--      "TV",
--      2000,
--      true
--      )

# Manera Simplificada
insert into comercioit.productos 
     values (
     2,
     "23 Pro",
     1200,
     "Samsung",
     "Celulares",
     "Smartphones",
     200,
     true
     );

# Modo SQL     
insert INTO comercioit.productos SET nombre = 'iPhone 5', precio = 499.99, marca = 'Apple', categoria = 'Smartphone', stock = 500, disponible = false;
