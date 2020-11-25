from . import auth_bp as app

@app.route('/auth')
def auth():
    return "Auth"
