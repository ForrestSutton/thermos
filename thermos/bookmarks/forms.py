from flask.ext.wtf import Form
from wtforms.fields import StringField, BooleanField, SubmitField
from flask.ext.wtf.html5 import URLField
from wtforms.validators import DataRequired, Regexp, ValidationError

from models import  Bookmark, Tag

class BookmarkForm(Form):
    url = URLField('The URL for your bookmark:', validators=[DataRequired(), url()])
    description = StringField('description')
    tags = StringField('Tags', validators=[Regexp(r'^[a-zA-Z0-9, ]*$',
                    message="Tags can only contain letters and numbers")])


    def validate(self):
        if not self.url.data.startswith("http://") or\
               self.url.data.startswith("https://"):
               self.url.data = "http://" + self.url.data

        if not Form.validate(self):
            return False

        if not self.description.data:
            self.description.data = self.url.data
