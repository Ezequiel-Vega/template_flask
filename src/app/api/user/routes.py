from . import user_bp as app

@app.route('/user')
def auth():
    return "User"
