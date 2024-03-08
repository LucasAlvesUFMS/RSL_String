create database Artigos;
show databases;
use Artigos;

create table artigoCientifico(
    titulo varchar(200),
    autor varchar(200),
    topico varchar(500),
    ano_pub tinyint,
    perguntas varchar(500),
    respotas varchar(500)
);
describe artigoCientifico;