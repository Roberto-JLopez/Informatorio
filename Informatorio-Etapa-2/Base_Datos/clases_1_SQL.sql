-- esta son las dos maneras para crear
create database personas_db;
create schema personas_db;

use personas_db;
-- eliminar la db
drop schema personas_db;

-- Esto es un comentario 
-- Create Read Update Delete
create table personas(
id int primary key auto_increment not null,
nombre varchar(50) not null,
apellido varchar(50) not null,
direccion varchar(100)

);
-- hacer un insert dentro de la tabla
insert into personas(nombre, apellido,direccion)
value ('Jose', 'Gonzalez','av laprida');

-- hacer multiples insets dentro de la tabla
insert into personas(nombre, apellido,direccion)
values('Ricardo','Luza','av san martin'),
('Felipe','Lizz','mendoza'),
('Santi','Lezca','ayacucho'),
('Rodro','Joez','argentina')
;
-- ver los datos de la tabla persona
select * from personas;
-- ver solamente los nombres y apellidos
select nombre, apellido from personas;

-- modificar direccion de la tabla personas el id 2
update personas
set direccion = 'Av Guemes'
where id= 2;
update personas
set edad = 65
where id=5;

-- elimninar el registro con id 1
delete from personas where id =1;

-- modificar la estructura de la tabla (añadimos campo edad)
alter table personas
add column edad int;

-- funciones de sql
select  concat(nombre, ' ', apellido) as Personas from personas;
select sum(edad) as 'suma de edades' from personas;
select  avg (edad) from personas;
select min(edad) as 'edad minima' from personas;
select max(edad) as 'edad maxima' from personas;

--
select nombre, edad from personas order by edad desc; -- asc
--
select * from personas where edad >= 25;

-- nosotros sabemos que la direccion tiene en laguna parte "mar" pero no recordamos cual es
select * from personas where direccion like '%mar%'; -- sino tenemos los _ (guion bajo pero cada guion es un carater)
select * from personas where direccion like '___la%';
