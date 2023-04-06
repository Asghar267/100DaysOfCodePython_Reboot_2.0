import sqlite3

conn = sqlite3.connect("qoute.db")
curr = conn.cursor()

# curr.execute("""create table qoutes_tb(title text, author text, tags text) """)
curr.execute("""insert into qoutes_tb values('python', 'webscraping', 'scrapy') """)

conn.commit()

conn.close()