# https://peewee.readthedocs.io/en/latest/peewee/database.html

from peewee import *


class Connector:
    def __init__(self):
        self.database = MySQLDatabase('mydb', user='rob', password='1111')

    def __connect__(self):
        return self.database.connect(reuse_if_open=True)

    def __close__(self):
        return self.database.close()


mysql_db = MySQLDatabase('mydb', user='rob', password='1111')


class BaseModel(Model):
    class Meta:
        database = mysql_db


class Item(BaseModel):
    name = TextField()
    xCoor = IntegerField()
    yCoor = IntegerField()
    brand = TextField()
    plane = TextField()

    def print_table(self):
        return self.select(Item.name)


if __name__ == '__main__':
    test = Connector()
    test.__connect__()
    test.__close__()
