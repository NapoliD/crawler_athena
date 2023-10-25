import awswrangler as wr

# Replace the following variables with your specific values
s3_path = 's3://your/file/path'  # Replace with the correct file path
database_name = 'your_database_name'  # Provide your database name
table_name = 'your_table_name'  # Provide your table name

# Store Parquet metadata in AWS Glue Data Catalog
wr.s3.store_parquet_metadata(
    path=s3_path,
    database=database_name,
    table=table_name,
    dataset=True,
    mode="overwrite"
)

print('Metadata successfully stored in AWS Glue Data Catalog.')
