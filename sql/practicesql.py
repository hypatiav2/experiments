import sqlite3
conn = sqlite3.connect("newdata.db")
c = conn.cursor()
'''c.execute("drop table users;")
c.execute("CREATE TABLE IF NOT EXISTS users (userid integer primary key autoincrement, first text, last text, emailid text, age integer, phonenumber text, city text);")
def insert(first, last, emailid, age, number, city):
    c.execute("insert into users (first, last, emailid, age, phonenumber, city) values (?,?,?,?,?,?);",(first,last,emailid, age, number, city))
    conn.commit()
    
insert("meryl","mathew","mm23@gmail.com",15,"1234567890","London")
insert("margaret","sanger","meg@gmail.com",56,"8657537890","London")
insert("billy","joel","bj@gmail.com",20,"3974837553","New York")
insert("yoo","Kim","yk@gmail.com",39,"12376427434","Pyeongchang")

c.execute("select userid,first,last,age from users order by first")'''

c.execute("drop table employees;")
c.execute("CREATE TABLE IF NOT EXISTS employees (id integer primary key autoincrement, first text, last text, date date, city text, country text);")
c.execute("CREATE TABLE IF NOT EXISTS customers (id integer primary key autoincrement, name text, city text, country text);")
c.execute("CREATE TABLE IF NOT EXISTS orders (id integer primary key autoincrement, customerid integer, employeeid integer, date date, amount integer, foreign key (customerid) references customers(id), foreign key (employeeid) references employees(id));")

def insert(first, last, date, orders, country):
    c.execute("insert into employees (first, last, date, orders, country) values (?,?,?,?,?);",(first,last,date, orders, country))
    conn.commit()

c.execute("insert into employees (first, last, date, city, country) values (?,?,?,?,?);",("Steve","Liu", "2016-04-12", "Nagasaki", "Japan"))
c.execute("insert into employees (first, last, date, city, country) values (?,?,?,?,?);",("Mary","Jane", "2019-02-08", "London", "U.K"))
c.execute("insert into customers (name, city, country) values (?,?,?);",("Ned Perry", "New York", "U.S"))
c.execute("insert into customers (name, city, country) values (?,?,?);",("May Parker", "Boston", "U.S"))
c.execute("insert into orders (customerid,employeeid,date, amount) values (?,?,?,?);",(1,2,"2020-08-17",150))
c.execute("insert into orders (customerid,employeeid,date, amount) values (?,?,?,?);",(2,2,"2020-08-17",80))
c.execute("SELECT customers.name from customers where id  = (select orders.customerid from orders where orders.amount > 100); ")

scoresheet = c.fetchall()
print(scoresheet)
conn.commit()
c.close()
