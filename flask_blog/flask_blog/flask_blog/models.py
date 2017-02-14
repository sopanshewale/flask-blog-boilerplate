from datetime import datetime

from flask_blog.core import db
from flask_blog import app


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    summary = db.Column(db.Text)
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    def __init__(self, title, summary, body, pub_date=None):
        self.title = title
        self.summary = summary 
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date

    def __repr__(self):
        return '<Post %r>' % self.title

# models for which we want to create API endpoints
app.config['API_MODELS'] = {'post': Post}

# models for which we want to create CRUD-style URL endpoints,
# and pass the routing onto our AngularJS application
app.config['CRUD_URL_MODELS'] = {'post': Post}

