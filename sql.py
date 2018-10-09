'''import pymysql

# Open database connection
db = pymysql.connect("46.4.115.158", "root", "Mysql@rhombus123", "demo" )

# prepare a cursor object using cursor() method
x = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """"""
try:
   # Execute the SQL command
   x.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
import pymysql

# Open database connection
db = pymysql.connect("46.4.115.158","root","Mysql@rhombus123","demo" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO ron(date,
   time) VALUES (23-09-1995, 04:09:20)"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()'''
import pymysql

# Open database connection
db = pymysql.connect("46.4.115.158","root","Mysql@rhombus123","demo")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
#sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#   LAST_NAME, AGE, SEX, INCOME)
#   VALUES ('Ronil', 'Lalita', 22, 'M', 2007)"""
count = 0
while (count < 2):
  first = raw_input("Enter the Value string: ")
  second = raw_input("Enter the Value no: ")
  third = raw_input("Enter the Value no: ")
  four = raw_input("Enter the Value no: ")
  five = raw_input("Enter the Value no: ")
  count = count + 1
  print(first)
  print(second)
  print(third)
  print(four)
  print(five)

  try:
   cursor.execute("""INSERT INTO suriya VALUES (%s,%s,%s,%s,%s)""",(first, second, third, four, five))
   print("Successfully Inserted")
   # Commit your changes in the database
   db.commit()
  except:
          # disconnect from server
   db.rollback()
   print("Not Successful")
   db.close()
          '''

import pymysql

# Open database connection
db = pymysql.connect("46.4.115.158","root","Mysql@rhombus123","demo" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
first_name = raw_input("Enter the name given: ")
# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM sah where name = " + "'" +  first_name + "'"
print(sql)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   x = results.__len__()
   print(x)
   if x == results:
    for i in results:
           lname = i[1]
           print(int(raw_input("Enter no")))
       else:
           x = i[0]
           y = i[1]
           print(str(y))
           db.commit()

except:
        db.rollback()
        print ("Error: unable to fetch data")

# disconnect from server
        db.close()





