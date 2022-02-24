# Background of the project

This project is a small demonstration of regarding using a relational/SQL database.
Because there is not yet much data relational/SQL database is suitable.
At frist the modelling is designed according to the star schema.
The fact table, "songplays", is created then some dimension tables.
Because it is a relational database it is suitable to first create the tables and then the queries.
The queries can be of different kinds:
 - It could be useful to know the maximal duration of all songs
 - To know how many songs an atrist published in general
 - Which users listens to which songs
 - etc.

## The reason for this database design:

 - Star schema because the data simple enough to not need snowflake schema
 - Small dataset
 - Queries are not known yet
 - Perfect use case for using SQL
 - Flexibility to alter the tables
 
## Schema description:

 - There is one fact table "songplays". Each record is a union of played songs and log data.
 - There are five dimension tables:
     - "users": Entities using the app
     - "songs" Available songs
     - "artists": Artists of the songs
     - "time": Containing the timestamps for the rows in the fact table (e.g. year, month, day,hours, minute of the entry)
 
## ETL Pipeline:

 1. Retrieve all files from directory
 2. Iterate over file (-paths), extract information from *.json
 3. Insert each one into the database
 
## Files in this repo:

 - sql_queries.py -> Cotains all SQL queries which are used
 - create_tables.py -> Initiate database, i.e. establish connection, drop existing tables, create tables (star schema)
 - etl.py -> Retrieve data and insert into database tables
 
## How to run the scripts:

1. Run create_tables.py to initiate tables/settings
2. Run etl.py to process the data