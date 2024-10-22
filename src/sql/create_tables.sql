CREATE SCHEMA IF NOT EXISTS survey;

CREATE EXTENSION postgis;
SELECT * FROM pg_extension WHERE extname = 'postgis';

CREATE TABLE survey.fact_sample (
    global_id VARCHAR(255),
    objectid INT,
    fecha TIMESTAMP,
    encargado VARCHAR(255),
    finca VARCHAR(255),
    lote VARCHAR(255),
    sublote VARCHAR(255),
    creationdate TIMESTAMP,
    creator VARCHAR(255),
    editdate TIMESTAMP,
    editor VARCHAR(255),
    shape GEOGRAPHY,

    PRIMARY KEY (global_id)
);


CREATE TABLE survey.dim_sample (
    objectid INT PRIMARY KEY ,
    globalid VARCHAR(255),
    estado VARCHAR(1),
    fruta VARCHAR(255),
    parentglobalid VARCHAR(255),
    creationdate TIMESTAMP,
    creator VARCHAR(255),
    editdate TIMESTAMP,
    editor VARCHAR(255),
    shape geometry,
    CONSTRAINT fk_object_id FOREIGN KEY (parentglobalid) REFERENCES survey.fact_sample(global_id)
);
