from flask import Flask
from services import root_dir, nice_json
from werkzeug.exceptions import NotFound
import json
from bson import json_util
import pymongo

client = pymongo.MongoClient('0.0.0.0:27017')

cinema_db = client['cinema_db']
campaign_collection = cinema_db['campaign']


app = Flask(__name__)

@app.route("/campaigns/<campaignid>", methods=['GET'])
def campaign_info(campaignid):

    campaigns = campaign_collection.find({})
    
    for campaign in campaigns:

        print(type(campaign['_id']))
        
        if str(campaign['_id']) == campaignid:

            return json_util.dumps(campaign, sort_keys=True, indent=4)

    return 'Not Find'


@app.route("/campaigns", methods=['GET'])
def campaign_record():

    campaigns = campaign_collection.find({})
    
    return json_util.dumps(campaigns, sort_keys=True, indent=4)




if __name__ == "__main__":
    app.run(port=5004, debug=True)
