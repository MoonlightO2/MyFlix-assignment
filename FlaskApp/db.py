import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'AccessKeys'

TABLES = {}
TABLES['key'] = (
    "CREATE TABLE if not exists AccessKeys.AccessKey ("
    "  ID int(11) NOT NULL AUTO_INCREMENT,"
    "  username varchar(60) NOT NULL,"
    "  keynum varchar(64) NOT NULL,"
    "  PRIMARY KEY (ID)"
    ") ENGINE=InnoDB")

def create_database(cnx,cursor):
    print ("Trying database creation")
    try:
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET = 'utf8' ".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
    print ("database created")

    for key in TABLES:
        print(key, '->', TABLES[key])
    try:
        cnx.database = DB_NAME
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor)
            cnx.database = DB_NAME
        else:
            print(err)
            exit(1)
    print  ("creating tables"    )
    print (TABLES["key"])

    try:
        
        cursor.execute(TABLES["key"])
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

    cursor.close()
    cnx.close()

def insert_user(cnx,cursor,username,key):
    add_user = ("INSERT INTO AccessKeys.AccessKey "
               "(username,keynum) "
               "VALUES (%s, %s)")
    data_user=(username,key)
    cursor.execute(add_user,data_user)
    cnx.commit()
    cursor.close()
    cnx.close()
