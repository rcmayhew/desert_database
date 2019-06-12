# https://peewee.readthedocs.io/en/latest/peewee/database.html

from peewee import *
import os


class PassLoader:
    def __init__(self):
        user = os.getlogin()
        self.path = "C:/Users/" + user + "/Documents/Python Scripts/pwd.txt"
        self.cred = ()

    def read_creds(self):
        passes_file = open(self.path, "r")
        self.cred = [line[:-1] for line in passes_file]

    def load_creds(self):
        return self.cred


database_details = PassLoader()
database_details.read_creds()
passwords = database_details.load_creds()

mysql_db = MySQLDatabase(passwords[0], host=passwords[1], port=int(passwords[2]),
                        user=passwords[3], password=passwords[4])


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
        return self.get(self.name == 'test')

    def add_test_item(self):
        self.create(name='test', xCoor=0, yCoor=0)

if __name__ == '__main__':
    x = Item()
    x.add_test_item()
    print(x.print_table())
