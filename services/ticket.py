from flask import Flask,request, abort
from services import root_dir, nice_json
from werkzeug.exceptions import NotFound
import json
from bson import json_util
import pymongo

client = pymongo.MongoClient('0.0.0.0:27017')

cinema_db = client['cinema_db']
ticket_collection = cinema_db['ticket']


app = Flask(__name__)

@app.route("/tickets/<ticketid>", methods=['GET'])
def ticket_info(ticketid):

    tickets = ticket_collection.find({})
    
    for ticket in tickets:
        
        if str(ticket['_id']) == ticketid:

            return json_util.dumps(ticket, sort_keys=True, indent=4)

    return 'Not Find'


@app.route("/tickets", methods=['GET'])
def ticket_record():

    tickets = ticket_collection.find({})
    
    return json_util.dumps(tickets, sort_keys=True, indent=4)

@app.before_request
def limit_remote_addr():
    if request.remote_addr != '127.0.0.1':
        abort(403)


if __name__ == "__main__":
    app.run(port=5005, debug=True)
