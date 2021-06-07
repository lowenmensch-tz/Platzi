

CREATE TABLE User(
    id SERIAL PRIMARY KEY, 
    email VARCHAR(35) UNIQUE NOT NULL COMMENT "Email del usuario",
    password TEXT NOT NULL COMMENT "Contraseña del usuario", 
    first_name TEXT NOT NULL COMMENT "Primer nombre del usuario", 
    last_name TEXT NOT NULL COMMENT "Apellido" , 
    is_admin BIT(1) NOT NULL DEFAULT 0 COMMENT "0 usuario | 1 administrador", 
    bio TEXT NOT NULL COMMENT "Biografía", 
    birthday DATE NOT NULL COMMENT "Fecha de nacimiento",
    created TIMESTAMP NOT NULL DEFAULT NOW() COMMENT "Fecha de creación del perfil",
    modified TIMESTAMP NOT NULL DEFAULT NOW() COMMENT "Fecha en que se actualizó el perfil"
) COMMENT "Tabla de usuario";