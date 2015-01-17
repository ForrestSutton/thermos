#import os
#from datetime import datetime
#from flask import Flask, render_template, request, redirect, url_for, flash
#from flask_sqlalchemy import SQLAlchemy

#from forms import BookmarkForm
#import models

#basedir = os.path.abspath(os.path.dirname(__file__))


#fake login
#def logged_in_user():
#    return models.User.query.filter_by(username='forrest').first()



#app = Flask(__name__)
#app.config['SECRET_KEY']= '\xb4\xdfj\xd8\n~\x9c\xbc]\xbd\x12S\x8a\xc5\xcb\x05_\xc0\xc4\xf0\xa5\xb0r\xaf'
#app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///'+ os.path.join(basedir, 'thermos.db')
#db = SQLAlchemy(app)
#bookmarks = []


#@app.route('/')
#@app.route('/index')
#def index():
#    return render_template('index.html', new_bookmarks=new_bookmarks(5))

#@app.route('/add', methods=['GET', 'POST'] )
#def add():
#    form = BookmarkForm()		
#    if form.validate_on_submit():
#        url = form.url.data
#	description = form.description.data
#        bm = models.Bookmark(user=logged_in_user(), url=url, description=description)
#        db.session.add(bm)
#        db.session.commit()
        #store_bookmark(url, description)
#        flash("Stored '{}'".format(description))
#        return redirect(url_for('index'))
#    return render_template('add.html', form=form)

#@app.errorhandler(404)
#def page_not_found(e):
#    return render_tempalate('404.html'),404

#@app.errorhandler(500)
#def server_error(e):
#    return render_template('500.html'), 500

#if __name__ == '__main__':
    #app.run(debug=True)

