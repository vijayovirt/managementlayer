#Basic token authentication.
TODO: integrate user and role mangement with ldap authentication

from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
#import jwt
#import datetime
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Spare/Desktop/vijay/todo.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)



@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    print "###############################3 %s" %data
    hashed_password = generate_password_hash(data['password'],method = 'sha256')
    newuser = User(public_id = str(uuid.uuid4()), name = data['name'],
                   password = hashed_password, admin=False)
    db.session.add(newuser)
    db.session.commit()

    return jsonify({'message': 'New user created!'})



def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

@app.route('/user', methods =['GET'])
#@token_required
def get_all_users():
    #if not current_user.admin:
    #    return jsonify({'message': 'Cannot perform that function!'})

    users = User.query.all()
    output = []
    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['admin'] = user.admin
        output.append(user_data)

    return jsonify({'users' : output})

    
if __name__ == '__main__':
    app.run(debug=True)


