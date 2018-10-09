import pymysql

# Open database connection
db = pymysql.connect("46.4.115.158", "root", "Mysql@rhombus123", "demo")
lst = []
str = "create table Test ("
x = int(raw_input("Enter length of input: "))
for i in range(x):
     column = (raw_input("enter the column name  "))
     datatype = (raw_input("enter theb datatype Given "))
     #lst.append(y)
     str = str + " " +  column + " " + datatype + " ,"
print(str)
x = str.split()
lst.append(x)
print(lst)
y = lst[0]
print(y)


