# This file contains the methods that maintain the database. 

import sqlite3
from app import app
from flask import g

def connect_db():
    '''# Database connection and querying'''
    # connects to the specific database
    rv = sqlite3.connect('test.db')
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    '''# returns the db connection'''
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    '''# closes the database at the end of the request'''
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def query_db(query, args=(), one=False):
    '''# will allow you to grab one piece of data from the database at a time'''
    cursor = get_db().execute(query, args)
    rv = cursor.fetchall()
    cursor.close()
    return (rv[0] if rv else None) if one else rv

def add_query(query, args=None):
    '''#execute insert queries'''
    db = get_db()
    if args:
        db.execute(query, args) # figured out what args was for
    else:
        db.execute(query) 
    db.commit()