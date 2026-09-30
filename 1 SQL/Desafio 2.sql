-- PREGUNTA 1: ¿Cuántos registros hay?
SELECT COUNT(*) AS total_registros FROM INSCRITOS;

-- PREGUNTA 2: ¿Cuántos inscritos hay en total?
SELECT SUM(cantidad) AS total_inscritos FROM INSCRITOS;

-- PREGUNTA 3: Registros de mayor antigüedad (Subconsulta)
SELECT * FROM INSCRITOS WHERE fecha = (SELECT MIN(fecha) FROM INSCRITOS);

-- PREGUNTA 4: Inscritos por día
SELECT fecha, SUM(cantidad) AS inscritos_dia FROM INSCRITOS GROUP BY fecha ORDER BY fecha;

-- PREGUNTA 5: Día con mayor inscripción
SELECT fecha, SUM(cantidad) AS max_inscritos FROM INSCRITOS GROUP BY fecha ORDER BY max_inscritos DESC LIMIT 1;