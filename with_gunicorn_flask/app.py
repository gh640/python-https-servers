"""https server with Flask"""

from pathlib import Path

from flask import Flask

STATIC_FOLDER = str(Path(__file__).resolve().parent.parent / 'htdocs')

application = Flask(__name__, static_url_path='', static_folder=STATIC_FOLDER)
