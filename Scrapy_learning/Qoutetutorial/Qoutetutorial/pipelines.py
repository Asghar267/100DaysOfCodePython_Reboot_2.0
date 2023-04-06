# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3

class QoutetutorialPipeline:
    def __init__(self):
        self.create_connetion()
        self.create_table()

    def create_connetion(self):
        self.conn = sqlite3.connect("myqoutes.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute(""" DROP TAbLE IF EXISTS qoutes_tb """)
        self.curr.execute("""create table qoutes_tb(title text, author text, tags text) """)

        # self.curr.execute("""insert into qoutes_tb values('python', 'webscraping', 'scrapy') """)

    def process_item(self, item, spider):
        self.store_db(item)
        print("pipeline:", item['title'][0])
        return item

    def store_db(self, item):
        self.curr.execute("""insert into qoutes_tb values(?,?,?)  """,(item['title'][0],item['author'][0],item['tag'][0]))

        self.conn.commit()
