#!/usr/bin/python

from thermos import app, db
from thermos.models import User, Bookmark, Tag
from flask.ext.script import Manager, prompt_bool
from flask.ext.migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
#
# @manager.command
# def initdb():
# 	db.create_all()
# 	db.session.add(User(username="forrest", email="forrest@example.com", password="test"))
# 	db.session.add(User(username="reindert", email="reindert@example.com", password="test"))
# 	db.session.commit()
# 	print 'Initialized the database'

@manager.command
def insert_data():
	forrest = User(username="forrest", email="forrest@example.com", password="test")
	db.session.add(forrest)

	def add_bookmark(url, description, tags):
		db.session.add(Bookmark(url=url, description=description, user=forrest, tags=tags))

		for name in ["python", "flask", "webdev", "programming", "training", "news", "orm"]:
			db.session.add(Tag(name=name))
		db.session.commit()

        add_bookmark("http://www.python.org", "Python - my favorite language", "python")
        add_bookmark("http://flask.pocoo.org", "flask - web development one drop at a time", "flask")
        add_bookmark("http://www.reddit.con", "reddit the front page of the internet", "news")

        reindert = User(username="riendert", email="reindert@example.com", password="test")
        db.session.add(forrest)

@manager.command
def dropdb():
	if prompt_bool(
	    "Are you sure you want to lose all your data?"):
		db.drop_all()
		print 'Dropped the database'

if __name__ == '__main__':
    manager.run()
