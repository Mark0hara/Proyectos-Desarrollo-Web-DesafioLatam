-- 1. Obtener el ID de la película “Titanic”
SELECT id AS id_titanic
FROM peliculas 
WHERE "Titulo" = 'Titanic';

-- 2. Listar a todos los actores que aparecen en "Titanic"
SELECT r.actor
FROM reparto r
JOIN peliculas p ON r.id_pelicula = p.id
WHERE p."Titulo" = 'Titanic';

-- 3. Consultar en cuántas películas del top 100 participa Harrison Ford
SELECT COUNT(*) AS total_peliculas_harrison_ford
FROM reparto r
JOIN peliculas p ON r.id_pelicula = p.id
WHERE r.actor = 'Harrison Ford';

-- 4. Películas estrenadas entre 1990 y 1999 ordenadas por título ascendente
SELECT "Titulo", "Año estreno"
FROM peliculas
WHERE "Año estreno" BETWEEN 1990 AND 1999
ORDER BY "Titulo" ASC;

-- 5. Mostrar títulos con su longitud nombrada como "longitud_titulo"
SELECT "Titulo", LENGTH("Titulo") AS longitud_titulo
FROM peliculas;

-- 6. Consultar cuál es la longitud más grande entre todos los títulos
SELECT MAX(LENGTH("Titulo")) AS maxima_longitud
FROM peliculas;