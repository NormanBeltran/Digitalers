drop table comercioit.paises_backup; # Elimina datos + estructura

# Creación de una tabla desde un SELECT 

create table comercioit.paises_backup
select * from comercioit.paises where nombre like "%a%";

select * from comercioit.paises;
select * from comercioit.paises_backup;

# Desbloquear el modo seguro del UPDATE
set SQL_SAFE_UPDATES = 0;

# Update de mas de un campo con condición de filtro 

update comercioit.paises set capital = upper(capital), salario_minimo = (salario_minimo*100) where capital like "%A%";

update comercioit.paises_backup set id = id*100;

# Insert de datos anexados (el select va sin parentesis, ojo error 1241)

INSERT into comercioit.paises (id, nombre, habitantes, capital, salario_minimo, independencia)
select id, nombre, habitantes, capital, salario_minimo, independencia from comercioit.paises_backup where habitantes =  214;


INSERT into comercioit.paises (id, nombre, habitantes, capital, salario_minimo, independencia)
select id*10, nombre, habitantes, capital, salario_minimo, independencia from comercioit.paises where habitantes =  12;


# Eliminación de registros

DELETE from comercioit.paises where id in (20, 300); # Elimina registros (eventualmente con condiciones)

TRUNCATE table comercioit.paises_backup; # Elimina registros pero NO la estructura

create table comercioit.paises_backup
select * from comercioit.paises;

INSERT into comercioit.paises_backup (nombre, habitantes, capital, salario_minimo, independencia)  values ("USA", 220, "Washinton", 1000, "1789-01-01" );

select * from comercioit.paises_backup;

delete from comercioit.paises_backup;
truncate table comercioit.paises_backup;


