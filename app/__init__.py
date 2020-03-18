from flask import Flask
from .Api import simple_page

app = Flask(__name__)
app.config['TESTING'] = True

app.register_blueprint(simple_page, url_prefix='/pages')

from app import routes