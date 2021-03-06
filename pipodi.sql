
create schema pipodi;

create table pipodi.manager(
    id serial primary key,
    email text not null,
    password text not null,
    created timestamp not null default now()
);

insert into pipodi.manager(email, password) values('root', 'root');

create table pipodi.customer(
    id serial primary key,
    email text not null,
    password text not null,
    name text,
    phone text,
    adress text,
    postcode text,
    confirm_email boolean not null default false,
    created timestamp not null default now()
);
