import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1706926131633 = glueContext.create_dynamic_frame.from_catalog(
    database="de-youtube-cleanseddb",
    table_name="cleansed_csvraw_statisticsdataraw_statistics",
    transformation_ctx="AWSGlueDataCatalog_node******",
)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1706926117048 = glueContext.create_dynamic_frame.from_catalog(
    database="de-youtube-cleanseddb",
    table_name="cleansed_statistics_data",
    transformation_ctx="AWSGlueDataCatalog_node*****",
)

# Script generated for node Join
Join_node1706926223303 = Join.apply(
    frame1=AWSGlueDataCatalog_node1706926131633,
    frame2=AWSGlueDataCatalog_node1706926117048,
    keys1=["category_id"],
    keys2=["id"],
    transformation_ctx="Join_node1706926223303",
)

# Script generated for node Amazon S3
AmazonS3_node1706926442619 = glueContext.getSink(
    path="s3://de-youtube-analyticsoutput",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=["region", "category_id"],
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1706926442619",
)
AmazonS3_node1706926442619.setCatalogInfo(
    catalogDatabase="de_youtube_analyticsoutput",
    catalogTableName="de-youtube-analyticstable",
)
AmazonS3_node1706926442619.setFormat("glueparquet", compression="snappy")
AmazonS3_node1706926442619.writeFrame(Join_node1706926223303)
job.commit()
