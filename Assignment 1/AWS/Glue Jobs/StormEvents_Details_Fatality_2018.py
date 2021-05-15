import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
## @type: DataSource
## @args: [database = "sevir-db", table_name = "details_2018", transformation_ctx = "DataSource0"]
## @return: DataSource0
## @inputs: []
DataSource0 = glueContext.create_dynamic_frame.from_catalog(database = "sevir-db", table_name = "details_2018", transformation_ctx = "DataSource0")
## @type: ApplyMapping
## @args: [mappings = [("episode_id", "long", "Episode_ID", "long"), ("event_id", "long", "Event_ID", "long"), ("state", "string", "State", "string"), ("state_fips", "long", "State_Fips", "long"), ("year", "long", "Year", "int"), ("month_name", "string", "Month_Name", "string"), ("event_type", "string", "Event_Type", "string"), ("cz_fips", "long", "County_Fips", "long"), ("cz_name", "string", "County_Name", "string"), ("begin_date_time", "string", "Begin_Date_Time", "date"), ("end_date_time", "string", "End_Date_Time", "date"), ("injuries_direct", "long", "Injuries_Direct", "int"), ("injuries_indirect", "long", "Injuries_Indirect", "int"), ("deaths_direct", "long", "Deaths_Direct", "int"), ("deaths_indirect", "long", "Deaths_Indirect", "int"), ("damage_property", "string", "Damage_Property", "string"), ("damage_crops", "string", "Damage_Crops", "string"), ("magnitude", "double", "Magnitude", "double"), ("magnitude_type", "string", "Magnitude_Type", "string"), ("tor_f_scale", "string", "Tornado_Scale", "string"), ("tor_other_wfo", "string", "Tornado_other_wfo", "string"), ("tor_other_cz_name", "string", "Tornado_other_county_name", "string"), ("begin_range", "long", "Begin_range", "long"), ("begin_azimuth", "string", "Begin_azimuth", "string"), ("begin_location", "string", "Begin_location", "string"), ("end_range", "long", "End_range", "long"), ("end_azimuth", "string", "End_azimuth", "string"), ("end_location", "string", "End_location", "string"), ("begin_lat", "double", "Begin_lat", "double"), ("begin_lon", "double", "Begin_lon", "double"), ("end_lat", "double", "End_lat", "double"), ("end_lon", "double", "End_lon", "double")], transformation_ctx = "Transform0"]
## @return: Transform0
## @inputs: [frame = DataSource0]
Transform0 = ApplyMapping.apply(frame = DataSource0, mappings = [("episode_id", "long", "Episode_ID", "long"), ("event_id", "long", "Event_ID", "long"), ("state", "string", "State", "string"), ("state_fips", "long", "State_Fips", "long"), ("year", "long", "Year", "int"), ("month_name", "string", "Month_Name", "string"), ("event_type", "string", "Event_Type", "string"), ("cz_fips", "long", "County_Fips", "long"), ("cz_name", "string", "County_Name", "string"), ("begin_date_time", "string", "Begin_Date_Time", "date"), ("end_date_time", "string", "End_Date_Time", "date"), ("injuries_direct", "long", "Injuries_Direct", "int"), ("injuries_indirect", "long", "Injuries_Indirect", "int"), ("deaths_direct", "long", "Deaths_Direct", "int"), ("deaths_indirect", "long", "Deaths_Indirect", "int"), ("damage_property", "string", "Damage_Property", "string"), ("damage_crops", "string", "Damage_Crops", "string"), ("magnitude", "double", "Magnitude", "double"), ("magnitude_type", "string", "Magnitude_Type", "string"), ("tor_f_scale", "string", "Tornado_Scale", "string"), ("tor_other_wfo", "string", "Tornado_other_wfo", "string"), ("tor_other_cz_name", "string", "Tornado_other_county_name", "string"), ("begin_range", "long", "Begin_range", "long"), ("begin_azimuth", "string", "Begin_azimuth", "string"), ("begin_location", "string", "Begin_location", "string"), ("end_range", "long", "End_range", "long"), ("end_azimuth", "string", "End_azimuth", "string"), ("end_location", "string", "End_location", "string"), ("begin_lat", "double", "Begin_lat", "double"), ("begin_lon", "double", "Begin_lon", "double"), ("end_lat", "double", "End_lat", "double"), ("end_lon", "double", "End_lon", "double")], transformation_ctx = "Transform0")
## @type: DataSource
## @args: [database = "sevir-db", table_name = "fatality_2018", transformation_ctx = "DataSource1"]
## @return: DataSource1
## @inputs: []
DataSource1 = glueContext.create_dynamic_frame.from_catalog(database = "sevir-db", table_name = "fatality_2018", transformation_ctx = "DataSource1")
## @type: ApplyMapping
## @args: [mappings = [("fat_yearmonth", "long", "Fatality_YearMonth", "long"), ("fat_day", "long", "Fatality_Day", "int"), ("fat_time", "long", "Fatality_Time", "long"), ("fatality_id", "long", "Fatality_Id", "long"), ("event_id", "long", "Event_ID", "long"), ("fatality_type", "string", "Fatality_Type", "string"), ("fatality_date", "string", "Fatality_Date", "string"), ("fatality_age", "long", "Fatality_Age", "long"), ("fatality_sex", "string", "Fatality_Sex", "string"), ("fatality_location", "string", "Fatality_Location", "string")], transformation_ctx = "Transform2"]
## @return: Transform2
## @inputs: [frame = DataSource1]
Transform2 = ApplyMapping.apply(frame = DataSource1, mappings = [("fat_yearmonth", "long", "Fatality_YearMonth", "long"), ("fat_day", "long", "Fatality_Day", "int"), ("fat_time", "long", "Fatality_Time", "long"), ("fatality_id", "long", "Fatality_Id", "long"), ("event_id", "long", "Event_ID", "long"), ("fatality_type", "string", "Fatality_Type", "string"), ("fatality_date", "string", "Fatality_Date", "string"), ("fatality_age", "long", "Fatality_Age", "long"), ("fatality_sex", "string", "Fatality_Sex", "string"), ("fatality_location", "string", "Fatality_Location", "string")], transformation_ctx = "Transform2")
## @type: Join
## @args: [keys2 = ["Event_ID"], keys1 = ["Event_ID"], transformation_ctx = "Transform1"]
## @return: Transform1
## @inputs: [frame1 = Transform0, frame2 = Transform2]
Transform1 = Join.apply(frame1 = Transform0, frame2 = Transform2, keys2 = ["Event_ID"], keys1 = ["Event_ID"], transformation_ctx = "Transform1")
## @type: DataSink
## @args: [connection_type = "s3", format = "csv", connection_options = {"path": "s3://staging-dataset/staging/", "partitionKeys": []}, transformation_ctx = "DataSink0"]
## @return: DataSink0
## @inputs: [frame = Transform1]
DataSink0 = glueContext.write_dynamic_frame.from_options(frame = Transform1, connection_type = "s3", format = "csv", connection_options = {"path": "s3://staging-dataset/staging/", "partitionKeys": []}, transformation_ctx = "DataSink0")
job.commit()