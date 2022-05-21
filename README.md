# Python https servers

Examples of an https server for development. **Never use them for production.**

## Samples

There're 3 samples.

1. Python standard libraries
2. Gunicorn
3. Gunicorn + Flask

## Usage

### Preparation

Generate a self-signed certificate and name it `localhost.pem`.

```bash
cd python-https-servers/
openssl req -x509 -new -days 365 -nodes \
  -keyout localhost.pem \
  -out localhost.pem \
  -subj "/CN=localhost"
```

```text
Generating a 2048 bit RSA private key
.....................................................................................................................................+++
........+++
writing new private key to 'localhost.pem'
-----
```

### 1. Python standard libraries

Just execute `run-python.sh`.

```bash
./run-python.sh
```

### 2. Gunicorn

Install the required packages with [Poetry](https://python-poetry.org/) or `pip`.

```bash
poetry install
# or
python3 -m pip install gunicorn
```

Then execute `run-gunicorn.sh`.

```bash
./run-gunicorn.sh
```

### 3. Gunicorn + Flask

Install the required packages with Poetry or `pip`.

```bash
poetry install
# or
python3 -m pip install gunicorn Flask
```

Then execute `run-gunicorn-flask.sh`.

```bash
./run-gunicorn-flask.sh
```

You can view the sample html file on your browser with `https://localhost`.

```bash
open https://localhost
```

## Files

```text
├── README.md: This file
├── gunicorn.conf.py: Config file for Gunicorn
├── htdocs: Served directory
├── localhost.pem: Self-signed certificate (You need to create this.)
├── poetry.lock: Poetry lock file (You don't need this if you don't use Poetry)
├── pyproject.toml: Poetry project file (You don't need this if you don't use Poetry)
├── run-gunicorn-flask.sh: Script to run `with_gunicorn_flask/app.py`
├── run-gunicorn.sh: Script to run `with_gunicorn/app.py`
├── run-python.sh: Script to run `with_python/server.py`
├── with_gunicorn
│   └── app.py: Sample with Gunicorn
├── with_gunicorn_flask
│   └── app.py: Sample with Gunicorn and Flask
└── with_python
    └── server.py: Sample with Python standard libraries
```

## Reference

- [`http.server` HTTP servers — Python 3 documentation](https://docs.python.org/3/library/http.server.html)
- [`ssl` TLS/SSL wrapper for socket objects — Python 3 documentation](https://docs.python.org/3/library/ssl.html)
- [Creating an HTTPS server in Python · Martin Pitt](https://piware.de/2011/01/creating-an-https-server-in-python/)
- [simple-https-server.py · GitHub](https://gist.github.com/dergachev/7028596)
- [Simple Python HTTP(S) Server Example · AnvilEight Blog](https://blog.anvileight.com/posts/simple-python-http-server/)
