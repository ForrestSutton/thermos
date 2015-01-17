#!/usr/bin/python

from app import app, db
from app.models import User
from flask.ext.script import Manager, prompt_bool

manager = Manager(app)

@manager.command
def initdb():
	db.create_all()
	db.session.add(User(username="forrest", email="forrest@example.com"))
	db.session.add(User(username="reindert", email="reindert@example.com"))
	db.session.commit()
	print 'Initialized the database'

@manager.command
def dropdb():
	if prompt_bool(
	    "Are you sure you want to lose all your data?"):
		db.drop_all()
		print 'Dropped the database'

if __name__ == '__main__':
    manager.run()
