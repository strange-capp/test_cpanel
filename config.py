import os


class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(BASE_DIR, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOADS_DEFAULT_DEST = os.path.join(BASE_DIR, 'project/static/img/')
    UPLOADS_DEFAULT_URL = 'http://localhost:5000/static/img/'

    UPLOADED_IMAGES_DEST = os.path.join(BASE_DIR, 'project/static/img/')
    UPLOADED_IMAGES_URL = 'http://localhost:5000/static/img/'

    SECRET_KEY = 'sddkgfbkdsjnjkdjdsjek'
