import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

sparkContext = SparkContext.getOrCreate()
glueContext = GlueContext(sparkContext)
spark = glueContext.spark_session
job = Job(glueContext)


df = spark.read.option("header","true").option("inferSchema","true").csv('s3://ik-city-data/CityData/*.csv')
print(df.printSchema())
print(df.show())
df.write.partitionBy('Country').mode('append').format('parquet').save('s3://ik-city-data/ParquetCityData/')


job.commit()
