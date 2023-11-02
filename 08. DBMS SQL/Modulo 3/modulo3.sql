# Funciones de Texto 

-- select * from comercioit.paises;

-- select concat(nombre, " / " ,capital) as pais_capital from comercioit.paises;

-- select concat_ws(";" , nombre, capital, ID) as pais_capital from comercioit.paises;

-- select upper(nombre)  from comercioit.paises;
-- select lower(nombre)  from comercioit.paises;

-- select concat_ws(";" , upper(nombre), capital, (ID*10) ) as pais_capital from comercioit.paises;

-- select left(nombre, 3) as abreviatura  from comercioit.paises;

-- select right(nombre, 3) as abreviatura  from comercioit.paises;

-- select substring(nombre, 2, 4) as abreviatura  from comercioit.paises; # Devuelve un substr donde empieza y cuantos caracteres necesito

-- select nombre, char_length(nombre) from comercioit.paises;

-- select nombre, locate("gentina", nombre) as posicion from comercioit.paises;

-- select rtrim((ltrim("           PEDRO PEREZ      "))) as nombre ;

-- select trim("           PEDRO PEREZ      ") as nombre ;

-- select nombre, replace(capital, "Aires", "AIRES")  as capitales from comercioit.paises;

# Funciones de Fecha


-- select * from comercioit.paises;

-- select *, year(independencia) as anio_independencia from comercioit.paises;

-- select *, curdate() as hoy, year(independencia) as anio_independencia from comercioit.paises;

-- select *, datediff(curdate(), independencia) as dias_desde from comercioit.paises;

-- select *, datediff(curdate(), independencia)/365 as anios_desde from comercioit.paises;

-- select *, timestampdiff(year, independencia, curdate()) as anios_desde from comercioit.paises;

-- select dayname(curdate()) as nombre_dia, dayofweek(curdate()) as dia_de_la_semana, dayofyear(curdate()) as dia_del_anio, monthname(curdate()) as nombre_mes

-- select curdate() as hoy, adddate(curdate(), interval 60 day) as fecha_vencimiento

# Funciones matematicas

-- select * from comercioit.peliculas where rate >= 9;

-- select *, round(rate) as rate_round from comercioit.peliculas where rate >= 9;

-- select *, ceil(rate) as rate_ceil from comercioit.peliculas where rate >= 9;

-- select *, floor(rate) as rate_floor from comercioit.peliculas where rate >= 9;

-- select mod(17, 3) as resto;

select pow(2,3) as cubo_de_dos;

