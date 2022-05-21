"""https server with Gunicorn"""

from mimetypes import guess_type
from pathlib import Path
from typing import Optional

ROOT_DIR = Path(__file__).resolve().parent.parent / 'htdocs'


def application(environ, start_response):
    path = ROOT_DIR / environ['PATH_INFO'].lstrip('/')

    file = locate_target_file(ROOT_DIR, path)
    if file is None:
        start_response('404 Not Found', [('Content-Length', '0')])
        return iter([b''])

    status = '200 OK'
    data = file.read_bytes()
    (mimetype, encoding) = guess_type(file)
    response_headers = [
        ('Content-type', mimetype),
        ('Content-Length', str(len(data))),
    ]
    start_response(status, response_headers)
    return iter([data])


def locate_target_file(root: Path, path: Path) -> Optional[Path]:
    if path.is_relative_to(root):
        if path.is_file():
            return path
        if path.is_dir():
            index_file = path / 'index.html'
            if index_file.is_file():
                return index_file

    return None
