Spark has two fundamental sets of APIs: the low-level "unstructured" APIs and the higher-level structured APIs.

To allow every executors to perform work in parallel, spark breaks up the data into chunks called partitions.
A partition is a collection of rows that sit on one physical machine in your cluster.

With dataFrames, you do not manipulate partitions manually or individually

Transformations:
    1. narrow dependencies: each input partition contribute to only one output partition
    2. wide dependency: have input partitions contributing to many output partitions (shuffle)

Actions: trigger computation


Data frame operations are built on top of RDDs and compile down to these lower-level tools for convenient and extremely efficient distributed execution.

RDDs are lower level than DataFrames because they reveal physical execution characteristics (like partitions) to end users.