#! /usr/bin/python3.8

import logging
import sys

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/usr/local/www/flask_downloader/')
from flask_downloader import app as application
# application.secret_key = "my_secret_key"
application.secret_key = os.getenv('FLASK_SECRET_KEY', 'for dev')