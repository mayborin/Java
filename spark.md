Spark has two fundamental sets of APIs:
the low-level "unstructured" APIs and the higher-level structured APIs.

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
	"untyped" dataFrames, spark maintain types completely and only checks whether these types line up to thoses specified in the schema at run time

3. SQL tables and views

Structured API Execution:
1. Write DataFrame/Dataset/SQL Code
2. If valid code, Spark converts this into a Logical Plan
3. Spark transforms Logical Plan to a Physical Plan, checking for optimizations along the way
4. Spark then executes the Physical Plan (RDD manipulations) on the cluster