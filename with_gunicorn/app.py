"""https server with Gunicorn"""

from mimetypes import guess_type
from pathlib import Path

ROOT_DIR = (Path(__file__).resolve().parent.parent / 'htdocs')


def application(environ, start_response):
    path = ROOT_DIR / environ['PATH_INFO'].lstrip('/')

    data = b''
    if path.is_relative_to(ROOT_DIR) and path.is_file():
        data = path.read_bytes()

    status = '200 OK'
    (mimetype, encoding) = guess_type(path)
    response_headers = [
        ('Content-type', mimetype or 'text/plain'),
        ('Content-Length', str(len(data)))
    ]

    start_response(status, response_headers)
    return iter([data])
