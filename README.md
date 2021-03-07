# Python https servers

Examples of an https server for development. They work on Python 3.

**These are for development usage and never use them for production.**

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
openssl req -new -x509 -keyout localhost.pem -out localhost.pem -days 365 -nodes
```

Sample dialog of `openssl req`:

```bash
openssl req -new -x509 -keyout localhost.pem -out localhost.pem -days 365 -nodes
Generating a 2048 bit RSA private key
..+++
.........................+++
writing new private key to 'localhost.pem'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) []:xxx
State or Province Name (full name) []:xxx
Locality Name (eg, city) []:xxx
Organization Name (eg, company) []:
Organizational Unit Name (eg, section) []:
Common Name (eg, fully qualified host name) []:localhost
Email Address []:
```

### 1. Python standard libraries

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

Install the requiredpackage with Poetry or `pip`.

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
