DROP TABLE IF EXISTS lectores CASCADE;

CREATE TABLE lectores (
    numero    BIGSERIAL    PRIMARY KEY,
    nombre    VARCHAR(255) NOT NULL,
    apellidos VARCHAR(255),
    telefono  VARCHAR(255)
);

DROP TABLE IF EXISTS libros CASCADE;

CREATE TABLE libros (
    codigo      VARCHAR(13)  PRIMARY KEY,
    titulo      VARCHAR(255) NOT NULL,
    num_paginas SMALLINT     NOT NULL CHECK (num_paginas >= 0),
    lector      BIGINT       REFERENCES lectores (numero)
);

-- Datos de prueba:

INSERT INTO lectores (nombre, apellidos, telefono)
VALUES ('Juan', 'Martínez Peña', '666555444'),              -- 1
       ('María', 'González Rodríguez', '654456546');        -- 2

INSERT INTO libros (codigo, titulo, num_paginas, lector)
VALUES ('1111111111111', 'El nombre de la rosa', 637, 2),   -- Prestado a María
       ('2222222222222', 'Cien años de soledad', 591, NULL),
       ('3333333333333', 'Toma el dinero y corre', 200, 1); -- Prestado a Juan
