import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrameCollection
from awsglue.dynamicframe import DynamicFrame

def MyTransform(glueContext, dfc) -> DynamicFrameCollection:
    newdf = dfc.select(list(dfc.keys())[0]).toDF()
    
    from pyspark.sql import functions as sf
    from pyspark.sql.functions import col,substring
    newdf= newdf.withColumn('length', sf.length('id'))
    newdf=newdf.withColumn('IDnew',col('id').substr(sf.lit(2),col('length')))
    newdatadyc= DynamicFrame.fromDF(newdf,glueContext,'newData')
    return(DynamicFrameCollection({"CustomTransform0":newdatadyc},glueContext))

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
## @type: DataSource
## @args: [database = "sevir-db", table_name = "sevir_metadata", transformation_ctx = "DataSource0"]
## @return: DataSource0
## @inputs: []
DataSource0 = glueContext.create_dynamic_frame.from_catalog(database = "sevir-db", table_name = "sevir_metadata", transformation_ctx = "DataSource0")
## @type: ApplyMapping
## @args: [mappings = [("id", "string", "id", "string"), ("file_name", "string", "file_name", "string"), ("img_type", "string", "img_type", "string"), ("time_utc", "string", "time_utc", "string"), ("episode_id", "string", "episode_id", "string"), ("event_id", "string", "event_id", "string"), ("event_type", "string", "event_type", "string"), ("llcrnrlat", "double", "llcrnrlat", "double"), ("llcrnrlon", "double", "llcrnrlon", "double"), ("urcrnrlat", "double", "urcrnrlat", "double"), ("urcrnrlon", "double", "urcrnrlon", "double"), ("size_x", "long", "size_x", "long"), ("size_y", "long", "size_y", "long"), ("height_m", "double", "height_m", "double"), ("width_m", "double", "width_m", "double"), ("data_min", "double", "data_min", "double"), ("data_max", "double", "data_max", "double")], transformation_ctx = "Transform1"]
## @return: Transform1
## @inputs: [frame = DataSource0]
Transform1 = ApplyMapping.apply(frame = DataSource0, mappings = [("id", "string", "id", "string"), ("file_name", "string", "file_name", "string"), ("img_type", "string", "img_type", "string"), ("time_utc", "string", "time_utc", "string"), ("episode_id", "string", "episode_id", "string"), ("event_id", "string", "event_id", "string"), ("event_type", "string", "event_type", "string"), ("llcrnrlat", "double", "llcrnrlat", "double"), ("llcrnrlon", "double", "llcrnrlon", "double"), ("urcrnrlat", "double", "urcrnrlat", "double"), ("urcrnrlon", "double", "urcrnrlon", "double"), ("size_x", "long", "size_x", "long"), ("size_y", "long", "size_y", "long"), ("height_m", "double", "height_m", "double"), ("width_m", "double", "width_m", "double"), ("data_min", "double", "data_min", "double"), ("data_max", "double", "data_max", "double")], transformation_ctx = "Transform1")
## @type: CustomCode
## @args: [dynamicFrameConstruction = DynamicFrameCollection({"Transform1": Transform1}, glueContext), className = MyTransform, transformation_ctx = "Transform2"]
## @return: Transform2
## @inputs: [dfc = Transform1]
Transform2 = MyTransform(glueContext, DynamicFrameCollection({"Transform1": Transform1}, glueContext))
## @type: SelectFromCollection
## @args: [key = list(Transform2.keys())[0], transformation_ctx = "Transform0"]
## @return: Transform0
## @inputs: [dfc = Transform2]
Transform0 = SelectFromCollection.apply(dfc = Transform2, key = list(Transform2.keys())[0], transformation_ctx = "Transform0")
## @type: DataSink
## @args: [connection_type = "s3", format = "csv", connection_options = {"path": "s3://staging-dataset/metadata-new/", "partitionKeys": []}, transformation_ctx = "DataSink0"]
## @return: DataSink0
## @inputs: [frame = Transform0]
DataSink0 = glueContext.write_dynamic_frame.from_options(frame = Transform0, connection_type = "s3", format = "csv", connection_options = {"path": "s3://staging-dataset/metadata-new/", "partitionKeys": []}, transformation_ctx = "DataSink0")
job.commit()