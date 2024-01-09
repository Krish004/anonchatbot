import configparser
from peewee import *

config = configparser.ConfigParser()
config.read('db.ini')

DB_USERNAME = config['database']['username']
DB_PASSWORD = config['database']['password']
DB_HOST = config['database']['host']
DB_NAME = config['database']['name']

db = MySQLDatabase(
    host=config["database"]["host"],
    database=config["database"]["name"],
    user=config["database"]["username"],
    password=config["database"]["password"]
)
