#!/bin/bash

# Esperar a que el servicio de PostgreSQL esté disponible
until pg_isready -h db -p 5432 -U postgres; do
  echo "Esperando a que PostgreSQL esté disponible..."
  sleep 2
done

# Exportar la contraseña para que psql la use automáticamente
export PGPASSWORD=$POSTGRES_PASSWORD

# Ejecutar el script SQL para crear las tablas
psql -h db -U postgres -d temperatures -f /scripts/create_tables.sql