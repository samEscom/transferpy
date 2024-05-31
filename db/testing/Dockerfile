FROM postgres:15

# Establecer un directorio de trabajo
WORKDIR /docker-entrypoint-initdb.d

# Copiar el archivo SQL al contenedor
COPY init.sql /docker-entrypoint-initdb.d/