import  mysql.connector as mysqlcon
mydb = mysqlcon.connect(
    host="localhost",
    user='root',
    password = "1213",
    database = 'online_store')
mycursor = mydb.cursor()
print(mydb)
print(type(mydb))