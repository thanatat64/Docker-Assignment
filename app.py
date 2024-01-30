import os
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'db')
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'password')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'MYSQL_DATABASE')

mysql = MySQL(app)

# Routes
@app.route('/users', methods=['GET'])
def get_users():
    # return "test"
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Users')
    users = cur.fetchall()
    cur.close()
    return jsonify({'users': users})

@app.route('/users/<int:uid>', methods=['GET'])
def get_user(uid):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Users WHERE uid = %s', (uid,))
    user = cur.fetchone()
    cur.close()
    if user:
        return jsonify({'user': user})
    else:
        return jsonify({'message': 'User not found'}), 404
    
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    name = data['name']
    age = data['age']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO Users (Fname, age) VALUES (%s, %s)', (name, age))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/users/<int:uid>', methods=['PUT'])
def update_user(uid):
    data = request.json
    name = data['name']
    age = data['age']
    cur = mysql.connection.cursor()
    cur.execute('UPDATE Users SET Fname=%s, age=%s WHERE uid=%s', (name, age, uid))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/users/<int:uid>', methods=['DELETE'])
def delete_user(uid):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Users WHERE uid=%s', (uid,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')