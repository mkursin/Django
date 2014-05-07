create database django_site;
create table guest_book
(
id int not null auto_increment primary key,
username varchar(16),
email varchar(30),
date datetime,
comment longtext
) CHARACTER SET utf8 COLLATE utf8_general_ci;