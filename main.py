from flask import Flask, render_template, jsonify, request
from redis import Redis, RedisError
import os 
import socket



redis = Redis(host="redis", db=0)
app = Flask(__name__)

@app.route('/')
def index():
    #print('Try')
    redis.set('mykey', 'Hello from Python!')
    return render_template('./app.html')
 

#value = redis.get('mykey')
#print(value)

#redis.zadd('vehicles', {'car' : 0})
#redis.zadd('vehicles', {'bike' : 0})
#vehicles = redis.zrange('vehicles', 0, -1)
    # return jsonify({'data': "shubham"})
  
  
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
# @app.route('/', methods = ['GET', 'POST'])    
# def home():
#     if(request.method == 'GET'):
  
#         data = "hello world"
#         return jsonify({'data': data})
    


if __name__ == '__main__':
   port = int(os.environ.get("PORT", 9595))
   app.run(debug=True,host='0.0.0.0',port=port)
