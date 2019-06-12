## Enhanced Aggregation, Cube, Grouping and Rollup

#### GROUPING SETS clause

The GROUPING SETS clause in GROUP BY allows us to specify more than one GROUP BY option in the same record set.

GROUP BY a, b, c WITH CUBE is equivalent to 
	GROUP BY a, b, c GROUPING SETS ( (a, b, c), (a, b), (b, c), (a, c), (a), (b), (c), ( ))

GROUP BY a, b, c, WITH ROLLUP is equivalent to
	GROUP BY a, b, c GROUPING SETS ( (a, b, c), (a, b), (a), ( )).

#### Pivot

The syntax for the PIVOT clause in SQL Server (Transact-SQL) is:
```sql
SELECT first_column AS <first_column_alias>,
[pivot_value1], [pivot_value2], ... [pivot_value_n]
FROM 
(<source_table>) AS <source_table_alias>
PIVOT 
(
 aggregate_function(<aggregate_column>)
 FOR <pivot_column>
 IN ([pivot_value1], [pivot_value2], ... [pivot_value_n])
) AS <pivot_table_alias>;
```

#### SQL syntax

1.Case statement

```sql
CASE expression

   WHEN value_1 THEN result_1
   WHEN value_2 THEN result_2
   ...
   WHEN value_n THEN result_n

   ELSE result

END
```

OR

```sql
CASE

   WHEN condition_1 THEN result_1
   WHEN condition_2 THEN result_2
   ...
   WHEN condition_n THEN result_n

   ELSE result

END
```

2.Declare Variables

syntax
```sql
DECLARE @variable_name datatype [ = initial_value ],
        @variable_name datatype [ = initial_value ],
        ...;
SET     @variable_name datatype [ = initial_value ],
        @variable_name datatype [ = initial_value ],
        ...;
```

