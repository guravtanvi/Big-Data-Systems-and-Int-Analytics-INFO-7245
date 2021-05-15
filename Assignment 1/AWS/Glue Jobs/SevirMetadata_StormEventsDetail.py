import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
## @type: DataSource
## @args: [database = "sevir-db", table_name = "metadata_new", transformation_ctx = "DataSource0"]
## @return: DataSource0
## @inputs: []
DataSource0 = glueContext.create_dynamic_frame.from_catalog(database = "sevir-db", table_name = "metadata_new", transformation_ctx = "DataSource0")
## @type: DataSource
## @args: [database = "sevir-db", table_name = "details_2018", transformation_ctx = "DataSource1"]
## @return: DataSource1
## @inputs: []
DataSource1 = glueContext.create_dynamic_frame.from_catalog(database = "sevir-db", table_name = "details_2018", transformation_ctx = "DataSource1")
## @type: Join
## @args: [columnConditions = ["="], joinType = left, keys2 = ["event_id"], keys1 = ["idnew"], transformation_ctx = "Transform0"]
## @return: Transform0
## @inputs: [frame1 = DataSource0, frame2 = DataSource1]
DataSource0DF = DataSource0.toDF()
DataSource1DF = DataSource1.toDF()
Transform0 = DynamicFrame.fromDF(DataSource0DF.join(DataSource1DF, (DataSource0DF['idnew'] == DataSource1DF['event_id']), "left"), glueContext, "Transform0")
## @type: DataSink
## @args: [connection_type = "s3", format = "csv", connection_options = {"path": "s3://staging-dataset/combine-catalog-details/", "partitionKeys": []}, transformation_ctx = "DataSink0"]
## @return: DataSink0
## @inputs: [frame = Transform0]
DataSink0 = glueContext.write_dynamic_frame.from_options(frame = Transform0, connection_type = "s3", format = "csv", connection_options = {"path": "s3://staging-dataset/combine-catalog-details/", "partitionKeys": []}, transformation_ctx = "DataSink0")
job.commit()