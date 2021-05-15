import sqlalchemy as sql
import pandas as pd
from sqlalchemy.dialects import registry
import app.snowflakecfg as cfg
import os

registry.register('snowflake', 'snowflake.sqlalchemy', 'dialect')

# Setup an SQL Alchemy Engine object
# This will provide a connection pool for Pandas to use later

engine = sql.create_engine(
    'snowflake://{u}:{p}@{a}/{d}/{s}?warehouse={w}&role={r}'.format(
        u=cfg.snowflake["username"],
        p=cfg.snowflake["password"],
        a=cfg.snowflake["region"],
        r=cfg.snowflake["role"],
        d=cfg.snowflake["database"],
        s=cfg.snowflake["schema"],
        w=cfg.snowflake["warehouse"]
    )
)

try:
    # Directory where the downloaded data is present
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'data'))

    for file in os.listdir(data_dir):

        data = pd.read_csv(data_dir+"\\"+file)
        table_name = file[:-4]  # Removing the extension .csv
        data.to_sql(table_name, con=engine, index=False, if_exists='append', chunksize=16000)
        print("Data loaded in table {t}".format(t=table_name))

finally:
    engine.dispose()
