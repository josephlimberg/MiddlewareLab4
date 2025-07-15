CREATE DATABASE saludosdb;
USE saludosdb;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100)
);

-- Insertar datos manualmente
INSERT INTO usuarios (nombre, apellido) VALUES 
('Alexa', 'Silvan');
('Juan', 'Porta');
('Alexander','Torre');

DELIMITER //

CREATE PROCEDURE GetSaludo(IN nombre_in VARCHAR(100), OUT saludo VARCHAR(255))
BEGIN
    DECLARE ape VARCHAR(100);

    SELECT apellido INTO ape FROM usuarios WHERE nombre = nombre_in LIMIT 1;

    IF ape IS NOT NULL THEN
        SET saludo = CONCAT('¡Hola, ', nombre_in, ' ', ape, '! Bienvenido al sistema.');
    ELSE
        SET saludo = CONCAT('Nombre "', nombre_in, '" no encontrado en la base de datos.');
    END IF;
END //

DELIMITER ;


CREATE USER 'admin'@'%' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON saludosdb.* TO 'admin'@'%';
FLUSH PRIVILEGES;