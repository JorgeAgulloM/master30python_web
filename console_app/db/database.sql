CREATE DATABASE IF NOT EXISTS master_python;
USE master_python;

CREATE TABLE users(
    id          INT(255) auto_increment NOT NULL,
    username    varchar(100),
    apellidos   varchar(355),
    email       varchar(255) NOT NULL,
    pass_wd     varchar(255) NOT NULL,
    date_reg    date NOT NULL,
    CONSTRAINT pk_users PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE notes(
    id          INT(25) auto_increment NOT NULL,
    user_id     INT(25) NOT NULL,
    title       varchar(255) NOT NULL,
    description MEDIUMTEXT,
    date        date NOT NULL,
    CONSTRAINT pk_notes PRIMARY KEY(id),
    CONSTRAINT fk_note_user FOREIGN KEY(user_id) REFERENCES users(id)
)ENGINE=InnoDb;
