create table if not exists factories
(
    id   BIGINT auto_increment,
    name varchar(255) null,
    hash varchar(255) null,
    constraint factory_pk
        primary key (id)
);