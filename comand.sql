.open example.db



CREATE TABLE IF NOT EXISTS notas
    (ID INTEGER PRIMARY KEY AUTO_INCREMENT, 
     nombre text, 
     puntaje1 integer, 
     puntaje2 integer,
     puntaje3 integer,
     puntaje4 integer,
     notafinal integer);

INSERT INTO notas (nombre)
VALUES
  ("Juan"),
  ("Sara"),
  ("Rocio"),
  ("Julio"),
  ("Leo");
