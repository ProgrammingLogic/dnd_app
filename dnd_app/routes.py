from flask import url_for, render_template

def init_routes(app, db):
    @app.route('/characters/<user_id>/<character_id>')
    def character(user_id, character_id):
        return f"""User: {user_id}, Character: {character_id}<br>\
                   URL: {url_for('character', user_id=user_id, character_id=character_id)}"""

    @app.route('/')
    def index():
        return 'Index page'
    
    @app.route('/users/<user_id>')
    def users(user_id):
        css = url_for('static', filename='styles.css')

        d_user = {'user_id': user_id, 'username': user_id, 'css_path': css}
        return render_template('profile.html', **d_user)

    @app.route('/login')
    def login():
        return 'Login Please'

    @app.route('/logout')
    def logout():
        return 'Logout Please'
