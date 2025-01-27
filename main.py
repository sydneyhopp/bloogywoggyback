from flask import Flask, jsonify
from flask import request
from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi # don't know why MongoDB suggest this

uri = "mongodb+srv://admin:<joeSydsam>@clusterwuster.rgsli.mongodb.net/?retryWrites=true&w=majority&appName=ClusterWuster"

app = Flask(__name__)

# Create a new client and connect to the server
client = MongoClient(uri)
db = client.database

# health check
@app.route('/health', methods=['GET'])
def health_check():
    """Healthy wealthy"""
    return jsonify({
        'status':'healthy',
        'message':'server runnin'
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
    
# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
    print(e)