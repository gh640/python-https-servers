"""https server with Flask"""

from pathlib import Path

from flask import Flask

STATIC_FOLDER = Path(__file__).resolve().parents[1] / 'htdocs'

application = Flask(__name__, static_url_path='', static_folder=STATIC_FOLDER)
