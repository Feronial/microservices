from flask import Flask, escape, request
import json

app = Flask(__name__)

def alive():

    return 0


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

if __name__ == '__main__':

    a = {'movies' : '5001',
         'payment' : '5002',
         'campaign' : '5003',
         'booking' : '5004',
         'showtimes' : '5005',
         'ticket' : '5006',
         'user' : '5007'

    }

    with open('ports.json', 'w') as outfile:
        json.dump(a, outfile)
    

    print(b)

    #app.run(host= '0.0.0.0', port= '5001', debug=True )