"""https server with Python standard libraries"""

import functools
import ssl
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
CERTFILE = ROOT_DIR / 'localhost.pem'
DIRECTORY = ROOT_DIR / 'htdocs'


def main():
    # http_server()
    https_server(certfile=CERTFILE)


def http_server():
    print('`http_server()` starts...')
    server_address = ('', 80)
    with HTTPServer(server_address, get_handler(DIRECTORY)) as httpd:
        print_server_info(httpd)
        try:
            httpd.serve_forever()
        except Exception as e:
            httpd.server_close()
            raise e


def https_server(*, certfile):
    print('`https_server()` starts...')
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(CERTFILE)

    server_address = ('', 443)
    with HTTPServer(server_address, get_handler(DIRECTORY)) as httpd:
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        print_server_info(httpd)
        try:
            httpd.serve_forever()
        except Exception as e:
            httpd.server_close()
            raise e


def get_handler(directory):
    return functools.partial(SimpleHTTPRequestHandler, directory=directory)


def print_server_info(server):
    print(f"""Server info:
    name: {server.server_name}
    address: {server.server_address}
    """)


if __name__ == '__main__':
    main()
