from flask import Flask, render_template, jsonify, request
from redis import Redis, RedisError
import os 
import socket



redis = Redis(host='10.16.4.139', port=6379, db=0, )
app = Flask(__name__)
redis.set('mykey', 'Hello from Python!')
@app.route('/')
def index():
    #print('Try')
    #redis.set('mykey', 'Hello from Python!')
    return render_template('./app.html')
 
if __name__ == '__main__':
   port = int(os.environ.get("PORT", 9595))
   app.run(debug=True,host='0.0.0.0',port=port)
