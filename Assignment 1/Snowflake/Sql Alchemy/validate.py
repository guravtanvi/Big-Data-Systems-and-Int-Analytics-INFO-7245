#!/usr/bin/env python

from sqlalchemy import create_engine

#pip install --upgrade snowflake-sqlalchemy

#snowflake://{user}:{password}@{account}.{region}/{database}?role={role}&warehouse={warehouse}

#snowflake://<user_login_name>:<password>@<account_name>/<database_name>/<schema_name>?warehouse=<warehouse_name>&role=<role_name>

engine = create_engine(
      'snowflake://{user}:{password}@{account}/{database}/{schema}?warehouse={warehouse_name}&role={role_name}'.format(
        user='**************',
        password='*********',
        account='********.us-east-1',
        database='sevir',
        schema='public',
        warehouse_name='COMPUTE_WH',
        role_name='sysadmin'

    )
)

try:
    connection = engine.connect()
    results = connection.execute('select * from STORMEVENTS_FATALITIES_2018').fetchone()
    print(results)
finally:
    connection.close()
    engine.dispose()
