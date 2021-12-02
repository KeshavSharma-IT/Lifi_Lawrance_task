import sqlite3

# define connection
conn=sqlite3.connect("hospital.db")
print('database created')

# define cursor
cur=conn.cursor()

# create table
sql="""
    create table Hospital_Data(
    Customer_Name VARCHAR(255) NOT NULL,
    Customer_Id VARCHAR(18) PRIMARY KEY NOT NULL,
    Open_Date DATE(8) NOT NULL,
    Last_Consulted_Date DATE(8) NOT NULL,
    Vaccination_Type CHAR(5),
    Doctor_Consulted CHAR(255),
    State CHAR(5),
    Country CHAR(5) NOT NULL,
    Post_Code INT(5),
    DOB DATE(8),
    Active_Customer CHAR(1))

    """
cur.execute(sql)
print("table created sucessfully")


# insert data into table
cur.execute("INSERT INTO hospital_Data VALUES ('Alex','123457','20101012','20121013','MVD','Paul','SA','USA',42516,'06031987','A')")
cur.execute("INSERT INTO hospital_Data VALUES ('John','123458','20101012','20121013','MVD','Paul','TN','IND',42587,'06031987','A')")
cur.execute("INSERT INTO hospital_Data VALUES ('Mathew','123459','20101012','20121013','MVD','Paul','WAS','PHIL',45289,'06031987','A')")
cur.execute("INSERT INTO hospital_Data VALUES ('Matt','12345','20101012','20121013','MVD','Paul','BOS','NYC',45127,'06031987','A')")
cur.execute("INSERT INTO hospital_Data VALUES ('Jacob','1256','20101012','20121013','MVD','Paul','VIC','AU',49875,'06031987','A')")


show=""" 
select * from Hospital_Data
    
    """

result=cur.execute(show)
for i in result:
    print(i)

sql2='''SELECT DISTINCT Country FROM Hospital_Data'''
Countries = conn.execute(sql2)

countrie = []
for i in Countries:
  countrie.append(i[0])
print(countrie)

# Create Table Per Country wise
for i in range(len(countrie)):
  cur.execute('CREATE TABLE "{}" AS SELECT * FROM Hospital_Data WHERE Country = "{}"'.format(countrie[i],countrie[i]))
print("Different table created for different Country")



conn.commit()
conn.close()
