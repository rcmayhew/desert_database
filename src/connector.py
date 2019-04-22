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

        print(self.cred)

    def load_creds(self):
        return self.cred


class Connector:
    def __init__(self):
        database_details = PassLoader()
        database_details.read_creds()
        passwords = database_details.load_creds()

        self.database = MySQLDatabase(passwords[0], host=passwords[1], port=int(passwords[2]),
                                      user=passwords[3], password=passwords[4])

    def __connect__(self):
        return self.database.connect(reuse_if_open=True)

    def __close__(self):
        return self.database.close()


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
        return self.select(Item.name)


if __name__ == '__main__':
    test = Connector()
    test.__connect__()
    print("connecting")
    test.__close__()
    print("closeing")