from flask import Flask, escape, request
import json

with open('./ports.json', 'r') as ports: 
    port_db = json.load(ports)

app = Flask(__name__)








@app.route('/')
def hello():

    return json.dumps( {
        "subresource_uris": {
            "movies": "/movies",
            "movie": "/movies/<id>",
            "bookings": "/bookings",
            "booking": "/bookings/<username>",
            "showtimes": "/showtimes",
            "showtime": "/showtimes/<date>",
            "users": "/users",
            "user": "/users/<username>",
            "bookings": "/users/<username>/bookings",
            "suggested": "/users/<username>/suggested"
        }}, sort_keys = True, indent=4)
    
    
if __name__ == '__main__':

    
    app.run(host= '0.0.0.0', port= '5008', debug=True )