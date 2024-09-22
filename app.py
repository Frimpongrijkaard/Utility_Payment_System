from flask import Flask, request, redirect, url_for, session, flash, render_template
#from models import storage
#from models.user import User
#from werkzeug.security import check_password_hash

#app.secret_key = 'your_secret_key'  # Required for session handling
app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('homepage.html')

if __name__ == '__main__':
    app.run(debug=False)