import os

# Global Variable Section
DB_FILE = str(os.getcwd()) + "/database.db"
WEB_URL = 'https://ghibliapi.herokuapp.com/'
HEADERS = {'Content-Type': 'application/json'}
SERVICE_PORT = 8000
FMT = '%H:%M:%S'
SINGLE_MINUTE_IN_SECONDS = 60
