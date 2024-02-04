/*データベースシステムsql演習課題*/

/*課題1*/
select * from confederationcup;

/*課題2*/
select name, club from confederationcup;

/*課題3*/
select * from confederationcup where national = "Brazil" and position = "GK";

/*課題4*/
select * from confederationcup where name like "%f%" OR name like "%F%";

/*課題5*/
select position ,count(position) from confederationcup where position = "FW" group by position;

/*課題6*/
select * from confederationcup where club = "Chelsea FC (ENG)" and  position = "MF" ;

/*課題7*/
select position, count(position) from confederationcup group by position;

/*課題8*/

select * from confederationcup where national = "Japan"  order by height desc;

/*課題9*/
select * from confederationcup where year(20231231) - year(birth) >= 44;

/*課題10*/
select * from confederationcup where position = "DF" and height = (select max(height) from confederationcup where position = "DF");

/*課題11*/
select national, avg(height) from confederationcup group by national order by avg(height) desc;

/*課題12*/
select club, count(club) from confederationcup group by club order by count(club) desc limit 0,5;

/*課題13*/
select club, count(club) from confederationcup where club like "%(ITA)%" group by club having count(club) >= 3;
