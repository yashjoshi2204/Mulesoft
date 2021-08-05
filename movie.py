import sqlite3
conn=sqlite3.connect('film.db')
cr=conn.cursor()

command1=""" CREATE TABLE IF NOT EXISTS film(name TEXT PRIMARY KEY,actor TEXT,actress TEXT, director TEXT,year INTEGER) """

cr.execute(command1)

cr.execute("INSERT INTO film VALUES('WAR','Hrithik roshan','Vaani Kapoor','Siddharth Anand','2019')")
cr.execute("INSERT INTO film VALUES('Kabir Singh','Shahid Kapoor','Kiara Advani','Sandeep Reddy Vanga','2019')")
cr.execute("INSERT INTO film VALUES('Sanju','Ranbir Kapoor','Anushka Sharma','Rajkumar Hirani','2018')")
cr.execute("INSERT INTO film VALUES('Dangal','Aamir Khan','Kiran Rao','Nitesh Tiwari','2016')")
cr.execute("INSERT INTO film VALUES('PK','Aamir Khan','Anushka Sharma','Rajkumar Hirani','2014')")

cr.execute("SELECT * FROM film")
results=cr.fetchall()

cr.execute("SELECT * FROM film WHERE actress='Anushka Sharma' ")
results2=cr.fetchall()

#print the results
print(results)

print(results2)