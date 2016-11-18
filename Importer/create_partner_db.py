# import sqlite3 as sql
import json
import os, sys, inspect

from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

from flask import Flask
from model.entities.partnerEntity import *

#=========================================================================
# Initialize
#=========================================================================
     
with open('config.json', 'r') as f:
    config = json.load(f)


app = Flask(__name__)

#=========================================================================
# Run script     
#=========================================================================

if os.path.exists(config.get("database_file")) == False:
    db = SqliteExtDatabase(config.get("database_file"))
    db.connect()
    db.create_tables([Partner])    
        
else:
    print "The database file: ", config.get("database_file"), " has existed!"; 
