use django_site;
create table blog
(
id int not null auto_increment primary key,
title varchar(150),
body longtext,
date timestamp
)
character set utf8 collate utf8_general_ci;