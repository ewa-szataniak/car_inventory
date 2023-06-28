import os
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

# Give access to the project in ANY os we find ourselves in
# Allow outside files/folders to be added to the project from the base directory
load_dotenv(os.path.join(basedir, '.env'))


class Config():
    """
        Set Config variables for the flask app.
        Using Environment variables where available other
        create the config variables if not already not.
    """

    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'First Flask steps to success'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # Turn off database updates from sqlalchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    