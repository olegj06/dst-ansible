import pymysql

def test_mysql_connection():
    # MySQL/MariaDB connection parameters
   # db_host = 'mariadb-server.jobs.fr'
   # db_user = 'wpadmin'
   # db_password = '{{ '
   # db_name = '{{ wp_mysql_db }}'

    try:
        # Establish a connection to the database
        connection = pymysql.connect(host="{{ wp_mysql_host }}", user="{{ wpadmin }}", password= "{{ wp_mysql_password }}",
        database= "{{ wp_mysql_db }}")

        # Create a cursor object
        cursor = connection.cursor()

        # Execute a sample SQL query to test the connection
        cursor.execute("SELECT VERSION()")

        # Fetch the result
        db_version = cursor.fetchone()[0]

        # Check if the database version is retrieved successfully
        assert db_version is not None # , "Failed to retrieve database version"

    except Exception as e:
        # If any exception occurs during the connection or query execution, fail the test
        assert False #,f"Failed to connect to MySQL/MariaDB: {e}"

    finally:
        # Close the database connection
        if connection:
            connection.close()
