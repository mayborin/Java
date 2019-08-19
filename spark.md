Spark has two fundamental sets of APIs:

1. the low-level "unstructured" APIs
    1. manipulating distributed data (RDDs)
    2. manipulating distributed shared variables (broadcast variables and accumulators)

2. the higher-level structured APIs.

To allow every executors to perform work in parallel, spark breaks up the data into chunks called partitions.
A partition is a collection of rows that sit on one physical machine in your cluster.

With dataFrames, you do not manipulate partitions manually or individually

Transformations:

1. narrow dependencies: each input partition contribute to only one output partition
2. wide dependency: have input partitions contributing to many output partitions (shuffle)

Actions: trigger computation


Data frame operations are built on top of RDDs and compile down to these lower-level tools for convenient and extremely efficient distributed execution.

RDDs are lower level than DataFrames because they reveal physical execution characteristics (like partitions) to end users.

Internally, Spark uses an enginee called Catalyst that maintains its own type information through the planning an processing of work.

Spark types map directly to the different language APIs that Spark maintains and there exists a lookup table for each of these in Scala, Java, Python, SQL and R.


Structured API:

1. Datasets
	"typed" Datasets: check whether types conform to the specification at compile time.
	Datasets are only available to JVM-based language (Scala and Java) and we specify types with case classes or Java beans
2. DataFrames
	"untyped" dataFrames, spark maintain types completely and only checks whether these types line up to those specified in the schema at run time

3. SQL tables and views

Structured API Execution:

1. Write DataFrame/Dataset/SQL Code

2. If valid code, Spark converts this into a Logical Plan

3. Spark transforms Logical Plan to a Physical Plan, checking for optimizations along the way

4. Spark then executes the Physical Plan (RDD manipulations) on the cluster


RDD:
RDD represents an immutable, partitioned collection of records thtat can be operated on in parallel.
The records in RDD are just Java, Scala or Python objects of the programmer's choosing.

Tyeps of RDD:

1. generic RDD type
2. key-value RDD


RDD is characterized by five main properties:

1. a list of partitions

2. a function for computing each split

3. a list of dependencies on other RDDs

4. optionally, a Partitioner for key-value RDDs

5. optionally, a list of preferred locations where to compute each split (eg. block locations for a Hadoop Distributed File System)

***

Word Count example:

```python
import re
from pyspark.sql.functions import desc, udf, explode
from pyspark.sql.types import StringType, ArrayType

def parse(line):
	return map(lambda x: re.sub('[^a-zA-Z-]', '', x), line.split())

parse_udf = udf(parse, ArrayType(StringType()))
tdf  = spark.read.txt('example.txt')
tdf.select(explode(parse_udf(tdf.value)).alias('word')).groupby('word').count().orderBy(desc('count')).show()
```
