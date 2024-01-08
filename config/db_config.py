import configparser
import sqlite3

config = configparser.ConfigParser()
config.read('db.ini')

connection = sqlite3.connect(config["database"]["name"])
connection.row_factory = sqlite3.Row
cursor = connection.cursor()
