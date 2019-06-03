/*
Calculate ratio

select * from a ;

id,cop,name
------
1|1|a
2|1|a
3|1|b
4|1|b
5|2|a
6|2|c


output:
1|a|0.5
1|b|0.5
2|a|0.5
2|c|0.5

*/

select t.cop, t.name, count(*)*1.0/t.ct 
from (
	select cop, name, count() over (partition by cop) as ct
	from a
) t
group by t.cop, t.name
order by t.cop, t.name
