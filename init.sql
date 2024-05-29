DROP TABLE IF EXISTS user_app;

CREATE TABLE user_app (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200),
    email VARCHAR(200),
    password VARCHAR(200),
    is_active SMALLINT DEFAULT 1,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP
);


DROP TABLE IF EXISTS user_info;
CREATE TABLE user_info (
    id SERIAL PRIMARY KEY,
    user_app_id INTEGER NOT NULL,
    full_name VARCHAR(500),
    address VARCHAR(600),
    phone_number VARCHAR(20),
    is_active SMALLINT DEFAULT 1,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP,
    FOREIGN KEY (user_app_id) REFERENCES user_app(id)
);

DROP TABLE IF EXISTS lu_gender;
CREATE TABLE lu_gender(
    id SERIAL PRIMARY KEY,
    gender VARCHAR(10),
    is_active SMALLINT DEFAULT 1,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP
);

INSERT INTO lu_gender (gender) VALUES ('masculino');
INSERT INTO lu_gender (gender) VALUES ('femenino');
INSERT INTO lu_gender (gender) VALUES ('otro');


DROP TABLE IF EXISTS lu_relationship;
CREATE TABLE lu_relationship(
    id SERIAL PRIMARY KEY,
    relationship VARCHAR(15),
    is_active SMALLINT DEFAULT 1,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP
);

INSERT INTO lu_relationship (relationship) VALUES ('esposo');
INSERT INTO lu_relationship (relationship) VALUES ('esposa');
INSERT INTO lu_relationship (relationship) VALUES ('padre');
INSERT INTO lu_relationship (relationship) VALUES ('madre');

DROP TABLE IF EXISTS beneficiary;
CREATE TABLE beneficiary (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(500),
    gender_id INTEGER NOT NULL,
    relationship_id INTEGER NOT NULL,
    date_of_birthday DATE NOT NULL,
    is_active SMALLINT DEFAULT 1,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP,
    FOREIGN KEY (gender_id) REFERENCES lu_gender(id),
    FOREIGN KEY (relationship_id) REFERENCES lu_relationship(id)
);


DROP TABLE IF EXISTS lu_transfer_status;
CREATE TABLE lu_transfer_status(
    id SERIAL PRIMARY KEY,
    status VARCHAR(20),
    is_active SMALLINT DEFAULT 1,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP
);

INSERT INTO lu_transfer_status (status) VALUES ('pendiente');
INSERT INTO lu_transfer_status (status) VALUES ('completada');
INSERT INTO lu_transfer_status (status) VALUES ('cancelada');


DROP TABLE IF EXISTS transfer;
CREATE TABLE transfer (
    id SERIAL PRIMARY KEY,
    user_app_id INTEGER NOT NULL,
    beneficiary_id INTEGER NOT NULL,
    amount NUMERIC NOT NULL,
    date_of_transfer DATE NOT NULL,
    status_id INTEGER NOT NULL,
    is_active SMALLINT DEFAULT 1,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP,
    FOREIGN KEY (user_app_id) REFERENCES user_app(id),
    FOREIGN KEY (beneficiary_id) REFERENCES beneficiary(id),
    FOREIGN KEY (status_id) REFERENCES lu_transfer_status(id)
);