
from flask import  render_template, flash, redirect, url_for, request, abort
from flask_login import login_required, current_user

from . import bookmarks
from .forms import BookmarkForm
from .. import db
from ..models import User, Bookmark, Tag


@bookmark.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        tags = form.tags.data
        bm = Bookmark(user=current_user, url=url, description=description, tags=tags)
        db.session.add(bm)
        db.session.commit()
        flash("Stored '{}'".format(bm.description))
        return redirect(url_for('index'))
    return render_template('bookmark_form.html', form=form, title="Add a bookmark")

@bookmark.route('/edit/<int:bookmark_id>', methods=['GET', 'POST'])
@login_required
def edit_bookmark(bookmark_id):
bookmark = Bookmark.query.get_or_404(bookmark_id)
if current_user != bookmark.user:
abort(403)
form = BookmarkForm(obj=bookmark)
if form.validate_on_submit():
form.populate_obj(bookmark)
db.session.commit()
    flash("Stored '{}'".format(bookmark.description))
    return redirect(url_for('user', username=current_user.username))
return render_template('bookmark_form.html', form=form, title="Edit bookmark")
