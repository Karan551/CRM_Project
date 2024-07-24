import psycopg
import os
import dotenv

conf = dotenv.dotenv_values()

try:

    with psycopg.connect(

            dbname=str(conf["DATABASE_NAME"]),
            user=str(conf["DATABASE_USER"]),
            password=str(conf["DATABASE_PASSWORD"]),
            host=str(conf["DATABASE_HOST"]),
            port=str(conf["DATABASE_PORT"]),
    ) as conn:

        conn.commit()
    print("Database Connected Successfully.")

except Exception as e:
    print("Database connection issue", e)


