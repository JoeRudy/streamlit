from snowflake.snowpark import Session

pars = {
    "account": "xxxxx",
    "user": "xxxxx",
    "password": "xxxxx!",
}

session = Session.builder.configs(pars).create()

df = session.sql("select * from xxxxxxx")

# rows = df.collect()
# for row in rows:
#     print(row)

dfp = df.to_pandas()
print(dfp)
