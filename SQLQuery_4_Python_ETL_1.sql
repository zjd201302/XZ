use XZ;

-- drop table Questionaire_stg;

Create table Questionaire_stg
(
Question varchar(100)
, Answer varchar(1000)
);


insert into Questionaire_stg values ('123', '234');

select * from Questionaire_stg;


select * from XZ.dbo.Questionaire_stg

truncate table  XZ.dbo.Questionaire;

create table  XZ.dbo.Questionaire
(
Provider varchar(100)
, Eff_DT  date
, TIN_1  varchar(15)
, TIN_2  varchar(15)
, Certificate varchar(20)
, Care_plan varchar(30)
, Clinical_Path_Way  varchar(50)
 , Load_STP date default getdate()
);

select * from XZ.dbo.Questionaire;

insert into XZ.dbo.Questionaire (Provider, Eff_DT, TIN_1, Tin_2, Certificate, Care_plan, Clinical_Path_Way) 
select  Provider, Efftive_Date, TIN_1, TIN_2, Certificate, Care_Plan, Cinical_Pathway
 from XZ.dbo.Questionaire_stg
 pivot
 (max(answer) for question in (Provider, Efftive_Date, TIN_1, TIN_2, Certificate, Care_Plan, Cinical_Pathway
)
 ) pivotTable

