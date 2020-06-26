from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, configure_uploads
from config import Config



################
#### config ####
################

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

images = UploadSet('images')
configure_uploads(app, images)
