use XZ
go

create table Emp_stage
(
Emp_ID varchar(5)
, FRST_NM varchar(50)
, LAST_NM varchar(50)
, DOB date
, Salary money
, Title	varchar(15)

);



create table Emp
(
Emp_ID varchar(5)
, FRST_NM varchar(50)
, LAST_NM varchar(50)
, DOB date
, Salary money
, Title	varchar(15)

);


select * from Emp_stage;
select * from Emp;

insert into Emp (Emp_ID) values ('A1')