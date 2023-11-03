/*データベースシステムsql演習課題*/

/*課題1*/
select * from confederationcup;

/*課題2*/
select name, club from confederationcup;

/*課題3*/
select * from confederationcup where position = "GK";

/*課題4*/
select * from confederationcup where name like "%f%" OR name like "%F%";

/*課題5*/
select position ,count(position) from confederationcup where position = "FW" group by position;

/*課題6*/
select * from confederationcup where club = "Chelsea FC (ENG)" AND  position = "MF" ;

/*課題7*/
select position, count(position) from confederationcup group by position;

/*課題8*/
select * from confederationcup where national = "Japan"  order by height desc;

/*課題9*/
select * from confederationcup where YEAR(birth) + 44 <= YEAR(20231231);

/*課題10*/
select * from confederationcup where position = "DF" AND height = (select max(height) from confederationcup where position = "DF");

/*課題11*/
select national, avg(height) from confederationcup group by national order by avg(height) desc;

/*課題12*/


/*課題13*/