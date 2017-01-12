from flask import Flask

app = Flask(__name__)
from sport_sessions_crawling.app import views
