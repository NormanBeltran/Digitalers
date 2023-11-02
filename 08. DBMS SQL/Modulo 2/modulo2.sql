# Select From

-- select nombre, salario_minimo as minimo_en_usd from comercioit.paises;
-- select nombre, habitantes, "Latinoamerica" as continente from comercioit.paises;

-- select nombre, salario_minimo from comercioit.paises order by Salario_Minimo desc;

-- select nombre, Capital, Salario_Minimo from comercioit.paises  order by capital LIMIT 5;

-- select id, nombre, Capital, Salario_Minimo from comercioit.paises  LIMIT 5 offset 2;

-- select id, nombre, Capital, Salario_Minimo, (Salario_Minimo * 1.1) as salario_proyectado  from comercioit.paises;

# Where
-- select * from comercioit.paises where Salario_Minimo > 300;

-- select * from comercioit.paises where Salario_Minimo = 450;

-- select * from comercioit.paises where Salario_Minimo <> 450;

-- select * from comercioit.paises where Salario_Minimo > 300 and habitantes > 10 ;

-- select * from comercioit.paises where Salario_Minimo > 300 and not habitantes > 10 ;

-- select * from comercioit.paises where Salario_Minimo between 200 and 400;

-- select * from comercioit.paises where nombre not in ("Bolivia", "Brasil");

# Like / No Like

-- select * from comercioit.paises where capital like '%o%';

-- select * from comercioit.paises where capital like '%o';

-- select * from comercioit.peliculas where genre like '_r%';


-- select * from comercioit.peliculas where title like '%\_%';

select * from comercioit.contactos where MiddleName is not null;




