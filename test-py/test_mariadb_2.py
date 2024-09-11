import pymysql

def test_mysql_connection():
    # MySQL/MariaDB connection parameters
      db_host = '172.17.0.2'
      db_user = 'wpadmin'
      db_password = 'mysql_pass'
      db_name = 'wpdatabase'
    # db_user = 'root'
    # db_password = ''
    # db_name = ''
      client_ip = '172.17.0.3'
   #client_ip = 'wordpress-server.jobs.fr'
   # Define connection outside the try block
      connection = None

      try:
        # Establish a connection to the database
        connection = pymysql.connect(host=db_host, user=db_user, password=db_password,
                database=db_name,bind_address=client_ip)

        # Create a cursor object
        cursor = connection.cursor()

        # Execute a sample SQL query to test the connection
        cursor.execute("SELECT VERSION()")

        # Fetch the result
        db_version = cursor.fetchone()[0]

        # Check if the database version is retrieved successfully
        assert db_version is not None

      except Exception as e:
        # If any exception occurs during the connection or query execution, fail the test
        assert False # , f"Failed to connect to MySQL/MariaDB: {e}"

      finally:
        # Close the database connection
        if connection:
            connection.close()
