import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='nasa')
cnx.close()

engine_connection = "mysql+mysqlconnector://root:root@localhost:3306/nasa"