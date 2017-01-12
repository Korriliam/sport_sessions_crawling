from sport_sessions_crawling.app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, this is sport_sessions_crawling project"
