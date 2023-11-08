# Relaciones entre tablas

select * from comercioit.paises;
select * from comercioit.paises_backup;

select * from comercioit.paises union all
select * from comercioit.paises_backup;

create table comercioit.marcas (
id int primary key not null auto_increment,
nombre varchar(50) not null
);

create table comercioit.articulos (
id int not null auto_increment,
nombre varchar(50) not null,
idmarca int not null,
primary key (id),
constraint fk_marcas
 foreign key (idmarca)
 references comercioit.marcas(id)
 on delete cascade
 on update cascade
);


insert into comercioit.marcas (nombre) values ("Samsung");
insert into comercioit.marcas (nombre) values ("Apple");
insert into comercioit.marcas (nombre) values ("LG");
insert into comercioit.marcas (nombre) values ("Phillips");
insert into comercioit.marcas (nombre) values ("TCL");
insert into comercioit.marcas (nombre) values ("Sony");

select * from comercioit.marcas;
select * from comercioit.articulos;

insert into comercioit.articulos (nombre, idmarca) values ("S21 ultra", 1);
insert into comercioit.articulos (nombre, idmarca) values ("S22 ultra", 1);
insert into comercioit.articulos (nombre, idmarca) values ("S23 ultra", 1);
insert into comercioit.articulos (nombre, idmarca) values ("Iphone 11 Max", 2);
insert into comercioit.articulos (nombre, idmarca) values ("Iphone 12 Max", 2);
insert into comercioit.articulos (nombre, idmarca) values ("Iphone 13 Max", 2);
insert into comercioit.articulos (nombre, idmarca) values ("PlayStation 3", 6);
insert into comercioit.articulos (nombre, idmarca) values ("PlayStation 4", 6);
insert into comercioit.articulos (nombre, idmarca) values ("PlayStation 5", 6);
insert into comercioit.articulos (nombre, idmarca) values ("PlayStation 6", 6);
drop table comercioit.articulos;

select * from comercioit.articulos;


SELECT 
    *
FROM
    comercioit.articulos AS art
JOIN     
    comercioit.marcas AS mar ON 
    art.idmarca = mar.id;

# Vistas
select * from comercioit.art_sony;

select id, nombre, marca from comercioit.art_marca where idmarca = 2;


# Ejemplos
select * from comercioit.articulos order by nombre;