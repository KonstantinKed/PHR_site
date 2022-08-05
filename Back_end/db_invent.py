import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
try: # connection to the current DB
    connection = psycopg2.connect(user='postgres',
                                  password='S1',
                                  host='127.0.0.1',
                                  port='5432',
                                  database='PHR_inventory')
    # connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # Creating cursor class to cooperate with DB
    cursor = connection.cursor()
    # SQL query to create a new table
    # create_table_query = '''CREATE TABLE Apartments
    #                         (Apt_ID VARCHAR(2) PRIMARY KEY NOT NULL,
    #                         Apt_name VARCHAR(15) NOT NULL)'''
    # cursor.execute(create_table_query)
    insert_query = """
INSERT INTO apartments 
VALUES ('5', 'Apartment #5');
INSERT INTO apartments 
VALUES ('6', 'Apartment #6');
INSERT INTO apartments 
VALUES ('7A', 'Apartment #7A');
INSERT INTO apartments 
VALUES ('7B', 'Apartment #7B');
INSERT INTO apartments 
VALUES ('8A', 'Apartment #8A');
INSERT INTO apartments 
VALUES ('8B', 'Apartment #8B');
INSERT INTO apartments 
VALUES ('10', 'Apartment #10');
INSERT INTO apartments 
VALUES ('13', 'Apartment #13');
INSERT INTO apartments 
VALUES ('14', 'Apartment #14');
INSERT INTO apartments 
VALUES ('15', 'Apartment #15');
INSERT INTO apartments 
VALUES ('16', 'Apartment #16');
INSERT INTO apartments 
VALUES ('19', 'Apartment #19');
INSERT INTO apartments 
VALUES ('21', 'Apartment #21');
INSERT INTO apartments 
VALUES ('22', 'Apartment #22');
INSERT INTO apartments 
VALUES ('23', 'Apartment #23');
INSERT INTO apartments 
VALUES ('24', 'Apartment #24')"""
    cursor.execute(insert_query)
    connection.commit()
    print('Table "Apartments" was created')

except (Exception, Error) as error:
    print("Error with PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Connection with PostgreSQL was closed")