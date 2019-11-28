import requests as rqst
from flask import Flask, escape, request
import json
import os
import threading

with open('./service_list.json', 'r') as service_json: 
    
    service_mods = json.load(service_json)

with open('./ports.json', 'r') as ports: 
    
    port_db = json.load(ports)


app = Flask(__name__)


def route_servise(mode):

    service_name = mode.split('/')[1]

    service_port = port_db[service_name]

    service_result = rqst.get('http://0.0.0.0:' + service_port + mode)

    return service_result.content



@app.route('/', methods = ['GET', 'POST'])
def hello():

    if request.method == 'POST':

        post_json = request.json['mode']

        service_name = route_servise(post_json)

        return service_name

    return json.dumps(service_mods, sort_keys = True, indent=4)


if __name__ == '__main__':

    service_list = ['user.py','ticket.py','bookings.py','campaign.py','movies.py','showtimes.py'] 


    app.run(host= '0.0.0.0', port= '5008', debug=True )