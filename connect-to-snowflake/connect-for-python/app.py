import snowflake.connector

conn = snowflake.connector.connect(
    account="xxxxx",
    user="xxxxx",
    password="xxxxx",
    database="xxxxx",
    schema="xxxxx",
    role="xxxxx",
    warehouse="xxxxx",
)

cur = conn.cursor()
cur.execute("select * from xxxxx")

# (1) fetching row by row
# for row in cur:
#     print(row)

# (2) getting the whole set
df = cur.fetch_pandas_all()
print(df)
