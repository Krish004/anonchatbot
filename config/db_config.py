import configparser
import sqlite3

config = configparser.ConfigParser()
config.read('db.ini')
connection = sqlite3.connect(config["database"]["name"])
