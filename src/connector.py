# https://peewee.readthedocs.io/en/latest/peewee/database.html

from peewee import *


class Connector:
    def __init__(self):
        self.database = MySQLDatabase('mydb', user='rob', password='1111')

    def __connect__(self):
        return self.database.connect(reuse_if_open=True)

    def __close__(self):
        return self.database.close()


if __name__ == '__main__':
    test = Connector()
    test.__connect__()
    test.__close__()
