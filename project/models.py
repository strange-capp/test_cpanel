from project import db

class Recipe(db.Model):

    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    image_filename = db.Column(db.String, default=None, nullable=True)
    image_url = db.Column(db.String, default=None, nullable=True)

    def __init__(self, image_filename=None, image_url=None):
        self.image_filename = image_filename
        self.image_url = image_url

    def __repr__(self):
        return '<id: {}>'.format(self.id)
