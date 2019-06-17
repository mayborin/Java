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




# NoSQL

Types:
1. Key-value stores

common use cases: storing user's session data and shopping cart data, cache for applications or databases

examples: Redis, Riak, Amazon DynamoDB

2. Document stores

Databases store data in collections of key-value pairs called documents. Most document stores store data in JSON

Example: MongoDB, CouchDB, Couchbase

3. Column Family Store

Example: BigTable, Cassandra, HBase

4. Graph databases:

Example: Neo4J InfoGrid


### RDBMS vs NOSQL

strength of RDBMS:
1. Maturity
2. Data safety: ACID
  Atomicity: each transaction is all or nothing
  Consistency: any data the transaction modifies or adds follow the rules of each table
  Isolation: if the database runs transactions concurrently to speed up writes, that the outcome of the transactions would be the same if they wre run serially
  Durability: once a transaction is accepted, the data must never be lost
3. Speed and Scale: It is completely possible for an RDBMS to scale but requires complexity
