import psycopg2

from config.get_config import get_config


connection = None

try:
    db_params = get_config("config/config.yaml")
    print(db_params)
    connection = psycopg2.connect(**db_params, connect_timeout=3)
    cursor = connection.cursor()

    table_query = """
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public';
    """
    cursor.execute(table_query)

    table_names = cursor.fetchall()

    print("Table Names:")
    for table in table_names:
        print(table[0])

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL:", error)

finally:
    if connection:
        cursor.close()
        connection.close()
