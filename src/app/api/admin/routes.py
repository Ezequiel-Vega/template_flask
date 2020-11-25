from . import admin_bp as app

@app.route('/admin')
def auth():
    return "admin"
