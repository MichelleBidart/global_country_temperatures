CREATE TABLE global_land_temperatures (
    id SERIAL PRIMARY KEY,
    country VARCHAR(255),
    year INTEGER,
    temperature FLOAT
);