select count(*) from comercioit.peliculas; 
select count(*) from comercioit.paises; 

select * from comercioit.peliculas;
select count(*) from comercioit.peliculas where title like "%The%"; 

select sum(duration) from comercioit.peliculas; 

select certificate, count(*) from comercioit.peliculas group by certificate; 

select max(duration) from comercioit.peliculas; 
select min(duration) from comercioit.peliculas; 

select avg(duration) from comercioit.peliculas; 

select certificate, count(*) from comercioit.peliculas group by certificate having count(*) >= 99; 