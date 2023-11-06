# Sub consultas

select * from comercioit.paises;
select * from comercioit.paises_backup;

insert into comercioit.paises_seleccion (id) values (9);

select * from comercioit.paises_seleccion;

select * from comercioit.paises where id in (select id from comercioit.paises_seleccion);

update comercioit.paises set salario_minimo = salario_minimo/100 where salario_minimo > 900;

select * from comercioit.paises;

# Quiero solo los paises de la tabla paises cuyo salario minimo es mayor a la media de TODOS los paises

select * from comercioit.paises where salario_minimo > (select avg(salario_minimo) from comercioit.paises);

select avg(salario_minimo) from comercioit.paises;

# Condicional CASE

SELECT *, case when salario_minimo < 250 then "BAJO" 
		       when salario_minimo < 337 then "NORMAL"
               else  "MAYOR A LO NORMAL"
		  end as categoria from comercioit.paises order by categoria;