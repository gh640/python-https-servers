"""https server with Flask"""

from pathlib import Path

from flask import Flask, render_template

STATIC_FOLDER = Path(__file__).resolve().parents[1] / 'htdocs'
CSS_FOLDER = STATIC_FOLDER / 'css'

application = Flask(
    __name__,
    static_url_path='/css',
    static_folder=CSS_FOLDER,
    template_folder=STATIC_FOLDER,
)


@application.route('/')
def index():
    # Serve `index.html` for `/` as it's not automatically served.
    return render_template('index.html')
