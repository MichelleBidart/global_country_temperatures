CREATE TABLE IF NOT EXISTS global_land_temperatures (
    id SERIAL PRIMARY KEY,
    country VARCHAR(255),
    year VARCHAR(255),
    temperature VARCHAR(255)
);