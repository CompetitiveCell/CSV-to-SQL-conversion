import csv
import mysql.connector

# Open connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger",
    database = "cs_project"
)
cursor = db.cursor()

# Creating the database
# OPTIONAL HERE(comment to prevent unwanted errors)
#cursor.execute("CREATE DATABASE cs_project;")

# Creating the table
# OPTIONAL HERE (comment to prevent unwanted errors)
#cursor.execute("CREATE TABLE ranks(Name char(80), Roll_Number varchar(80), Ranks varchar(80));")

# Read data from the CSV file
with open('rank_data.csv','r', newline = '\r\n') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # Skipping the header row
    
    # CLEARS THE WHOLE TABLE
    cursor.execute("TRUNCATE TABLE rankings;")
    
    # Insert each row of the CSV file into the MySQL database
    for row in csv_reader:
        if row == ['Name', 'Roll_Number', 'Ranks']:
            pass
        else:
            print(row)
            cursor.execute("INSERT INTO rankings(Name, Roll_Number, Ranks) VALUES('{}', {}, {})".format(row[0], row[1], row[2]))
            db.commit()
