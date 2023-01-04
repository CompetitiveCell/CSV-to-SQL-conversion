import mysql.connector as mysql
import csv

file = open("database.csv", "w")
write = csv.writer(file)
connection = mysql.connect(host = "localhost", user = "root", passwd = "tiger", database = "cs_project")

#Cursor intialization
cursor = connection.cursor()

data = "select * from rankings;"
cursor.execute(data)

rows_data = cursor.fetchall()
write.writerow(["Name", "Roll_Number", "Ranks"])
count = cursor.rowcount
for i in range(len(rows_data)):
    unit_1 = rows_data[i]
    data_list = unit_1
    print(data_list)
    write.writerow(data_list)

print("Data Transfer Finished")
